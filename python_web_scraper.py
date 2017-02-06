import os
import urllib2
from flask import Flask
from bs4 import BeautifulSoup
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def root():
	return "Nothing Here"

@app.route('/html/<string:site>')
def whole_html(site):
	url = "https://" + site
	html = urllib2.urlopen(url).read()
	return html

@app.route('/text/<string:site>')
def whole_text(site):
	url = "https://" + site
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	for script in soup(["script", "style", "span"]):
		script.extract()    # rip it out

	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk.lower() for chunk in chunks if chunk)

	return text


@app.route('/searchhtml/<string:word>/<string:site>')
def searchhtml(word, site):
	url = "https://" + site
	html = urllib2.urlopen(url).read()
	html2 = html.decode('latin-1')

	return jsonify (
		Word=word,
		count = html2.count(word.lower())
	)


@app.route('/searchtext/<string:word>/<string:site>')
def searchtext(word, site):
	url = "https://" + site
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	for script in soup(["script", "style"]):
		script.extract()    

	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk.lower() for chunk in chunks if chunk)

	return jsonify(
		Count = text.count(word.lower()),
		Word = word	
	)


if __name__=='__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)


