
# Segmentation report

For the current task NLTK Sentence Tokenizer and my own segmentator implementation (just a simple regular expression) for English texts were used. 

Both of them performed quite well:
- NLTK segmentator identified 209 sentences 
- regex segmentator identified 220 sentences

Both segmentators made mistakes with processing abbreviations like *i.e.*. However, they did it in a different way: NLTK segmentator marked the end of a sentence after the whole *i.e.* while regex segmentator put the border either after *i.* and *e.*. 


```python
# NLTK_segmentation
from nltk.tokenize import sent_tokenize

with open('wiki_paragraphs.txt', 'r', encoding='utf8') as infile:
    data = infile.read()

sent_tokenize_NLTK = sent_tokenize(data, language='english')

for sent in sent_tokenize_NLTK:
    print('\n======\n' + sent)
```

    
    ======
    Anarchism is an anti-authoritarian political philosophy that advocates self-governed societies based on voluntary, cooperative institutions and the rejection of hierarchies those societies view as unjust.
    
    ======
    These institutions are often described as stateless societies, although several authors have defined them more specifically as distinct institutions based on non-hierarchical or free associations.
    
    ======
    Anarchism holds the state to be undesirable, unnecessary, and harmful.
    
    ======
    Anarchism is often considered a far-left ideology, and much of anarchist economics and anarchist legal philosophy reflect anti-authoritarian interpretations of communism, collectivism, syndicalism, mutualism, or participatory economics.
    
    ======
    Anarchism does not offer a fixed body of doctrine from a single particular world view, instead fluxing and flowing as a philosophy.
    
    ======
    Many types and traditions of anarchism exist, not all of which are mutually exclusive.
    
    ======
    Anarchist schools of thought can differ fundamentally, supporting anything from extreme individualism to complete collectivism.
    
    ======
    Strains of anarchism have often been divided into the categories of social and individualist anarchism or similar dual classifications.
    
    ======
    The etymological origin of anarchism derives from ancient Greek word "anarkhia".
    
    ======
    "Anarkhia " meant "without a ruler" as it was composed by the prefix "a" (i.e "without") and the word "arkhos" (i.e leader or ruler).
    
    ======
    The suffix -ism is used to denote the ideological current that favours anarchism.
    
    ======
    The first known use of this word was in 1642.
    
    ======
    Various factions within the French Revolution labelled opponents as anarchists although few shared many views of later anarchists.
    
    ======
    There would be many revolutionaries of the early nineteenth century who contributed to the anarchist doctrines of the next generation, such as William Godwin and Wilhelm Weitling, but they did not use the word "anarchist" or "anarchism" in describing themselves or their beliefs.
    
    ======
    The first political philosopher to call himself an anarchist was Pierre-Joseph Proudhon, marking the formal birth of anarchism in the mid-nineteenth century.
    
    ======
    Since the 1890s and beginning in France, the term "libertarianism" has often been used as a synonym for anarchism and its use as a synonym is still common outside the United States.
    
    ======
    On the other hand, some use libertarianism to refer to individualistic free market philosophy only, referring to free market anarchism as libertarian anarchism.
    
    ======
    Defining anarchism is not an easy task.
    
    ======
    There is a lot of talk among scholars and anarchists on the matter and various currents perceive anarchism slightly differently.
    
    ======
    Hence, it might be true to say that anarchism is a cluster of political philosophies rejecting hierarchies (including the state and all associated institutions), in favour of a society based on voluntary association, freedom and decentralization.
    
    ======
    This definition though has its own shortcomings, as the definition based on etymology (which is simply a negation of a ruler), or based on anti-statism (anarchism is much more than that) or even the anti-authoritarian (which is an "a posteriori" concussion) Major elements of the definition of anarchism include a)the will for a non coercive society b)the rejection of State apparatus, c)belief in human nature, even though it is even harder to define it than anarchism d)a suggestion on how to act to pursue the ideal of anarchy.
    
    ======
    During the prehistoric era of mankind, an established authority did not exist; humans were living in anarchistic societies.
    
    ======
    It was after the creation of towns and cities that hierarchy was invented and as a reaction, anarchistic ideas espoused.
    
    ======
    Most notable examples of anarchism in the ancient world were in China and Greece.
    
    ======
    In China philosophical anarchism, meaning peaceful delegitimizing of the state, was delineated by Taoist philosophers (i.e.
    
    ======
    Zhuangzi and Lao Tzu).
    
    ======
    Likewise in Greece, anarchist attitudes were articulated by tragedians and philosophers.
    
    ======
    Aeschylus and Sophocles used the myth of Antigone to illustrate the conflict of personal autonomy with the state rules.
    
    ======
    Socrates questioned Athenian authorities constantly and insisted to the right of individual freedom of consciousness.
    
    ======
    Cynics dismissed human law ("Nomos") and associated authorities while trying to live according to nature ("physis").
    
    ======
    Stoics were supportive of a society based on unofficial and friendly relations among its citizens without the presence of a state.
    
    ======
    During the Middle Ages, there was no anarchistic activity except some ascetic religious movements in the Islamic world or in Christian Europe.
    
    ======
    This kind of tradition later gave birth to religious anarchism.
    
    ======
    In Persia, a Zoroastrian Prophet, Mazdak, was calling for an egalitarian society and the abolition of monarchy.
    
    ======
    He soon found himself executed by the King.
    
    ======
    In Basra, religious sects preached against the State.
    
    ======
    In Europe, various sects developed anti-state and libertarian tendencies.
    
    ======
    Those currents were the precursor of religious anarchism in the centuries to come.
    
    ======
    It was in Renaissance and along with the spread of reasoning and humanism through Europe, libertarian ideas emerged.
    
    ======
    Writers were outlining in their novels ideal societies that were based not on coercion but voluntarism.
    
    ======
    Enlightenment further pushed towards anarchism with the optimism for social progress.
    
    ======
    The turning point towards anarchism was the French Revolution.
    
    ======
    Anarchists per se didn't take part, but the anti-state and federalist sentiments began to take a form, mostly by "enrages" and "sans culottes".Some prominent figures of anarchism begun developing the first anarchist currents.
    
    ======
    That is the era of classical anarchism that lasted until the end of the Spanish Civil War and was the belle epoque of anarchism.
    
    ======
    William Godwin in England espoused to philosophical anarchism, morally delegitimizing the state, Max Stirner thinking paved the way to individualism and Pietr Joseph Proudhon's theory of mutualism, found fertile soil in France.
    
    ======
    Michael Bakunin took mutualism and extended it to anarcho-collectivism.
    
    ======
    Bakunin's current (Jura Federation) entered the class worker union, International Workingmen's Association (or First International) which was formed in 1864, to unite diverse revolutionary currents.
    
    ======
    Due to its links to active workers' movements, the International became a significant organisation.
    
    ======
    Karl Marx became a leading figure in the International and a member of its General Council.
    
    ======
    Proudhon's followers, the mutualists, opposed Marx's state socialism, advocating political abstentionism and small property holdings.
    
    ======
    Bakunin's followers entered a bitter dispute with Karl Marx which ended with the split of Worker movement, that officially took place in the Fifth Congress of IWA in the Hague, 1872.
    
    ======
    The major reason lied on fundamentally different approaches on how the workers would emancipate themselves.
    
    ======
    Marx was advocating for the creation of a political party, taking part in electoral struggles, whereas Bakunin thought that the whole set of Marx's thinking was very authoritarian.
    
    ======
    Bakunin is famous for predicting that if such a party would gain power by Marxist's terms, it will end up to be the new tyrant of workers.
    
    ======
    After being expelled from the first international, anarchists formed the St. Imier International.
    
    ======
    Under the spell of Kropotkin, a Russian philosopher and respectful scientist, anarcho-communism overlapped collectivism.
    
    ======
    Anarcho-communists, who drew inspiration from Paris Commune, advocated for free federation and distribution of goods according to one needs.
    
    ======
    The major argument of anarcho-communism was that Bakunian perspective would lead to antagonism among collectives.
    
    ======
    At the turning of the century, anarchism has spread all over the world.
    
    ======
    In China, small groups of students imported the humanistic pro-science version of anarcho-communism.
    
    ======
    Tokyo was a hotspot for rebellious youth from countries of the far east, pouring into Japanese capital to study.
    
    ======
    In Latin America, Sao Paolo was a stronghold and anarchosyndicalism was the most prominent left wing ideology.
    
    ======
    During that time, a minority of anarchists embarked into utilizing of violence in order to achieve their political ends.
    
    ======
    This kind of strategy is named as propaganda by the deed.
    
    ======
    The dismemberment of the French socialist movement into many groups and—following the suppression of the 1871—Paris Commune the execution and exile of many communards to penal colonies favoured individualist political expression and acts.
    
    ======
    Even though many anarchists distanced themselves to those terrorist acts, anarchists were persecuted and were given bad fame.
    
    ======
    Illegalism, stealing the possessions of the rich, because capitalists were not their rightful owners was another strategy some anarchist adopted during the same years.
    
    ======
    Anarchists took part enthusiastically in the Russian revolution.
    
    ======
    Anarchists during the revolution had concerns but opted for the revolution than supporting the Whites.
    
    ======
    But they met harsh suppression after the Bolshevik regime was stabilized.
    
    ======
    Anarchists in central Russia were either imprisoned, driven underground or joined the victorious Bolsheviks; the anarchists from Petrograd and Moscow fled to Ukraine.
    
    ======
    Kronstadt rebellion and Machno's struggle in Ukraine were the most notable examples.
    
    ======
    After anarchist being crashed in Russia, two new antithetical currents emerged: Platformism and Synthesis anarchism.
    
    ======
    Platformists sought to create a coherent group that would push for the revolution while the latter were against anything that would resemble a political party.
    
    ======
    The victory of the Bolsheviks in the October Revolution and the resulting Russian Civil War did serious damage to anarchist movements internationally.
    
    ======
    Many workers and activists saw Bolshevik success as setting an example and communist parties grew at the expense of anarchism and other socialist movements.
    
    ======
    In France and the United States, for example, members of the major syndicalist movements of the General Confederation of Labour and Industrial Workers of the World (IWW) left the organisations and joined the Communist International.
    
    ======
    In the Spanish Civil War, anarchist's most glorious moment, anarchists and syndicalists (CNT and FAI) once again allied themselves with various currents of leftists.
    
    ======
    Spain had a long anarchist tradition, and thus anarchist played an important role in the Civil War.
    
    ======
    In response to the army rebellion, an anarchist-inspired movement of peasants and workers, supported by armed militias, took control of Barcelona and of large areas of rural Spain where they collectivised the land.
    
    ======
    USSR provided some limited assistance at the beginning of the civil war, but as Stalin tried to seize control of the Republicans, the result was a bitter fight among communists and anarchists (i.e.
    
    ======
    at a series of events named May Days).
    
    ======
    Despite their heroic effort, they were ultimately defeated, leaving an ultimate question: should the anarchist join or not the Democratic group to fight the fascists?
    
    ======
    The first years after World War II, anarchism seemed inexisted, a ghost of itself.
    
    ======
    So it was kind of a surprise that the '60s witnessed a revival of anarchism.
    
    ======
    Main causes may have been the miserable failure of authoritarian communism and alongside with the tension build by Cold War.
    
    ======
    During this era, anarchism was mostly part of other movements critical to State and Capitalism, ie within the Anti-nuclear movementand pacifist movement, New Left, the Greens or the counter-culture.
    
    ======
    Anarchism was also associated with the punk rock movement as exemplified by bands such as Crass and the Sex Pistols..
    
    ======
    Although feminist tendencies have always been a part of the anarchist movement in the form of anarcha-feminism, they returned with vigour during the second wave of feminism in the 1960s.
    
    ======
    Around the turn of the 21st century, anarchism grew in popularity and influence as part of the anti-war, anti-capitalist, and anti-globalisation movements.
    
    ======
    Anarchists became known for their involvement in protests against the meetings of the World Trade Organization (WTO), Group of Eight (G8) and the World Economic Forum (WEF).
    
    ======
    Some anarchist factions at these protests engaged in rioting, property destruction, and violent confrontations with police.
    
    ======
    These actions were precipitated by ad hoc, leaderless, anonymous cadres known as black blocs—other organisational tactics pioneered in this time include security culture, affinity groups and the use of decentralised technologies such as the internet.
    
    ======
    A significant event of this period was the confrontations at WTO conference in Seattle in 1999.
    
    ======
    Anarchist ideas have been influential in the development of the Zapatista movement in Chiapas, Mexico and the Democratic Federation of Northern Syria (DFNS), more commonly known as Rojava, a "de facto" autonomous region in northern Syria.
    
    ======
    Anarchist schools of thought had been generally grouped in two main historical traditions, individualist anarchism and social anarchism, which have some different origins, values and evolution.
    
    ======
    The individualist wing of anarchism emphasises negative liberty, i.e.
    
    ======
    opposition to state or social control over the individual, while those in the social wing emphasise positive liberty to achieve one's potential and argue that humans have needs that society ought to fulfil, "recognising equality of entitlement".
    
    ======
    In a chronological and theoretical sense, there are classical—those created throughout the 19th century—and post-classical anarchist schools—those created since the mid-20th century and after.
    
    ======
    Beyond the specific factions of anarchist thought is philosophical anarchism, which embodies the theoretical stance that the state lacks moral legitimacy without accepting the imperative of revolution to eliminate it.
    
    ======
    A component especially of individualist anarchism philosophical anarchism may accept the existence of a minimal state as unfortunate, and usually temporary, "necessary evil" but argue that citizens do not have a moral obligation to obey the state when its laws conflict with individual autonomy.
    
    ======
    One reaction against sectarianism within the anarchist milieu was "anarchism without adjectives", a call for toleration first adopted by Fernando Tarrida del Mármol in 1889 in response to the "bitter debates" of anarchist theory at the time.
    
    ======
    In abandoning the hyphenated anarchisms (i.e.
    
    ======
    collectivist-, communist-, mutualist- and individualist-anarchism), it sought to emphasise the anti-authoritarian beliefs common to all anarchist schools of thought.
    
    ======
    The various anarchist schools of thought or currents are not distinct entities but intermingle with each other.
    
    ======
    Collectivist, Communist and Anarcho-syndicalism are considered a form of social anarchism.
    
    ======
    Mutualism and Individualism were the other notable anarchist currents through the 19th and early 20th century.
    
    ======
    Social anarchism rejects private property, seeing it as a source of social inequality (while retaining respect for personal property) and emphasises cooperation and mutual aid.
    
    ======
    Mutualism began in 18th-century English and French labour movements before taking an anarchist form associated with Pierre-Joseph Proudhon in France and others in the United States.
    
    ======
    Proudhon proposed spontaneous order, whereby organisation emerges without central authority, a "positive anarchy" where order arises when everybody does ""what he wishes and only what he wishes"" and where "business transactions alone produce the social order."
    
    ======
    Proudhon distinguished between ideal political possibilities and practical governance.
    
    ======
    For this reason, much in contrast to some of his theoretical statements concerning ultimate spontaneous self-governance, Proudhon was heavily involved in French parliamentary politics and allied himself not with anarchist but socialist factions of workers' movements and, in addition to advocating state-protected charters for worker-owned cooperatives, promoted certain nationalisation schemes during his life of public service.
    
    ======
    Mutualist anarchism is concerned with reciprocity, free association, voluntary contract, federation, and credit and currency reform.
    
    ======
    According to the American mutualist William Batchelder Greene, each worker in the mutualist system would receive ""just and exact pay for his work; services equivalent in cost being exchangeable for services equivalent in cost, without profit or discount"".
    
    ======
    Mutualism has been retrospectively characterised as ideologically situated between individualist and collectivist forms of anarchism.
    
    ======
    Proudhon first characterised his goal as a ""third form of society, the synthesis of communism and property [which] we call LIBERTY"".
    
    ======
    Collectivist anarchism, also referred to as revolutionary socialism or a form of such, is a revolutionary form of anarchism, commonly associated with Mikhail Bakunin and Johann Most.
    
    ======
    At the epicentre of collectivist anarchism lies the belief in the potential of humankind for goodness and solidarity, which will flourish when oppressive governments are abolished.
    
    ======
    Collectivist anarchists oppose all private ownership of the means of production, instead advocating that ownership be collectivised.
    
    ======
    This was to be achieved through violent revolution, first starting with a small cohesive group through acts of violence, or propaganda by the deed, which would inspire the workers as a whole to revolt and forcibly collectivise the means of production.
    
    ======
    However, collectivisation was not to be extended to the distribution of income as workers would be paid according to time worked, rather than receiving goods being distributed "according to need" as in anarcho-communism.
    
    ======
    This position was criticised by anarchist communists as effectively "uphold[ing] the wages system".
    
    ======
    Collectivist anarchism arose contemporaneously with Marxism, but opposed the Marxist dictatorship of the proletariat despite the stated Marxist goal of a collectivist stateless society.
    
    ======
    Anarchist, communist and collectivist ideas are not mutually exclusive—although the collectivist anarchists advocated compensation for labour, some held out the possibility of a post-revolutionary transition to a communist system of distribution according to need.
    
    ======
    Anarcho-communism (also known as anarchist-communism, libertarian communism and occasionally as free communism) is a theory of anarchism that advocates abolition of the state, markets, money, private property (while retaining respect for personal property) and capitalism in favour of common ownership of the means of production, direct democracy and a horizontal network of voluntary associations and workers' councils with production and consumption based on the guiding principle: "From each according to his ability, to each according to his need".
    
    ======
    Some forms of anarchist communism such as insurrectionary anarchism are strongly influenced by egoism and radical individualism, believing anarcho-communism is the best social system for the realisation of individual freedom.
    
    ======
    Most anarcho-communists view anarcho-communism as a way of reconciling the opposition between the individual and society.
    
    ======
    Anarcho-communism developed out of radical socialist currents after the French Revolution but was first formulated as such in the Italian section of the First International.
    
    ======
    The theoretical work of Peter Kropotkin took importance later as it expanded and developed pro-organisationalist and insurrectionary anti-organisationalist sections.
    
    ======
    To date, the best known examples of an anarchist communist society (i.e.
    
    ======
    established around the ideas as they exist today and achieving worldwide attention and knowledge in the historical canon), are the anarchist territories during the Spanish Revolution and the Free Territory during the Russian Revolution.
    
    ======
    Through the efforts and influence of the Spanish anarchists during the Spanish Revolution within the Spanish Civil War, starting in 1936 anarchist communism existed in most of Aragon, parts of the Levante and Andalusia as well as in the stronghold of anarchist Catalonia.
    
    ======
    It was crushed by the combined forces of the Franco’s Nationalists, Hitler, and Mussolini, as well as repression by the Communist Party of Spain (backed by the Soviet Union) and economic and armaments blockades from the capitalist countries and the Spanish Republic itself.
    
    ======
    Anarcho-syndicalism is a branch of anarchism that focuses on the labour movement.
    
    ======
    Anarcho-syndicalists view labour unions as a potential force for revolutionary social change, replacing capitalism and the state with a new society democratically self-managed by workers.
    
    ======
    The basic principles of anarcho-syndicalism are workers' solidarity, direct action and workers' self-management.
    
    ======
    Anarcho-syndicalists believe that only direct action—that is, action concentrated on directly attaining a goal as opposed to indirect action, such as electing a representative to a government position—will allow workers to liberate themselves.
    
    ======
    Moreover, anarcho-syndicalists believe that workers' organisations (the organisations that struggle against the wage system, which in anarcho-syndicalist theory will eventually form the basis of a new society) should be self-managing.
    
    ======
    They should not have bosses or "business agents"—rather, the workers should be able to make all the decisions that affect them themselves.
    
    ======
    Rudolf Rocker was one of the most popular voices in the anarcho-syndicalist movement.
    
    ======
    He outlined a view of the origins of the movement, what it sought and why it was important to the future of labour in his 1938 pamphlet "Anarcho-Syndicalism".
    
    ======
    The International Workers Association is an international anarcho-syndicalist federation of various labour unions from different countries.
    
    ======
    The Spanish CNT played and still plays a major role in the Spanish labour movement.
    
    ======
    It was also an important force in the Spanish Civil War.
    
    ======
    Individualist anarchism refers to several traditions of thought within the anarchist movement that emphasise the individual and their will over any kinds of external determinants such as groups, society, traditions and ideological systems.
    
    ======
    Individualist anarchism is not a single philosophy, but it instead refers to a group of individualistic philosophies that sometimes are in conflict.
    
    ======
    In 1793, William Godwin, who has often been cited as the first anarchist, wrote "Political Justice", which some consider the first expression of anarchism.
    
    ======
    Godwin was a philosophical anarchist and from a rationalist and utilitarian basis opposed revolutionary action and saw a minimal state as a present "necessary evil" that would become increasingly irrelevant and powerless by the gradual spread of knowledge.
    
    ======
    Godwin advocated individualism, proposing that all cooperation in labour be eliminated on the premise that this would be most conducive with the general good.
    
    ======
    An influential form of individualist anarchism, called "egoism", or egoist anarchism, was expounded by one of the earliest and best-known proponents of individualist anarchism, the German Max Stirner.
    
    ======
    Stirner's "The Ego and Its Own", published in 1844, is a founding text of the philosophy.
    
    ======
    According to Stirner, the only limitation on the rights of individuals is their power to obtain what they desire without regard for God, state, or morality.
    
    ======
    To Stirner, rights were "spooks" in the mind and he held that society does not exist, but "the individuals are its reality".
    
    ======
    Stirner advocated self-assertion and foresaw unions of egoists, non-systematic associations continually renewed by all parties' support through an act of will, which Stirner proposed as a form of organisation in place of the state.
    
    ======
    Egoist anarchists argue that egoism will foster genuine and spontaneous union between individuals.
    
    ======
    "Egoism" has inspired many interpretations of Stirner's philosophy.
    
    ======
    It was re-discovered and promoted by German philosophical anarchist and homosexual activist John Henry Mackay.
    
    ======
    Josiah Warren was a pioneer American anarcho-individualist, who drew inspiration from Proudhon.
    
    ======
    Henry David Thoreau (1817–1862) was an important early influence in individualist anarchist thought in the United States and Europe.
    
    ======
    Thoreau was an American author, poet, naturalist, tax resister, development critic, surveyor, historian, philosopher and leading transcendentalist.
    
    ======
    He is best known for his books "Walden", a reflection upon simple living in natural surroundings, as well as his essay, "Civil Disobedience", an argument for individual resistance to civil government in moral opposition to an unjust state.
    
    ======
    Benjamin Tucker later fused Stirner's egoism with the economics of Warren and Proudhon in his eclectic influential publication "Liberty".
    
    ======
    From these early influences, individualist anarchism in different countries attracted a small yet diverse following of Bohemian artists and intellectuals, free love and birth control advocates (see anarchism and issues related to love and sex), individualist naturists and nudists (see anarcho-naturism), freethought and anti-clerical activists as well as young anarchist outlaws in what became known as illegalism and individual reclamation (see European individualist anarchism and individualist anarchism in France).
    
    ======
    These authors and activists included Oscar Wilde, Emile Armand, Han Ryner, Henri Zisly, Renzo Novatore, Miguel Gimenez Igualada, Adolf Brand and Lev Chernyi among others.
    
    ======
    Anarchist principles undergird contemporary radical social movements of the left.
    
    ======
    Interest in the anarchist movement developed alongside momentum in the anti-globalization movement, whose leading activist networks were anarchist in orientation.
    
    ======
    As the movement shaped 21st century radicalism, wider embrace of anarchist principles signaled a revival of interest.
    
    ======
    Contemporary news coverage, which emphasizes black bloc demonstrations, has reinforced anarchism's historical association with chaos and violence, though its publicity has also led more scholars to engage with the anarchist movement.
    
    ======
    Anarchism continues to generate many philosophies and movements, at times eclectic, drawing upon various sources and syncretic, combining disparate concepts to create new philosophical approaches.
    
    ======
    Insurrectionary anarchism is a revolutionary theory, practice, and tendency within the anarchist movement which emphasises insurrection within anarchist practice It is critical of formal organisations such as labour unions and federations that are based on a political programme and periodic congresses.
    
    ======
    Instead, insurrectionary anarchists advocate informal organisation and small affinity group based organisation.
    
    ======
    Insurrectionary anarchists put value in attack, permanent class conflict and a refusal to negotiate or compromise with class enemies.
    
    ======
    Green anarchism (or eco-anarchism) is a school of thought within anarchism that emphasises environmental issues, with an important precedent in anarcho-naturism and whose main contemporary currents are anarcho-primitivism and social ecology.
    
    ======
    Writing from a green anarchist perspective, John Zerzan attributes the ills of today's social degradation to technology and the birth of agricultural civilization.
    
    ======
    While Layla AbdelRahim argues that "the shift in human consciousness was also a shift in human subsistence strategies, whereby some human animals reinvented their narrative to center murder and predation and thereby institutionalize violence".
    
    ======
    Thus, according to her, civilization was the result of the human development of technologies and grammar for predatory economics.
    
    ======
    Language and literacy, she claims, are some of these technologies.
    
    ======
    Anarcho-pacifism is a tendency that rejects violence in the struggle for social change (see non-violence).
    
    ======
    It developed mostly in the Netherlands, Britain and the United States before and during the Second World War.
    
    ======
    Christian anarchism is a movement in political theology that combines anarchism and Christianity.
    
    ======
    Its main proponents included Leo Tolstoy, Dorothy Day, Ammon Hennacy and Jacques Ellul.
    
    ======
    Religious anarchism refers to a set of related anarchist ideologies that are inspired by the teachings of (organized) religions, but many anarchists have traditionally been skeptical of and opposed to organized religion.
    
    ======
    Many different religions have served as inspiration for religious forms of anarchism, most notably Christianity as Christian anarchists believe that biblical teachings give credence to anarchist philosophy.
    
    ======
    Non-Christian forms of religious anarchism include Buddhist anarchism, Jewish anarchism and most recently Neopaganism.
    
    ======
    Synthesis anarchism is a form of anarchism that tries to join anarchists of different tendencies under the principles of anarchism without adjectives.
    
    ======
    In the 1920s, this form found as its main proponents the anarcho-communists Voline and Sébastien Faure.
    
    ======
    It is the main principle behind the anarchist federations grouped around the contemporary global International of Anarchist Federations.
    
    ======
    Platformism is a tendency within the wider anarchist movement based on the organisational theories in the tradition of Dielo Truda's "Organisational Platform of the General Union of Anarchists (Draft)".
    
    ======
    The document was based on the experiences of Russian anarchists in the 1917 October Revolution, which led eventually to the victory of the Bolsheviks over the anarchists and other groups.
    
    ======
    The "Platform" attempted to address and explain the anarchist movement's failures during the Russian Revolution.
    
    ======
    Post-left anarchy is a recent current in anarchist thought that promotes a critique of anarchism's relationship to traditional left-wing politics.
    
    ======
    Some post-leftists seek to escape the confines of ideology in general also presenting a critique of organisations and morality.
    
    ======
    Influenced by the work of Max Stirner and by the Marxist Situationist International, post-left anarchy is marked by a focus on social insurrection and a rejection of leftist social organisation.
    
    ======
    Post-anarchism is a theoretical move towards a synthesis of classical anarchist theory and poststructuralist thought, drawing from diverse ideas including post-left anarchy, postmodernism, autonomism, postcolonialism and the Situationist International.
    
    ======
    Queer anarchism is a form of socialism which suggests anarchism as a solution to the issues faced by the LGBT community, mainly heteronormativity, homophobia, transphobia and biphobia.
    
    ======
    Anarcho-queer arose during the late 20th century based on the work of Michel Foucault "The History of Sexuality".
    
    ======
    Left-wing market anarchism strongly affirm the classical liberal ideas of self-ownership and free markets while maintaining that taken to their logical conclusions, these ideas support strongly anti-corporatist, anti-hierarchical, pro-labour positions and anti-capitalism in economics and anti-imperialism in foreign policy.
    
    ======
    Anarcho-capitalism advocates the elimination of the state in favour of self-ownership in a free market.
    
    ======
    Anarcho-capitalism developed from radical anti-state libertarianism and individualist anarchism, drawing from Austrian School economics, study of law and economics and public choice theory.
    
    ======
    There is a strong current within anarchism which believes that anarcho-capitalism cannot be considered a part of the anarchist movement due to the fact that anarchism has historically been an anti-capitalist movement and for definitional reasons which see anarchism as incompatible with capitalist forms.
    
    ======
    Anarcho-transhumanism is a recently new branch of anarchism that takes traditional and modern anarchism, typically drawing from anarcho-syndicalism, left-libertarianism or libertarian socialism and combines it with transhumanism and post-humanism.
    
    ======
    It can be described as a "liberal democratic revolution, at its core the idea that people are happiest when they have rational control over their lives.
    
    ======
    Reason, science, and technology provide one kind of control, slowly freeing us from ignorance, toil, pain, disease and limited lifespans (aging)".
    
    ======
    Some anarcho-transhumanists might also follow technogaianism.
    
    ======
    Anarcha-feminism (also called anarchist feminism and anarcho-feminism) combines anarchism with feminism.
    
    ======
    It generally views patriarchy as a manifestation of involuntary coercive hierarchy that should be replaced by decentralised free association.
    
    ======
    Anarcha-feminists believe that the struggle against patriarchy is an essential part of class struggle, and the anarchist struggle against the state.
    
    ======
    In essence, the philosophy sees anarchist struggle as a necessary component of feminist struggle and vice versa.
    
    ======
    Anarcha-feminists espoused to a detailed analysis of patriarchy and claim that oppression has its roots to social norms.
    


```python
# My segmentation (using regular expression)
import re

def sent_tokenize(text):
    sentences = re.split(r"[.!?]", text)
    sentences = [x.strip() for x in sentences]
    return sentences

sent_tokenize_regex = sent_tokenize(data)

for sent in sent_tokenize_regex:
    print('\n======\n' + sent)
```

    
    ======
    Anarchism is an anti-authoritarian political philosophy that advocates self-governed societies based on voluntary, cooperative institutions and the rejection of hierarchies those societies view as unjust
    
    ======
    These institutions are often described as stateless societies, although several authors have defined them more specifically as distinct institutions based on non-hierarchical or free associations
    
    ======
    Anarchism holds the state to be undesirable, unnecessary, and harmful
    
    ======
    Anarchism is often considered a far-left ideology, and much of anarchist economics and anarchist legal philosophy reflect anti-authoritarian interpretations of communism, collectivism, syndicalism, mutualism, or participatory economics
    
    ======
    Anarchism does not offer a fixed body of doctrine from a single particular world view, instead fluxing and flowing as a philosophy
    
    ======
    Many types and traditions of anarchism exist, not all of which are mutually exclusive
    
    ======
    Anarchist schools of thought can differ fundamentally, supporting anything from extreme individualism to complete collectivism
    
    ======
    Strains of anarchism have often been divided into the categories of social and individualist anarchism or similar dual classifications
    
    ======
    The etymological origin of anarchism derives from ancient Greek word "anarkhia"
    
    ======
    "Anarkhia " meant "without a ruler" as it was composed by the prefix "a" (i
    
    ======
    e "without") and the word "arkhos" (i
    
    ======
    e leader or ruler)
    
    ======
    The suffix -ism is used to denote the ideological current that favours anarchism
    
    ======
    The first known use of this word was in 1642
    
    ======
    Various factions within the French Revolution labelled opponents as anarchists although few shared many views of later anarchists
    
    ======
    There would be many revolutionaries of the early nineteenth century who contributed to the anarchist doctrines of the next generation, such as William Godwin and Wilhelm Weitling, but they did not use the word "anarchist" or "anarchism" in describing themselves or their beliefs
    
    ======
    The first political philosopher to call himself an anarchist was Pierre-Joseph Proudhon, marking the formal birth of anarchism in the mid-nineteenth century
    
    ======
    Since the 1890s and beginning in France, the term "libertarianism" has often been used as a synonym for anarchism and its use as a synonym is still common outside the United States
    
    ======
    On the other hand, some use libertarianism to refer to individualistic free market philosophy only, referring to free market anarchism as libertarian anarchism
    
    ======
    Defining anarchism is not an easy task
    
    ======
    There is a lot of talk among scholars and anarchists on the matter and various currents perceive anarchism slightly differently
    
    ======
    Hence, it might be true to say that anarchism is a cluster of political philosophies rejecting hierarchies (including the state and all associated institutions), in favour of a society based on voluntary association, freedom and decentralization
    
    ======
    This definition though has its own shortcomings, as the definition based on etymology (which is simply a negation of a ruler), or based on anti-statism (anarchism is much more than that) or even the anti-authoritarian (which is an "a posteriori" concussion) Major elements of the definition of anarchism include a)the will for a non coercive society b)the rejection of State apparatus, c)belief in human nature, even though it is even harder to define it than anarchism d)a suggestion on how to act to pursue the ideal of anarchy
    
    ======
    During the prehistoric era of mankind, an established authority did not exist; humans were living in anarchistic societies
    
    ======
    It was after the creation of towns and cities that hierarchy was invented and as a reaction, anarchistic ideas espoused
    
    ======
    Most notable examples of anarchism in the ancient world were in China and Greece
    
    ======
    In China philosophical anarchism, meaning peaceful delegitimizing of the state, was delineated by Taoist philosophers (i
    
    ======
    e
    
    ======
    Zhuangzi and Lao Tzu)
    
    ======
    Likewise in Greece, anarchist attitudes were articulated by tragedians and philosophers
    
    ======
    Aeschylus and Sophocles used the myth of Antigone to illustrate the conflict of personal autonomy with the state rules
    
    ======
    Socrates questioned Athenian authorities constantly and insisted to the right of individual freedom of consciousness
    
    ======
    Cynics dismissed human law ("Nomos") and associated authorities while trying to live according to nature ("physis")
    
    ======
    Stoics were supportive of a society based on unofficial and friendly relations among its citizens without the presence of a state
    
    ======
    During the Middle Ages, there was no anarchistic activity except some ascetic religious movements in the Islamic world or in Christian Europe
    
    ======
    This kind of tradition later gave birth to religious anarchism
    
    ======
    In Persia, a Zoroastrian Prophet, Mazdak, was calling for an egalitarian society and the abolition of monarchy
    
    ======
    He soon found himself executed by the King
    
    ======
    In Basra, religious sects preached against the State
    
    ======
    In Europe, various sects developed anti-state and libertarian tendencies
    
    ======
    Those currents were the precursor of religious anarchism in the centuries to come
    
    ======
    It was in Renaissance and along with the spread of reasoning and humanism through Europe, libertarian ideas emerged
    
    ======
    Writers were outlining in their novels ideal societies that were based not on coercion but voluntarism
    
    ======
    Enlightenment further pushed towards anarchism with the optimism for social progress
    
    ======
    The turning point towards anarchism was the French Revolution
    
    ======
    Anarchists per se didn't take part, but the anti-state and federalist sentiments began to take a form, mostly by "enrages" and "sans culottes"
    
    ======
    Some prominent figures of anarchism begun developing the first anarchist currents
    
    ======
    That is the era of classical anarchism that lasted until the end of the Spanish Civil War and was the belle epoque of anarchism
    
    ======
    William Godwin in England espoused to philosophical anarchism, morally delegitimizing the state, Max Stirner thinking paved the way to individualism and Pietr Joseph Proudhon's theory of mutualism, found fertile soil in France
    
    ======
    Michael Bakunin took mutualism and extended it to anarcho-collectivism
    
    ======
    Bakunin's current (Jura Federation) entered the class worker union, International Workingmen's Association (or First International) which was formed in 1864, to unite diverse revolutionary currents
    
    ======
    Due to its links to active workers' movements, the International became a significant organisation
    
    ======
    Karl Marx became a leading figure in the International and a member of its General Council
    
    ======
    Proudhon's followers, the mutualists, opposed Marx's state socialism, advocating political abstentionism and small property holdings
    
    ======
    Bakunin's followers entered a bitter dispute with Karl Marx which ended with the split of Worker movement, that officially took place in the Fifth Congress of IWA in the Hague, 1872
    
    ======
    The major reason lied on fundamentally different approaches on how the workers would emancipate themselves
    
    ======
    Marx was advocating for the creation of a political party, taking part in electoral struggles, whereas Bakunin thought that the whole set of Marx's thinking was very authoritarian
    
    ======
    Bakunin is famous for predicting that if such a party would gain power by Marxist's terms, it will end up to be the new tyrant of workers
    
    ======
    After being expelled from the first international, anarchists formed the St
    
    ======
    Imier International
    
    ======
    Under the spell of Kropotkin, a Russian philosopher and respectful scientist, anarcho-communism overlapped collectivism
    
    ======
    Anarcho-communists, who drew inspiration from Paris Commune, advocated for free federation and distribution of goods according to one needs
    
    ======
    The major argument of anarcho-communism was that Bakunian perspective would lead to antagonism among collectives
    
    ======
    At the turning of the century, anarchism has spread all over the world
    
    ======
    In China, small groups of students imported the humanistic pro-science version of anarcho-communism
    
    ======
    Tokyo was a hotspot for rebellious youth from countries of the far east, pouring into Japanese capital to study
    
    ======
    In Latin America, Sao Paolo was a stronghold and anarchosyndicalism was the most prominent left wing ideology
    
    ======
    During that time, a minority of anarchists embarked into utilizing of violence in order to achieve their political ends
    
    ======
    This kind of strategy is named as propaganda by the deed
    
    ======
    The dismemberment of the French socialist movement into many groups and—following the suppression of the 1871—Paris Commune the execution and exile of many communards to penal colonies favoured individualist political expression and acts
    
    ======
    Even though many anarchists distanced themselves to those terrorist acts, anarchists were persecuted and were given bad fame
    
    ======
    Illegalism, stealing the possessions of the rich, because capitalists were not their rightful owners was another strategy some anarchist adopted during the same years
    
    ======
    Anarchists took part enthusiastically in the Russian revolution
    
    ======
    Anarchists during the revolution had concerns but opted for the revolution than supporting the Whites
    
    ======
    But they met harsh suppression after the Bolshevik regime was stabilized
    
    ======
    Anarchists in central Russia were either imprisoned, driven underground or joined the victorious Bolsheviks; the anarchists from Petrograd and Moscow fled to Ukraine
    
    ======
    Kronstadt rebellion and Machno's struggle in Ukraine were the most notable examples
    
    ======
    After anarchist being crashed in Russia, two new antithetical currents emerged: Platformism and Synthesis anarchism
    
    ======
    Platformists sought to create a coherent group that would push for the revolution while the latter were against anything that would resemble a political party
    
    ======
    The victory of the Bolsheviks in the October Revolution and the resulting Russian Civil War did serious damage to anarchist movements internationally
    
    ======
    Many workers and activists saw Bolshevik success as setting an example and communist parties grew at the expense of anarchism and other socialist movements
    
    ======
    In France and the United States, for example, members of the major syndicalist movements of the General Confederation of Labour and Industrial Workers of the World (IWW) left the organisations and joined the Communist International
    
    ======
    In the Spanish Civil War, anarchist's most glorious moment, anarchists and syndicalists (CNT and FAI) once again allied themselves with various currents of leftists
    
    ======
    Spain had a long anarchist tradition, and thus anarchist played an important role in the Civil War
    
    ======
    In response to the army rebellion, an anarchist-inspired movement of peasants and workers, supported by armed militias, took control of Barcelona and of large areas of rural Spain where they collectivised the land
    
    ======
    USSR provided some limited assistance at the beginning of the civil war, but as Stalin tried to seize control of the Republicans, the result was a bitter fight among communists and anarchists (i
    
    ======
    e
    
    ======
    at a series of events named May Days)
    
    ======
    Despite their heroic effort, they were ultimately defeated, leaving an ultimate question: should the anarchist join or not the Democratic group to fight the fascists
    
    ======
    The first years after World War II, anarchism seemed inexisted, a ghost of itself
    
    ======
    So it was kind of a surprise that the '60s witnessed a revival of anarchism
    
    ======
    Main causes may have been the miserable failure of authoritarian communism and alongside with the tension build by Cold War
    
    ======
    During this era, anarchism was mostly part of other movements critical to State and Capitalism, ie within the Anti-nuclear movementand pacifist movement, New Left, the Greens or the counter-culture
    
    ======
    Anarchism was also associated with the punk rock movement as exemplified by bands such as Crass and the Sex Pistols
    
    ======
    
    
    ======
    Although feminist tendencies have always been a part of the anarchist movement in the form of anarcha-feminism, they returned with vigour during the second wave of feminism in the 1960s
    
    ======
    Around the turn of the 21st century, anarchism grew in popularity and influence as part of the anti-war, anti-capitalist, and anti-globalisation movements
    
    ======
    Anarchists became known for their involvement in protests against the meetings of the World Trade Organization (WTO), Group of Eight (G8) and the World Economic Forum (WEF)
    
    ======
    Some anarchist factions at these protests engaged in rioting, property destruction, and violent confrontations with police
    
    ======
    These actions were precipitated by ad hoc, leaderless, anonymous cadres known as black blocs—other organisational tactics pioneered in this time include security culture, affinity groups and the use of decentralised technologies such as the internet
    
    ======
    A significant event of this period was the confrontations at WTO conference in Seattle in 1999
    
    ======
    Anarchist ideas have been influential in the development of the Zapatista movement in Chiapas, Mexico and the Democratic Federation of Northern Syria (DFNS), more commonly known as Rojava, a "de facto" autonomous region in northern Syria
    
    ======
    Anarchist schools of thought had been generally grouped in two main historical traditions, individualist anarchism and social anarchism, which have some different origins, values and evolution
    
    ======
    The individualist wing of anarchism emphasises negative liberty, i
    
    ======
    e
    
    ======
    opposition to state or social control over the individual, while those in the social wing emphasise positive liberty to achieve one's potential and argue that humans have needs that society ought to fulfil, "recognising equality of entitlement"
    
    ======
    In a chronological and theoretical sense, there are classical—those created throughout the 19th century—and post-classical anarchist schools—those created since the mid-20th century and after
    
    ======
    Beyond the specific factions of anarchist thought is philosophical anarchism, which embodies the theoretical stance that the state lacks moral legitimacy without accepting the imperative of revolution to eliminate it
    
    ======
    A component especially of individualist anarchism philosophical anarchism may accept the existence of a minimal state as unfortunate, and usually temporary, "necessary evil" but argue that citizens do not have a moral obligation to obey the state when its laws conflict with individual autonomy
    
    ======
    One reaction against sectarianism within the anarchist milieu was "anarchism without adjectives", a call for toleration first adopted by Fernando Tarrida del Mármol in 1889 in response to the "bitter debates" of anarchist theory at the time
    
    ======
    In abandoning the hyphenated anarchisms (i
    
    ======
    e
    
    ======
    collectivist-, communist-, mutualist- and individualist-anarchism), it sought to emphasise the anti-authoritarian beliefs common to all anarchist schools of thought
    
    ======
    The various anarchist schools of thought or currents are not distinct entities but intermingle with each other
    
    ======
    Collectivist, Communist and Anarcho-syndicalism are considered a form of social anarchism
    
    ======
    Mutualism and Individualism were the other notable anarchist currents through the 19th and early 20th century
    
    ======
    Social anarchism rejects private property, seeing it as a source of social inequality (while retaining respect for personal property) and emphasises cooperation and mutual aid
    
    ======
    Mutualism began in 18th-century English and French labour movements before taking an anarchist form associated with Pierre-Joseph Proudhon in France and others in the United States
    
    ======
    Proudhon proposed spontaneous order, whereby organisation emerges without central authority, a "positive anarchy" where order arises when everybody does ""what he wishes and only what he wishes"" and where "business transactions alone produce the social order
    
    ======
    " Proudhon distinguished between ideal political possibilities and practical governance
    
    ======
    For this reason, much in contrast to some of his theoretical statements concerning ultimate spontaneous self-governance, Proudhon was heavily involved in French parliamentary politics and allied himself not with anarchist but socialist factions of workers' movements and, in addition to advocating state-protected charters for worker-owned cooperatives, promoted certain nationalisation schemes during his life of public service
    
    ======
    Mutualist anarchism is concerned with reciprocity, free association, voluntary contract, federation, and credit and currency reform
    
    ======
    According to the American mutualist William Batchelder Greene, each worker in the mutualist system would receive ""just and exact pay for his work; services equivalent in cost being exchangeable for services equivalent in cost, without profit or discount""
    
    ======
    Mutualism has been retrospectively characterised as ideologically situated between individualist and collectivist forms of anarchism
    
    ======
    Proudhon first characterised his goal as a ""third form of society, the synthesis of communism and property [which] we call LIBERTY""
    
    ======
    Collectivist anarchism, also referred to as revolutionary socialism or a form of such, is a revolutionary form of anarchism, commonly associated with Mikhail Bakunin and Johann Most
    
    ======
    At the epicentre of collectivist anarchism lies the belief in the potential of humankind for goodness and solidarity, which will flourish when oppressive governments are abolished
    
    ======
    Collectivist anarchists oppose all private ownership of the means of production, instead advocating that ownership be collectivised
    
    ======
    This was to be achieved through violent revolution, first starting with a small cohesive group through acts of violence, or propaganda by the deed, which would inspire the workers as a whole to revolt and forcibly collectivise the means of production
    
    ======
    However, collectivisation was not to be extended to the distribution of income as workers would be paid according to time worked, rather than receiving goods being distributed "according to need" as in anarcho-communism
    
    ======
    This position was criticised by anarchist communists as effectively "uphold[ing] the wages system"
    
    ======
    Collectivist anarchism arose contemporaneously with Marxism, but opposed the Marxist dictatorship of the proletariat despite the stated Marxist goal of a collectivist stateless society
    
    ======
    Anarchist, communist and collectivist ideas are not mutually exclusive—although the collectivist anarchists advocated compensation for labour, some held out the possibility of a post-revolutionary transition to a communist system of distribution according to need
    
    ======
    Anarcho-communism (also known as anarchist-communism, libertarian communism and occasionally as free communism) is a theory of anarchism that advocates abolition of the state, markets, money, private property (while retaining respect for personal property) and capitalism in favour of common ownership of the means of production, direct democracy and a horizontal network of voluntary associations and workers' councils with production and consumption based on the guiding principle: "From each according to his ability, to each according to his need"
    
    ======
    Some forms of anarchist communism such as insurrectionary anarchism are strongly influenced by egoism and radical individualism, believing anarcho-communism is the best social system for the realisation of individual freedom
    
    ======
    Most anarcho-communists view anarcho-communism as a way of reconciling the opposition between the individual and society
    
    ======
    Anarcho-communism developed out of radical socialist currents after the French Revolution but was first formulated as such in the Italian section of the First International
    
    ======
    The theoretical work of Peter Kropotkin took importance later as it expanded and developed pro-organisationalist and insurrectionary anti-organisationalist sections
    
    ======
    To date, the best known examples of an anarchist communist society (i
    
    ======
    e
    
    ======
    established around the ideas as they exist today and achieving worldwide attention and knowledge in the historical canon), are the anarchist territories during the Spanish Revolution and the Free Territory during the Russian Revolution
    
    ======
    Through the efforts and influence of the Spanish anarchists during the Spanish Revolution within the Spanish Civil War, starting in 1936 anarchist communism existed in most of Aragon, parts of the Levante and Andalusia as well as in the stronghold of anarchist Catalonia
    
    ======
    It was crushed by the combined forces of the Franco’s Nationalists, Hitler, and Mussolini, as well as repression by the Communist Party of Spain (backed by the Soviet Union) and economic and armaments blockades from the capitalist countries and the Spanish Republic itself
    
    ======
    Anarcho-syndicalism is a branch of anarchism that focuses on the labour movement
    
    ======
    Anarcho-syndicalists view labour unions as a potential force for revolutionary social change, replacing capitalism and the state with a new society democratically self-managed by workers
    
    ======
    The basic principles of anarcho-syndicalism are workers' solidarity, direct action and workers' self-management
    
    ======
    Anarcho-syndicalists believe that only direct action—that is, action concentrated on directly attaining a goal as opposed to indirect action, such as electing a representative to a government position—will allow workers to liberate themselves
    
    ======
    Moreover, anarcho-syndicalists believe that workers' organisations (the organisations that struggle against the wage system, which in anarcho-syndicalist theory will eventually form the basis of a new society) should be self-managing
    
    ======
    They should not have bosses or "business agents"—rather, the workers should be able to make all the decisions that affect them themselves
    
    ======
    Rudolf Rocker was one of the most popular voices in the anarcho-syndicalist movement
    
    ======
    He outlined a view of the origins of the movement, what it sought and why it was important to the future of labour in his 1938 pamphlet "Anarcho-Syndicalism"
    
    ======
    The International Workers Association is an international anarcho-syndicalist federation of various labour unions from different countries
    
    ======
    The Spanish CNT played and still plays a major role in the Spanish labour movement
    
    ======
    It was also an important force in the Spanish Civil War
    
    ======
    Individualist anarchism refers to several traditions of thought within the anarchist movement that emphasise the individual and their will over any kinds of external determinants such as groups, society, traditions and ideological systems
    
    ======
    Individualist anarchism is not a single philosophy, but it instead refers to a group of individualistic philosophies that sometimes are in conflict
    
    ======
    In 1793, William Godwin, who has often been cited as the first anarchist, wrote "Political Justice", which some consider the first expression of anarchism
    
    ======
    Godwin was a philosophical anarchist and from a rationalist and utilitarian basis opposed revolutionary action and saw a minimal state as a present "necessary evil" that would become increasingly irrelevant and powerless by the gradual spread of knowledge
    
    ======
    Godwin advocated individualism, proposing that all cooperation in labour be eliminated on the premise that this would be most conducive with the general good
    
    ======
    An influential form of individualist anarchism, called "egoism", or egoist anarchism, was expounded by one of the earliest and best-known proponents of individualist anarchism, the German Max Stirner
    
    ======
    Stirner's "The Ego and Its Own", published in 1844, is a founding text of the philosophy
    
    ======
    According to Stirner, the only limitation on the rights of individuals is their power to obtain what they desire without regard for God, state, or morality
    
    ======
    To Stirner, rights were "spooks" in the mind and he held that society does not exist, but "the individuals are its reality"
    
    ======
    Stirner advocated self-assertion and foresaw unions of egoists, non-systematic associations continually renewed by all parties' support through an act of will, which Stirner proposed as a form of organisation in place of the state
    
    ======
    Egoist anarchists argue that egoism will foster genuine and spontaneous union between individuals
    
    ======
    "Egoism" has inspired many interpretations of Stirner's philosophy
    
    ======
    It was re-discovered and promoted by German philosophical anarchist and homosexual activist John Henry Mackay
    
    ======
    Josiah Warren was a pioneer American anarcho-individualist, who drew inspiration from Proudhon
    
    ======
    Henry David Thoreau (1817–1862) was an important early influence in individualist anarchist thought in the United States and Europe
    
    ======
    Thoreau was an American author, poet, naturalist, tax resister, development critic, surveyor, historian, philosopher and leading transcendentalist
    
    ======
    He is best known for his books "Walden", a reflection upon simple living in natural surroundings, as well as his essay, "Civil Disobedience", an argument for individual resistance to civil government in moral opposition to an unjust state
    
    ======
    Benjamin Tucker later fused Stirner's egoism with the economics of Warren and Proudhon in his eclectic influential publication "Liberty"
    
    ======
    From these early influences, individualist anarchism in different countries attracted a small yet diverse following of Bohemian artists and intellectuals, free love and birth control advocates (see anarchism and issues related to love and sex), individualist naturists and nudists (see anarcho-naturism), freethought and anti-clerical activists as well as young anarchist outlaws in what became known as illegalism and individual reclamation (see European individualist anarchism and individualist anarchism in France)
    
    ======
    These authors and activists included Oscar Wilde, Emile Armand, Han Ryner, Henri Zisly, Renzo Novatore, Miguel Gimenez Igualada, Adolf Brand and Lev Chernyi among others
    
    ======
    Anarchist principles undergird contemporary radical social movements of the left
    
    ======
    Interest in the anarchist movement developed alongside momentum in the anti-globalization movement, whose leading activist networks were anarchist in orientation
    
    ======
    As the movement shaped 21st century radicalism, wider embrace of anarchist principles signaled a revival of interest
    
    ======
    Contemporary news coverage, which emphasizes black bloc demonstrations, has reinforced anarchism's historical association with chaos and violence, though its publicity has also led more scholars to engage with the anarchist movement
    
    ======
    Anarchism continues to generate many philosophies and movements, at times eclectic, drawing upon various sources and syncretic, combining disparate concepts to create new philosophical approaches
    
    ======
    Insurrectionary anarchism is a revolutionary theory, practice, and tendency within the anarchist movement which emphasises insurrection within anarchist practice It is critical of formal organisations such as labour unions and federations that are based on a political programme and periodic congresses
    
    ======
    Instead, insurrectionary anarchists advocate informal organisation and small affinity group based organisation
    
    ======
    Insurrectionary anarchists put value in attack, permanent class conflict and a refusal to negotiate or compromise with class enemies
    
    ======
    Green anarchism (or eco-anarchism) is a school of thought within anarchism that emphasises environmental issues, with an important precedent in anarcho-naturism and whose main contemporary currents are anarcho-primitivism and social ecology
    
    ======
    Writing from a green anarchist perspective, John Zerzan attributes the ills of today's social degradation to technology and the birth of agricultural civilization
    
    ======
    While Layla AbdelRahim argues that "the shift in human consciousness was also a shift in human subsistence strategies, whereby some human animals reinvented their narrative to center murder and predation and thereby institutionalize violence"
    
    ======
    Thus, according to her, civilization was the result of the human development of technologies and grammar for predatory economics
    
    ======
    Language and literacy, she claims, are some of these technologies
    
    ======
    Anarcho-pacifism is a tendency that rejects violence in the struggle for social change (see non-violence)
    
    ======
    It developed mostly in the Netherlands, Britain and the United States before and during the Second World War
    
    ======
    Christian anarchism is a movement in political theology that combines anarchism and Christianity
    
    ======
    Its main proponents included Leo Tolstoy, Dorothy Day, Ammon Hennacy and Jacques Ellul
    
    ======
    Religious anarchism refers to a set of related anarchist ideologies that are inspired by the teachings of (organized) religions, but many anarchists have traditionally been skeptical of and opposed to organized religion
    
    ======
    Many different religions have served as inspiration for religious forms of anarchism, most notably Christianity as Christian anarchists believe that biblical teachings give credence to anarchist philosophy
    
    ======
    Non-Christian forms of religious anarchism include Buddhist anarchism, Jewish anarchism and most recently Neopaganism
    
    ======
    Synthesis anarchism is a form of anarchism that tries to join anarchists of different tendencies under the principles of anarchism without adjectives
    
    ======
    In the 1920s, this form found as its main proponents the anarcho-communists Voline and Sébastien Faure
    
    ======
    It is the main principle behind the anarchist federations grouped around the contemporary global International of Anarchist Federations
    
    ======
    Platformism is a tendency within the wider anarchist movement based on the organisational theories in the tradition of Dielo Truda's "Organisational Platform of the General Union of Anarchists (Draft)"
    
    ======
    The document was based on the experiences of Russian anarchists in the 1917 October Revolution, which led eventually to the victory of the Bolsheviks over the anarchists and other groups
    
    ======
    The "Platform" attempted to address and explain the anarchist movement's failures during the Russian Revolution
    
    ======
    Post-left anarchy is a recent current in anarchist thought that promotes a critique of anarchism's relationship to traditional left-wing politics
    
    ======
    Some post-leftists seek to escape the confines of ideology in general also presenting a critique of organisations and morality
    
    ======
    Influenced by the work of Max Stirner and by the Marxist Situationist International, post-left anarchy is marked by a focus on social insurrection and a rejection of leftist social organisation
    
    ======
    Post-anarchism is a theoretical move towards a synthesis of classical anarchist theory and poststructuralist thought, drawing from diverse ideas including post-left anarchy, postmodernism, autonomism, postcolonialism and the Situationist International
    
    ======
    Queer anarchism is a form of socialism which suggests anarchism as a solution to the issues faced by the LGBT community, mainly heteronormativity, homophobia, transphobia and biphobia
    
    ======
    Anarcho-queer arose during the late 20th century based on the work of Michel Foucault "The History of Sexuality"
    
    ======
    Left-wing market anarchism strongly affirm the classical liberal ideas of self-ownership and free markets while maintaining that taken to their logical conclusions, these ideas support strongly anti-corporatist, anti-hierarchical, pro-labour positions and anti-capitalism in economics and anti-imperialism in foreign policy
    
    ======
    Anarcho-capitalism advocates the elimination of the state in favour of self-ownership in a free market
    
    ======
    Anarcho-capitalism developed from radical anti-state libertarianism and individualist anarchism, drawing from Austrian School economics, study of law and economics and public choice theory
    
    ======
    There is a strong current within anarchism which believes that anarcho-capitalism cannot be considered a part of the anarchist movement due to the fact that anarchism has historically been an anti-capitalist movement and for definitional reasons which see anarchism as incompatible with capitalist forms
    
    ======
    Anarcho-transhumanism is a recently new branch of anarchism that takes traditional and modern anarchism, typically drawing from anarcho-syndicalism, left-libertarianism or libertarian socialism and combines it with transhumanism and post-humanism
    
    ======
    It can be described as a "liberal democratic revolution, at its core the idea that people are happiest when they have rational control over their lives
    
    ======
    Reason, science, and technology provide one kind of control, slowly freeing us from ignorance, toil, pain, disease and limited lifespans (aging)"
    
    ======
    Some anarcho-transhumanists might also follow technogaianism
    
    ======
    Anarcha-feminism (also called anarchist feminism and anarcho-feminism) combines anarchism with feminism
    
    ======
    It generally views patriarchy as a manifestation of involuntary coercive hierarchy that should be replaced by decentralised free association
    
    ======
    Anarcha-feminists believe that the struggle against patriarchy is an essential part of class struggle, and the anarchist struggle against the state
    
    ======
    In essence, the philosophy sees anarchist struggle as a necessary component of feminist struggle and vice versa
    
    ======
    Anarcha-feminists espoused to a detailed analysis of patriarchy and claim that oppression has its roots to social norms
    
    ======
    
    
