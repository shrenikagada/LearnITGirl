from flask import Flask,render_template
from flask_bootstrap import Bootstrap
# ...

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/index')
def index():
  return render_template('index.html')
@app.route('/userbootstrap/<name>')
def user(name):
  return render_template('userbootstrap.html',name=name)
if __name__ == '__main__':
  app.run(debug=True)
