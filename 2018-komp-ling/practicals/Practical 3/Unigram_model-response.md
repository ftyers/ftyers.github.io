# Practical 3
## Functions
Output (first 10 lines) from running the [script](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%203/palindrome.py) for finding palindromes 
on the freq.txt file from the previous practical:
```
3439    как  
1669    или  
1254    еще  
1085    ее  
283     тут  
279     тот  
190     оно  
90      XX  
80      11  
71      XIX  
```

## Implementing n dimensional matrices with dict

I implemented the code from the task and got this output:
```
	a	absorbed	all	and	another
бы	0	0	0	0	0	
вас	0	0	0	0	0	
видит	0	0	0	0	0	
всего	0	0	0	0	0	
вы	0	0	0	0	0	
```
>Why do we need end='' passed to the print() statement ? What would happen if we didn't have it?

We need ```end=''``` to avoid printing every new element at the new line, because ```\n``` is the default ending.
Without this ending we have this table:
```
	a	absorbed	all	and	another
бы	
0	
0	
0	
0	
0	

вас	
0	
0	
0	
0	
0	

видит	
0	
0	
0	
0	
0	

всего	
0	
0	
0	
0	
0	

вы	
0	
0	
0	
0	
0	

```
After saving [this](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%203/args.py) code and running it in the command line using
```$ python3 args.py a b c ```

I had this output:
```['args.py', 'a', 'b', 'c']```
-- it's the list of arguments passed to the command line.

## Unigram language model
Here is my code train.py 
