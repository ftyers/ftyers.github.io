class Eval:
    def score(gold, parsed):

        tp,tn,fp,fn = (0,0,0,0)
        for g in range(0,len(parsed),4):
            for ind in range(len(gold[g:g+4])):
                i,j=(0,0)
                first = list(gold[ind])
                second = list(parsed[ind])
                while i<=(len(first)-1):
                    g_s_l = first[i]
                    p_s_l = second[j]
                    punct=',-:。“”【】?、_.「」・/\|%~!'
                    if (g_s_l.isalpha() or g_s_l in punct) and (p_s_l.isalpha() or g_s_l in punct):
                        tn+=1
                        i+=1
                        j+=1
                    if g_s_l==' ' and p_s_l==' ':
                        tp+=1
                        i += 1
                        j += 1
                    if g_s_l==' ' and (p_s_l.isalpha()or p_s_l in punct):
                        fn+=1
                        i += 1
                    if (g_s_l.isalpha()or g_s_l in punct) and p_s_l==' ':
                        j += 1
                        fp+=1
        #print ('TruePositive: {0}, TrueNegative: {1}, FalsePositive: {2}, FalseNegative: {3}'.format(tp,tn,fp,fn))
        Acc = (tp+tn)/float(tp+tn+fp+fn)
        Prec = tp/float(tp+fp)
        print('Accuracy: {}, Precision: {}'.format(round(Acc,2), round(Prec,2)))
