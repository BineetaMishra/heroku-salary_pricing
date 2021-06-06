from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def welcome():
    return render_template('base.html')

@app.route("/Contact")
def Contact():
    return'Contact_Us!'

@app.route("/FeedBack")
def FeedBack():
    return'Give us some FeedBack!'

@app.route("/help")
def help():
    return'Let us know how we can help!'

@app.route("/home")
def home():
    return'Welcome to our Data Science World!'

@app.route("/predict", methods=['post'])
def predict():
    return 'Welcome to our Page!'


app.run(debug=True)