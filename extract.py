import urllib
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
from collections import Counter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("art", help="Name of the article", type=str)
args = parser.parse_args()

article_url = "https://en.wikipedia.org/wiki/{0}".format(args.art)
resource = urllib.urlopen(article_url)
html = resource.read()

soup = BeautifulSoup(html)
html = soup.find("div", {"class":"reflist columns references-column-width"})
refs = html.findAll("a",{"class" : "external text"})

domains = []
for ref in refs:
    domains.append(urlparse(ref["href"])[1])

print "# Article: {0}".format(article_url)

counted = Counter(domains)
for key, value in counted.iteritems():
    print "{0} {1}".format(key, value)
