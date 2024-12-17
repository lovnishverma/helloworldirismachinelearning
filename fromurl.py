from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and train the model when the app starts
url = "https://raw.githubusercontent.com/lovnishverma/datasets/main/iris.csv"
data = pd.read_csv(url, header=None)
flower = data.values

# Split the data into features and target labels
x = flower[:, :-1]
y = flower[:, -1]

# Train the model
model = LogisticRegression()
model.fit(x, y)

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
    
    # Make a prediction based on the user input
    arr = model.predict([[swidth, sheight, pwidth, pheight]])

    return render_template("index.html", data=str(arr[0]))

if __name__ == '__main__':
    app.run()
