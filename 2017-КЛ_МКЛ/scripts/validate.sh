IN=$1
HEAD=`grep -nH 'LEXICON Root' $IN  | cut -f2 -d':'`
for i in `cat $IN | grep -o '%<[^>]\+%>' | sort -u`; do 
	cat $IN | head -n $HEAD | grep "$i" | wc -l | sed "s/$/\t$i/g" | grep "^0";
done 
