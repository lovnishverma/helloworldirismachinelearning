from flask import Flask, render_template, request
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def iris():
    return render_template("index.html")

@app.route('/irisf', methods=["POST"])
def page():
    # Get input values from the form
    swidth = float(request.form.get("swidth"))
    sheight = float(request.form.get("sheight"))
    pwidth = float(request.form.get("pwidth"))
    pheight = float(request.form.get("pheight"))
  
    # Step : Load the Iris dataset from sklearn
    iris = datasets.load_iris()
    x = iris.data  # Features (sepal length, sepal width, petal length, petal width)
    y = iris.target  # Labels (species)

    # Initialize the model and train it
    model = LogisticRegression(max_iter=200)
    model.fit(x, y)
  
    # Make prediction using the model
    arr = model.predict([[swidth, sheight, pwidth, pheight]])
    predicted_flower = iris.target_names[arr[0]]  # Map numeric label to species name

    return render_template("index.html", data=predicted_flower)  # Pass the flower name



if __name__ == '__main__':
    app.run()
