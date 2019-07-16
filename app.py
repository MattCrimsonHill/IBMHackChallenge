from flask import Flask, render_template, request
from run import bashC

app = Flask(__name__)

@app.route('/', host="ibmappendly.herokuapp.com")
def student():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'], host="ibmappendly.herokuapp.com")
def result():
   if request.method == 'POST':
      topic = request.form['Name']
      problem = request.form['Name2']
      randomFile = bashC(topic, problem)
      text = open(randomFile, 'r+')
      output = text.read()
      text.close()
      return render_template("index.html", output = output)

if __name__ == '__main__':
   app.run(debug=True, host="ibmappendly.herokuapp.com")