# easyscrape-zazzlesuggest
Scrape Zazzle search suggestions with Python

<img src="https://github.com/amazingjoe/amazingjoe.github.io/blob/main/imgs/Easyscrape.png" width="50%"/>

## Instructions

1. Install:

```
pip install easyscrape-zazzlesuggest
```

2. Get Zazzle Suggestions for a Search Term:

```python
from easyscrape_zazzlesuggest import querysuggestions as ZS

# Request suggestions for a search term
ZSResults = ZS.query("Monty")
ZSResults

['monty mens tshirts', 'monty mens tops', 'monty mens clothing', 'monty mens fashion', 'monty clothing', 'monty']
```

3. ZS query returns a list of strings with the results.