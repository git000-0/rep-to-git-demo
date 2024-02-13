from flask import Flask, render_template

app = Flask(__name__)

DESC = [
  {
    'id: ' : 1,
    'price': '$180/g',
    'made': '新疆',
    'name': '苹果'
  },
  {
    'id: ' : 2,
    'price': '',
    'made': '',
    'name': '香蕉'
  },
  {
    'id: ' : 3,
    'price': '',
    'made': '',
    'name': '橘子'
  }  
]

@app.route('/')
def hello_world():
      return render_template('home.html',
                            info = DESC)
                            
  
if __name__ == '__main__': 
  app.run(host="0.0.0.0", debug = True)


