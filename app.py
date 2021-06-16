from flask import Flask,render_template,request,redirect,url_for
import ktrain
predictor = ktrain.load_predictor('distilbert')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    string="Enter any Sentence"
    if(request.method == 'POST'):
        string = request.form['Sentence']
        string = predictor.predict([string])
        if string == 'neg': string = 'Negative'
        else: string = 'Positive'
    return redirect(url_for('result',output=string))

@app.route('/result/<output>')
def result(output):
    return render_template('Predicted.html',Predicted=output)

if __name__ == '__main__':
    app.run(debug=True)

