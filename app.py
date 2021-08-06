### necessary imports ### 
from flask import Flask, render_template, request, jsonify
from assistant import check

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)
### local development ###
# app.config['TESTING'] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['STATIC_AUTO_RELOAD'] = True
# app.run(debug=True)

################################
@app.route("/", methods=['GET', 'POST'])
def chat_home():

    return render_template('chatbot.html')


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    user_query = request.json

    user_query = user_query['name']
    result = check(user_query)

    return jsonify(result)