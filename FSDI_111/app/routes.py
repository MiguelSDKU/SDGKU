from flask import Flask                   #from the flask module import the flask class

app = Flask(__name__)                     #Create an instance of the Flask class (app is now an object)

@app.get("/")                             #Flask decorator to map routes to view functions 
def get_home():                           #Flask view function
  me = {                                  #Python dictionarty (key-value pairs)
    "first_name": "Rafael",               
    "last_name": "GPL",
    "hobbies": "DIY stuff",
    "is_online": True
  }
  return me                               #When you return a dict in flask it is converted to json! 