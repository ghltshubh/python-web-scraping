# python-web-scraping
A simple python-flask API for searching a given word in a given website.

This simple API has two inputs: a random word and a random website.
The python2 script will then send a HTTP request and will search for the given word in the website, the output is a simple JSON response with the word specified and it's number of occurences.

Keep in mind that the application also returns the whole html or the whole text in the scpecified webpage.

<b>Deploying the application in Heroku Platform:</b>

- Install Heroku CLI tools (check the syntax for your system):

*sudo apt-get install heroku* 

- Sign Up in Heroku website, after you can Sign In via CLI:

*heroku login*

- Create a new folder in your computer to host the project:

*mkdir python-web-scraping*
*cd python-web-scraping*

- create a Vitual env and activate it:

*virtualenv venv*
*source venv/bin/activate*

- Install bs4 and flask:

*pip install bs4*
*pip install flask*

- Copy the python file (python_web_scraper.py) inside the folder you just created.

- In order to install all dependencies in Heroku platform, we need to create a file with all necessary modules:

*pip freeze > requirements.txt*

- Create a file named "Procfile", so Heroku knows wich command to execute. 

*echo "web: python python_web_scraper.py" > Procfile*

- Now we can initialize a Git repository:

*git init*

- create a file named .gitignore , inside this file put the following lines:

*.pyc 
venv 

This way, GIT will ignore some files that are not necessary to commit.

- Commit and deploy the application:

*git add .
git commit -m "first deploy"
heroku apps:create python-web-scraper
*
<br></br>

<b>Usage</b>:
<br></br>
Here we'll use the word "search" in URL argument
<br></br>

- return only text (replace [site]):
  python-web-scraper.herokuapp.com/html/[site]
  
  example: python-web-scraper.herokuapp.com/html/www.google.com

- return html:
  python-web-scraper.herokuapp.com/text/[site]
  
  example: python-web-scraper.herokuapp.com/text/www.google.com 
  
  
- return the number of occurences of [word] within text:
  python-web-scraper.herokuapp.com/searchhtml/[word]/[site]
  
  example: python-web-scraper.herokuapp.com/searchhtml/search/www.google.com


- return the number of occurences of [word] within html:
 python-web-scraper.herokuapp.com/searchtext/[word]/[site]
 
 example: python-web-scraper.herokuapp.com/searchtext/search/www.google.com
 

The website has to be in this form: "www.google.com", don't use "http" or "https". You can use it either in web browser or with CLI <em>curl</em> command.


