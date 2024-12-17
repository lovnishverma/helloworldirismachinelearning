from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)

@app.route('/')
def iris():
  return render_template("index.html")

@app.route('/irisf', methods=["POST"])
def page():
  swidth=eval(request.form.get("swidth"))
  sheight=eval(request.form.get("sheight"))
  pwidth=eval(request.form.get("pwidth"))
  pheight=eval(request.form.get("pheight"))
  
  url="https://raw.githubusercontent.com/lovnishverma/datasets/main/iris.csv"
  
  data=pd.read_csv(url, header=None)
  flower=data.values
  
  #Split
  x=flower[:,:4]
  y=flower[:,-1]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[swidth,sheight,pwidth,pheight]])

  return render_template("index.html", data=str(arr[0]))


if __name__ == '__main__':
  app.run()