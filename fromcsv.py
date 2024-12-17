from flask import Flask, render_template, request
import pandas as pd
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

    # Load the Iris dataset from CSV (use the path to your local CSV file or URL)
    # Example URL: "https://raw.githubusercontent.com/lovnishverma/datasets/main/iris.csv"
    url = "https://raw.githubusercontent.com/lovnishverma/datasets/main/iris.csv"
    data = pd.read_csv(url)  # Don't Set header=None if there is header row present in the CSV
    
    # Separate the features (X) and target labels (Y)
    x = data.iloc[:, :-1]  # Select all rows and all columns except the last (features)
    y = data.iloc[:, -1]   # Select all rows and the last column (target labels)

    # Initialize the Logistic Regression model and train it
    model = LogisticRegression(max_iter=200)
    model.fit(x, y)

    # Make a prediction based on the user input
    arr = model.predict([[swidth, sheight, pwidth, pheight]])

    # Map the predicted numeric label to the flower name
    flower_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    predicted_flower = flower_names[arr[0]]

    return render_template("index.html", data=str(predicted_flower))


if __name__ == '__main__':
    app.run()
