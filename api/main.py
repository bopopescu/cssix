import webapp2
import jinja2
from google.appengine.api import urlfetch
import json 
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    

class MainPage(webapp2.RequestHandler):
    def get(self):  # for a get request
            trivia_endpoint_url = "https://opentdb.com/api.php?amount=1&category=10&difficulty=easy&type=multiple"
            trivia_response= urlfetch.fetch(trivia_endpoint_url).content
            trivia_as_json = json.loads(trivia_response)
            first_result = trivia_as_json['results'][0]
            trivia_question = first_result['question']
            correct_answer_dict = {
                'text': first_result['correct_answer'],
                'is_correct': True
            }
            
            incorrect_answers = first_result['incorrect_answers']
            
            #create an array of all 4 answer options
            all_answer_options = [correct_answer_dict]

            for answer in incorrect_answers: 
                answer_dict = {
                    'text': answer,
                    'is_correct': False
                }
                all_answer_options.append(answer_dict)
            
            
            random.shuffle(all_answer_options)
    
            the_variable_dict = {
                "question": trivia_question,
                "answers": all_answer_options,
            }
            
            game_template = the_jinja_env.get_template('templates/game.html')
            
        
        
            self.response.write(game_template.render(the_variable_dict))
        
        
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
