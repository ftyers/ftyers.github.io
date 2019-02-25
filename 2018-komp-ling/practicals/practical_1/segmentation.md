**Pragmatic Segmenter**  - сегментатор, работающий на правилах. Мне было трудно заставить его наконец работать, но когда у меня получилось, я была приятно удивлена. 
Он правильно нашел ВСЕ предложения, но тут есть нюансы, о которых необходимо упомянуть. Например:
* _Anarchist historian George Woodcock reports: "The annual Congress of the International had not taken place in 1870 owing to the outbreak of the Paris Commune, and in 1871 the General Council called only a special conference in London. One delegate was able to attend from Spain and none from Italy, while a technical excuse – that they had split away from the Fédération Romande – was used to avoid inviting Bakunin's Swiss supporters. Thus only a tiny minority of anarchists was present, and the General Council's resolutions passed almost unanimously. Most of them were clearly directed against Bakunin and his followers"._
  Сегментатор не размечал предложения, находящиеся внутри цитаты, как отдельные.  Насколько я понимаю, вопрос о том, как стоит сегментатору поступать в таких ситуациях, является открытым, но я для себя решила, что такое поведение - верное.
  Также он отлично справился с сокращениями, аббревиатурами и другими уловками пунктуации. Пример: 
* _In Latin America in particular, "anarchists quickly became active in organising craft and industrial workers throughout South and Central America, and until the early 1920s most of the trade unions in Mexico, Brazil, Peru, Chile, and Argentina were anarcho-syndicalist in general outlook; the prestige of the Spanish C.N.T. as a revolutionary organisation was undoubtedly to a great extent responsible for this situation. The largest and most militant of these organisations was the Federación Obrera Regional Argentina [... it grew quickly to a membership of nearly a quarter of a million, which dwarfed the rival socialdemocratic unions"._
  Еще пример:
* _The word "" is composed from the word "anarchy" and the suffix -ism, themselves derived respectively from the Greek , i.e. "anarchy" (from , "anarchos", meaning "one without rulers"; from the privative prefix ἀν- ("an-", i.e. "without") and , "archos", i.e. "leader", "ruler"; (cf. "archon" or , "arkhē", i.e. "authority", "sovereignty", "realm", "magistracy")) and the suffix or ("-ismos", "-isma", from the verbal infinitive suffix , "-izein")._

Результат: 100%


**Nltk punkt** - я использовала уже натренированный сегментатор для английского. К сожалению, он ошибся везде, где можно было это сделать. Разбивает предложения внутри цитат, не справляется с сокращениями и аббревиатурами. 
Насчитал мне на шесть предложений больше, чем было. На зато более прост в использовании, чем Pragmatic Segmenter, ха-ха ;D 

Вот его версии тех предложений, что я уже приводила выше:
* _In Latin America in particular, "anarchists quickly became active in organising craft and industrial workers throughout South and Central America, and until the early 1920s most of the trade unions in Mexico, Brazil, Peru, Chile, and Argentina were anarcho-syndicalist in general outlook; the prestige of the Spanish C.N.T._

_as a revolutionary organisation was undoubtedly to a great extent responsible for this situation._

* _The word "" is composed from the word "anarchy" and the suffix -ism, themselves derived respectively from the Greek , i.e._
  _"anarchy" (from , "anarchos", meaning "one without rulers"; from the privative prefix ἀν- ("an-", i.e._
  _"without") and , "archos", i.e._
  _"leader", "ruler"; (cf._
  _"archon" or , "arkhē", i.e._
  _"authority", "sovereignty", "realm", "magistracy")) and the suffix or ("-ismos", "-isma", from the verbal infinitive suffix , "-izein")._

* _Anarchist historian George Woodcock reports: "The annual Congress of the International had not taken place in 1870 owing to the outbreak of the Paris Commune, and in 1871 the General Council called only a special conference in London._

_One delegate was able to attend from Spain and none from Italy, while a technical excuse – that they had split away from the Fédération Romande – was used to avoid inviting Bakunin's Swiss supporters._

_Thus only a tiny minority of anarchists was present, and the General Council's resolutions passed almost unanimously._
_Most of them were clearly directed against Bakunin and his followers"._

Результат: 84%