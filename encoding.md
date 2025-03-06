### scikit-learn automatically handles string labels in classification problems, but not for categorical features.

### How does this work?
- In model.fit(features, labels), the labels (y) are string values (e.g., "setosa", "versicolor", "virginica").
- *Scikit-learn automatically encodes string labels* internally using LabelEncoder when training classification models like LogisticRegression.  
- However, this does *not* apply to categorical features (i.e., independent variables X), which must still be manually encoded.

### When would this fail?
If the dataset had *categorical features* (e.g., "color": ["red", "green", "blue"]), scikit-learn would *not* automatically encode them. You'd need to use OneHotEncoder or OrdinalEncoder before training.
