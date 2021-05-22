from flask import Flask
  
import random
app = Flask(__name__)

@app.route('/')

def hello_world():
    d={}
    d["power1"]=random.choice([True, False])
    d["power2"]=random.choice([True, False])
    l=["Error","Green","Yellow"]
    d["lcd"]=l[random.randint(0,2)]
    d["1"]=random.randint(0,100)
    d["2"]=random.randint(0,100)
    d["3"]=random.randint(0,100)
    d["4"]=random.randint(0,100)
    return d
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
