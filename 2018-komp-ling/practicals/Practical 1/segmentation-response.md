# Segmentation
1.  I downloaded my texts from a Wikipedia dump of Russian and used WikiExtractor to extract them. Then I chose 50 paragraphs of random texts with this bash command:

    `head -n 50000 wiki.txt | sort -R | head -n 50 > 50random.txt`

    So, this was my [data](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/50random.txt).

2. Applied Ruby's pragmatic_segmenter to it:

    `ruby -I . segmenter.rb < 50random.txt > pragmatic_segmenter_result.txt`
    
   [That's](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/pragmatic_segmenter_result.txt) what I've got.
   
3. Then I wrote [my implementation using NLTK's Punkt.](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/Segmentator%201.py)
    
    [Here](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/nltk_punkt_result.txt) is the results.
    
## Comparison of results
Both methods gave out the same number of sentences — 134. However, the sentences are different. 

Thus, pragmatic_segmenter divided basic Russian abbreviation "т. к." as two sentences:
> Мясо барана разделывают по суставам, при этом следят за тем, чтобы в бараний желудок (гюзян) не попали острые части, т.  
> к.  
> они могут его повредить.

NLTK's segmenter managed that task but also had troubles with abbreviation. For example, it separated language abbreviations like "тиб."  and "санскр.".
>Херуками, например, являются тантрические божества Чакрасамвара (тиб.  
>Демчог) и Вишуддха Херука (тиб.  
>Яндаг Херука).

While pragmatic_segmenter got ot right.
>Херуками, например, являются тантрические божества Чакрасамвара (тиб. Демчог) и Вишуддха Херука (тиб. Яндаг Херука).

## Evaluation

As both approaches gave quantitatively the same results on my data, there is no need to count their accuracy (it will be the same). What's interesting is that they make different types of mistakes. 
