from flask import Flask, render_template, request
from run import bashC

app = Flask(__name__)

@app.route('/', host="https://ibmappendly.herokuapp.com")
def student():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'], host="ibmappendly.herokuapp.com")
def result():
   if request.method == 'POST':
      topic = request.form['Name']
      problem = request.form['Name2']
      bashC(topic, problem)
      text = open('output.txt', 'r+')
      output = text.read()
      text.close()
      return render_template("index.html", output = output)

if __name__ == '__main__':
   app.run(debug=True)