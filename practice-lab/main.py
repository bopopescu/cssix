import webapp2
import jinja2
from google.appengine.api import urlfetch
import json 
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class MainPage(webapp2.RequestHandler):
    def get(self):  # for a get request
            trivia_endpoint_url = "https://opentdb.com/api.php?amount=1&category=10&difficulty=easy&type=multiple"
            user-first-ln= urlfetch.fetch(trivia_endpoint_url).content
            trivia_as_json = json.loads('user-first-ln')
            first_result =
            }