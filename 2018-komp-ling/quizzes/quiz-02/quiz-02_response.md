<p>1.<br>
<img src='s_to_is.png'></p>
<p>2. When "'s" is used in posessive case (<i>Julia's response</i>).<br>
I can incorporate context morphological rule that states that "'s" should never
correspond to "is" when followed by a noun, because phrases like <i>"Julia is dancing",
"Julia is a cat", "Julia is (not so) smart"</i>, when it's followed by verb, article, adjective or negation,
are okay.</p>
<p>3. b, c.</p>
<p>4. b, d.</p>
<p>5.<br>
<img src='pluralization.png'></p>
Python implementation <b>(2-5_pl.py)</b>:

```python 
import sys
import re

soft = ['ch', 'sh', 'tz', 's', 'x']

for line in sys.stdin.readlines():
	if re.search(str([i for i in soft])+'<PL>', line):
		line = line.replace('<PL>','es')
		print(line)
	else:
		line = line.replace('<PL>','s')
		print(line)
```