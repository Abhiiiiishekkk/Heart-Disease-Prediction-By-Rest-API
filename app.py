from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model2.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_heartdisease():
    age = float(request.form.get('age'))
    chest_pain = int(request.form.get('chest_pain'))
    cholestrol = int(request.form.get('cholesterol'))
    thalach = int(request.form.get('thalach'))
    thalassemia = int(request.form.get('thalassemia'))
    ca = int(request.form.get('ca'))
    slope = int(request.form.get('slope'))

    # prediction
    result = model.predict(np.array([age,chest_pain,cholestrol,thalach,thalassemia,ca,slope]).reshape(1,7))
    print(result)
    fin_result = float(round(result[0],2))

    if fin_result == 1:
        fin_result = 'Chances are High'
    else:
        fin_result = 'Chances are Low'

    
    return render_template('index.html',fin_result=fin_result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)