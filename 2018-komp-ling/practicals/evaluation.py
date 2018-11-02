def main():
    print('Insert file name with original segmentation')
    f = str(input())
    print('Insert file name with your segmentation')
    p = str(input())

    all_sent = open(f, "r", encoding="utf-8").read().splitlines()
    parsed_s = open(p, "r", encoding="utf-8").read().splitlines()

    tp,tn,fp,fn = (0,0,0,0)

    for g in range(0,577,4):
        for ind in range(len(all_sent[g:g+4])):
            i,j=(0,0)
            first = list(all_sent[ind])
            second = list(parsed_s[ind])
            while i<=(len(first)-1):
                g_s_l = first[i]
                p_s_l = second[j]
                punct=',-:。“”【】?、_.「」・/\|%~!'
                if (g_s_l.isalpha() or g_s_l in punct) and (p_s_l.isalpha() or p_s_l in punct):
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
    print ('TruePositive: {0}, TrueNegative: {1}, FalsePositive: {2}, FalseNegative: {3}'.format(tp,tn,fp,fn))
    Acc = (tp+tn)/float(tp+tn+fp+fn)
    Prec = tp/float(tp+fp)
    Recall = tp/float(tp+fn)
    Fscore = 2*Prec*Recall/float(Prec+Recall)
    print('Accuracy: {}, F-score: {}'.format(round(Acc, 2), round(Fscore, 2)))

main()