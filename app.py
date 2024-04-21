from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def predict():
    if request.method == 'POST':
        ht = request.form['height']
        print(ht)
        model = pickle.load(open('model.pkl', 'rb'))
        weight = model.predict([[float(ht)]])
        print(weight[0])
        rounded_weight = round(weight[0], 2)
        return render_template('prediction.html', prediction=rounded_weight)
    else:
        return "Method Not Allowed"

if __name__ == '__main__':
    app.run()