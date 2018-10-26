from flask import Flask, render_template, url_for
app = Flask(__name__)

trackers = [
  { 
    'title': 'NBA League Pass',
    'description': 'YouTube TV', 
    'cost': '$250'
  },
  { 
    'title': 'Voormi',
    'description': 'Wool is cool', 
    'cost': '$250'
  }
]

@app.route('/')
def home():
  return render_template('home.html', trackers=trackers)

@app.route('/new')
def add_new():
  return render_template('new.html', title='Add New Tracker')

if __name__ == '__main__':
  app.run(debug=True)