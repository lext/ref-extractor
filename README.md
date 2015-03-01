# ref-extractor
Reference extractor from Wikipedia pages. The script builds a frequency table of domains: 10 references from yahoo, 5 from BBC etc.

## Requirements:

* Python 2.7
* BeautifulSoup


## Example of the use of the script

```
python2 extract.py "2014-15_Russian_financial_crisis"

```

By the default, the script prints frequency table on the screen. You can use the output redirect (Unix-like systems):

```
python2 extract.py "2014-15_Russian_financial_crisis" > crysis.txt

```
