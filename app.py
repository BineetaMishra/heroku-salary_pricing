from flask import Flask, render_template, request

app= Flask(__name__)
# loading the model
import joblib
model= joblib.load('hiring_model.pkl')

@app.route("/")
def welcome():
    return render_template('base.html')


@app.route('/predict' , methods = ['POST'])
def predict():

    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('Interview_score')

    prediction = model.predict([[int(exp) , int(score) , int(interview_score)]])

    output = round(prediction[0] , 2)

    return render_template('base.html' , prediction_text = f"Employee Salary will be $ {output}")

if __name__=='__main__':
    app.run(debug=True)

