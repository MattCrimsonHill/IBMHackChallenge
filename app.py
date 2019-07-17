from flask import Flask, render_template, request
from run import bashC

app = Flask(__name__)

@app.route('/', host="ibmappendly.herokuapp.com")
def student():
	question = ""
	answer = ["","",""]
	return render_template('index.html', question = question, answer = answer)

@app.route('/result', methods = ['POST', 'GET'], host="ibmappendly.herokuapp.com")
def result():
   if request.method == 'POST':
      topic = request.form['Name']
      problem = request.form['Name2']
      bashC(topic, problem)
      text = open('output.txt', 'r+')
      output = text.read()
      text.close()
      
      result = output.split('Votes')
      question = result[0].split('Question:')[-1]
      answer = result[-1].split('-------')

      return render_template("index.html", question = question, answer = answer)

if __name__ == '__main__':
   app.run(debug=True)
