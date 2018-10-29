# Report on segmentation task

For this task I used Pragmatic segmenter and NLTK's Punkt. Both of them performed quite well while segmenting Russian text. However, there were some problems which we are to consider.

## Pragmatic segmenter

**Accuracy**: 0.97

Pragmatic segmenter could not cope with the abbreviation 'н. э.' and divided one sentence into two by mistake:

> Традиционно считается, что этническая основа Литвы сформирована носителями археологочической культуры восточнолитовских курганов, сформировавшейся в V веке н. э. \
> на территории современных Восточной Литвы и Северо-Западной Белоруссии.

Although, in the following example the segmenter did not make such a mistake (probably due to the bracket following the abbreviation):

> В конце неолита (III-II тыс. до н. э.) на территорию современной Литвы проникли индоевропейские племена.

Similar problem was found out with the abbreviation 'см.':

> В 1944 году нацисты были изгнаны Красной Армией с территории Литовской ССР (см.\
> Белорусская операция (1944)).

In all other cases the segmenter performed very well.

## NLTK's PUNKT

**Accuracy**: 0.95

This segmenter performed a little worse than the previous one. It could not cope with the abbreviation 'н. э.' as well, but made a wider range of mistakes.

Did not find the border between 2 sentences:

> Территория современной Литвы была заселена людьми с конца X—IX тысячелетия до н. э. Жители занимались охотой и рыболовством, использовали лук и стрелы с кремнёвыми наконечниками, скребки для обработки кожи, удочки и сети. - не разделилось

Made too many borders:

> В конце неолита (III-II тыс.\
> до н.\
> э.)

One more example with the abbreviation 'тыс.':

> Более 3 тыс.\
> озёр

The following example, however, shows that in some cases 'н. э.' was recognized as an abbreviation:

> Около VII века н. э. литовский язык отделился от латышского.

Another problem showed up while considering the abbreviation 'см.' (exactly the same case as we saw in Pragmatic segmenter):

> В 1944 году нацисты были изгнаны Красной Армией с территории Литовской ССР (см.\
> Белорусская операция (1944)).
