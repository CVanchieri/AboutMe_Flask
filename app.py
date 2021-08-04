### necessary imports ### 
from flask import Flask, render_template, request, jsonify, Response
from assistant import check
import os
from functools import wraps

# FalconSQL Login https://api.plot.ly/

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)
### local development ###
# app.config['TESTING'] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['STATIC_AUTO_RELOAD'] = True
# app.run(debug=True)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    USERNAME_AUTH = os.getenv("USERNAME_AUTH")
    PASSWORD_AUTH = os.getenv("PASSWORD_AUTH")
    return username == USERNAME_AUTH and password == PASSWORD_AUTH

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


### home page ###
@app.route('/')
def root():
    return render_template('home.html')


################################
@app.route("/chat_home", methods=['GET', 'POST'])
def chat_home():
    # if request.method == 'POST':
    #     user_query = request.form['user_query']
    #     print(user_query)
    #     user_query = user_query.strip()
    #     result = check(user_query)
    #     return render_template('index.html', response=result, user_query=user_query)
    return render_template('chatbot.html')


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    user_query = request.json
    #print(user_query)
    user_query = user_query['name']
    result = check(user_query)
    #print(result)
    return jsonify(result)