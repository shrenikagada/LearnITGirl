from flask import redirect,Flask
app=Flask(__name__)
@app.route('/')
def index():
  return redirect('http://www.google.com')
if __name__ == '__main__':
  app.run(debug=True)