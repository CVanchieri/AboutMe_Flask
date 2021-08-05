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