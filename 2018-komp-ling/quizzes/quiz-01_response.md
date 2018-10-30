Quiz 1 Answers - Anastasia Nikiforova

1. a, b, d (works much better on Asian languages than on European ones)

2. sed 's/([A-Za-z])/([A-Za-z])/\1\s/\s\2\g'

3. Downsides of machine learning techniques compared to rule-based approaches:
	* Not intuitive for many people, a good math foundation is needed (or at least understanding of different algorithms and OOB-tools or libraries).
	* Large training data needed for feeding the algorithm. Difficilties finding/creating a thoroughly labeled gold standard.
	* Chance of over- or underfitting the algorithm. A deep understanding of algorithms is needed to avoid that.
	* Usually, machine learning algorithms have to be supplemented with rules concerning difficult cases.
	* There will always be an error rate (even if it will be very small).

4. "Не будет ли монеты квас купить" "Небу дет лимон е тыква скупить"

5. Problems for sentence segmentation - [.!?] are not always the enf of the sentence.
	a) <и т.д. и т.п.>, <И.И. Иванов>, <С. Петербург>
	b) <"И что?" - спросил он.>, <Неожиданное бах! раздалось из кухни: кот разбил вазу>
	c) <"Привет как дела что делаешь"> (usually the sign of low literacy, or someone being in a rush)
	d) <"Вылетаю завтра.самолет в 10 утра."> (again - low literacy or being in a hurry. If the second sentence starts with a lowercase, that could be impossible to parse without a special rule for that)
