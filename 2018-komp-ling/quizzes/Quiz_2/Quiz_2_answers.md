**Quiz 2**

1&2.

There is much information we should take into account, building such a transducer. For instance, in ‘’children’s clothing’’ it would be a mistake to expand «’s» to get «is». Thus, we can think of a transducer that restricts an application of a rule, allowing it to work only with nouns in singular form.


| cat | +N | +SG |+SH_IS |
|-------|------|------|----|
| cat | ^     | ‘     |s |
| cat | < space > | i |s


There are certainly other options when such transducer expands «’s» in a wrong way:  
— «’s» using to form the possessive of singular nouns: *girl’s power*  
— «’s» using to form the possessive of word groups functioning as nouns: *the boy with a sandwich’s wallet*   
— short form of ‘us’: *let’s dance*  
— short form of ‘was’: *where’s he last night?*  
— short form of ‘has’: *she’s seen him*  
— short form of ‘does’: *what’s he want?*       

To cope with the problem, having all these possibilities, we can only with the help of morphological/syntactical disambiguation and even semantical analysis — all of that, as far as I know, is unresolvable within FST only.         


3. Advantages of two-level formalism:    

a) Declarative rather than procedural  
b) Parallel application rather than sequential  
c) More expressive than rewrite rules            


4.

a) Using the rewrite rules without changes

It’s not possible to use sequential rewrite rules as parallel two-level rules without changes since in the case of two-level rules there is a reference to both the lexical (input) and the surface contexts. For instance, let’s compare sequential rewrite rules and two-level rules which convert the lexical string *kaNpan* to the surface representation *kamman*. Sequential rewrite rules are the following:

    N stands for an underspecified nasal that is realized as a labial (N:m) or as a dental (N:n) depending on the environment.
    
    (a) N -> m / _ p; elsewhere, n.
    (b) p -> m / m _

Two-level rules for this case are:

    (a) N:m <=>    _ p:
    (b) p:m <=> :m _

In the first case ‘p’ and ‘m’ in the rule’s context stand for input representation, whereas in the second case, with twol rules, ‘p:’ stand for input (lexical) representation and ‘:m’ — for surface. If we try to implement the first rules as twol rules without changes (even not to mention different notation and different approach in regard to operators), we’ll get the rule where on the right there is ‘lexical p realized as p on the surface’ — and it will block the realization of the *kaNpan* as *kamman*. As the application of twol rules is parallel and there is no intermediate representation this reference to both contexts is essential for the adequate analysis and derivation — and thus, it can’t be treated like sequential rewrite rules.  

b) Underspecifying the rewrite rules

Underspecification is indeed a very useful option in twol system and it can help to get the properly working rules from sequential rewrite rules. Let’s consider the rules which appropriately form the genitive of Finnish word maku ‘taste’ as maun, but the genitive of puku ‘dress’ as puvun (intervocalic k is realized as v only between two ‘u’, in other contexts it disappears). The rule that turns *k* to *v* applies in the more specific context — and thus should be ordered in sequential rules system before the rule with the more general context:

    (a) k -> v / u _ u C (C) #
    (b) k -> ∅ / V _ V C (C) # 

In case of twol parallel framework it’s impossible to formulate rules like that because there is a fatal conflict with one another (since ‘u’ is a vowel). But is’t possible to avoid the conflict if we make the general rule more general, allowing for several options: 

    (a) k:v <=> u _ u C [#: | C]	
    (b) k:[epsilon] | k:v <= V _ V C [#: | C]	

The same strategy can be applied also for overlapping harmony systems (as in Turkish). The point is that there is no need for each rule to determine the outcome fully — the rules can be designed in such way that applied together, in parallel, they cover all the cases correctly and definitely. 

c) Subtracting the context of the more general rule from the more specific

I can hardly imagine the situation when it’s possible to subtract the context of the more general rule from the more specific, since specific rule is a subset of the general one — and it’s impossible to subtract the set from its subset with a meaningful result. 

d) Subtracting the context of the more specific rule from the more general

It is possible to make the general rule a bit more specific by subtracting the context of the more specific rule from it, for instance: 

    (b') k:[epsilon] <=	[V - u]	_  [V - u] C [#: | C]
       			[V - u]	_ u C [#: | C]
       		      	      u	_ [V - u] C [#: | C]

It’s clear that such rule is rather complicated and, thus, isn’t the best choice. 
There is also an option to construct rules, using extra restrictions with the help of an except clause. For example, take some phonological rules in Chuvash:

    ‘Non surface {Ă} in plural genitive’                                                                  
    %{Ă%}:0 <=> %{м%}: %>: _ н ; 

    ‘Back vowel harmony for archiphoneme {Ă}’     
    %{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;

These rules contradict each other. To resolve the conflict (that doesn’t exist if we apply rules sequentially, one by one) we can ‘subtract’ the context of the more specific rule using except clause like this: 

    "Back vowel harmony for archiphoneme {Ă}"
    %{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
        		except
                                       %{м%}: %>:  _ н ;


5. 
‘insert an e after a morpheme-final, which belongs to ‘soft consonant sounds’: ch, sh, tz, _s, _x, — and before the morpheme s’

    ε —> e / {ch | sh | tz | _s | _x} ^ __ s#
    
Script for pluralizing words with the tag `<PL>` (from command line):
    
    import re

    word = input('Enter the word (with <PL> tag) you want to pluralize: ')

    def plural(word):

        if re.search('[A-Za-z]+(ch|sh|tz|s|x)<PL>', word):
            word_pl = word[:word.index('<PL>')] + 'es'
            return(word_pl)
        elif re.search('([A-Za-z]+)<PL>', word):
            word_pl = word[:word.index('<PL>')] + 's'
            return(word_pl)
        else:
            return(plural(input('Try again: ')))

    print(plural(word))

Script for pluralizing words with the tag `<PL>` (from stdin):

    import sys, re

    def plural(word):

        if re.search('[A-Za-z]+(ch|sh|tz|s|x)<PL>', word):
            word_pl = word[:word.index('<PL>')] + 'es'
            return(word_pl)
        elif re.search('([A-Za-z]+)<PL>', word):
            word_pl = word[:word.index('<PL>')] + 's'
            return(word_pl)
        else:
            return('smth went wrong (maybe you forgot to add <PL>)')

    for line in sys.stdin.readlines():
        lines = line.strip()
        print(plural(lines))
