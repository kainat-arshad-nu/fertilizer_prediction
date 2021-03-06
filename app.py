from flask import Flask, request, render_template
import pickle
from flask_cors import CORS

app = Flask("__name__")
CORS(app)


q = ""

@app.route("/")
def loadPage():
	return render_template('index.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    
    inputQuery1 = int(request.form['n'])
    inputQuery2 = int(request.form['p'])
    inputQuery3 = int(request.form['k'])
    inputQuery4 = float(request.form['temp'])
    inputQuery5 = float(request.form['hum'])
    inputQuery6 = float(request.form['moisture'])

    model = pickle.load(open("model.sav", "rb"))
    
    
    data = [[inputQuery4, inputQuery5, inputQuery6, inputQuery1, inputQuery3, inputQuery2]]
    
    single = model.predict(data)
    
        
    return render_template('index.html', output1=single[0], query1 = inputQuery1, query2 = inputQuery2,query3 = inputQuery3 ,query4 = inputQuery4, query5 = inputQuery5, query6 = inputQuery6)

@app.route("/api/predict/", methods=['POST'])
def testAPI():
    inputQuery1 = int(request.form['n'])
    inputQuery2 = int(request.form['p'])
    inputQuery3 = int(request.form['k'])
    inputQuery4 = float(request.form['temp'])
    inputQuery5 = float(request.form['hum'])
    inputQuery6 = float(request.form['moisture'])

    model = pickle.load(open("model.sav", "rb"))
    
    
    data = [[inputQuery4, inputQuery5, inputQuery6, inputQuery1, inputQuery3, inputQuery2]]

    single = model.predict(data)
        
    return single[0]

if __name__ == "__main__":
    app.run()
