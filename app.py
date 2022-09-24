from flask import Flask, render_template, jsonify

app = Flask(__name__)
 
company_name = 'Jovian'

JOBS =[
  {'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,000,000'},
  {'id': 2,
  'title': 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,000,000'},
  {'id': 3,
  'title': 'Frontend engineer',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,000,000'},
  {'id': 4,
  'title': 'Backend engineer',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,000,000'}
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, title = company_name)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
