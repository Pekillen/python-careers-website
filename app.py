from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': ' Los Angeles',
    'salary': 'USD 750000',
  },
  {
    'id': 2,
    'title': 'Software developer',
    'location': ' Oslo',
    'salary': 'USD 120000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Berlin',
    'salary': 'USD 190000'
  },
  {
    'id': 4,
    'title': 'React developer',
    'location': ' Geneva',
    'salary': 'USD 90000'
  },
]


@app.route("/")
def render():
  return render_template('home.html', jobs=JOBS, company_name='Python')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
