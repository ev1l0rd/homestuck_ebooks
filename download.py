import requests

# HTML Stripping code from https://stackoverflow.com/q/11061058/4666756
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


print('Downloading the full homestuck text using requests from readmspa...')
r = requests.get('http://readmspa.org/search/search=6.html')
print('Removing all HTML tags from the file...')
r = strip_tags(r.text)
print('Saving to file')
with open('homestuck.txt', 'w') as outfile:
    outfile.write(r)
print('Success!')
