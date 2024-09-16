# Xrenner Response

So, the first - we must make all preparation, like install the xrenner etc:
The standart model for english language works just fine:

    $ python3 xrenner.py -m eng -o html example_in.conll10 > /mnt/c/sub_wsl/example.html
  
Next, we must make our language model (in this case - russian). We can make this model from scratch, or copy a meta-language folder:

    $ cp -R ./models/udx ./models/rus

### Rules

Add some rules to our model.

__pronouns.tab:__

    я       1sg 
    мы      1pl 
    он      male
    она     fema
    его     male
    её      fema
    меня    1sg 
    нас     1pl 

__coref.tab:__

    Рабиндранат Тагор|Тагор       coref
    
This simple rules give us a great results (see: pushkin.html):
  
    $ python3 xrenner.py -m rus -o html pushkin.conllu > /mnt/c/sub_wsl/pushkin.html
    
