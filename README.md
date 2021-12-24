# Benign-or-Malignant-Detection-in-Mammogram
#Prediction whether a mammogram mass is benign or malignant 
###  we'ill be using the mammographic "masses" public dataset from the UCI repository (source: http://archive.ics.uci.edu/ml/machine-learning-databases/mammographic-masses/)
### This data contains 961 instance detected in mammograms and contains the following attributes
### 1. BI-RADs assesment 1 to 5 (ordinal)
### 2. Age: patient's age in years (integer)
### 3. Shape: mass shape round=1, oval=2, lobular=3, irregular=4 (nominal)
### 4. Margin: mass margin: circumscribed=1 microlobulated=2 obscured=3 ill-defined=4 spiculated=5 (nominal)
### 5. Density: mass density high=1 iso=2 low=3 fat-containing=4 (ordinal)
### 6. Severity: benign=0 or malignant=1 (binominal)

## BI-RADS is an assesment  of how confident the severity classification is: it is not a "predictive" atttribute and so we will discard it. The age, shape, margin and density attributes are the features that we will build our model with and "severity" is the classification we will attempt to predict based on those attributes 

#### Although "shape" and "margin" are nominal data types which sklearn typically doesn't deal with how well they are close enough to ordinal that we shouldn't just discard them. The "shape" for example is ordered increasingly from round to irregular 

#### A lot of unnecessary anguish and surgery arises from false positives arising from mammogram results if we can build a better way to interpret them through supervised machine learning it could improve alot of lives 

## machine learning techniques used in this project
#### Different supervised machine learning techniques to this dataset and see which one yields the highest accuracy as measured with K-fold across validation(k=10)
#### .Decision tree
#### .Random forest
#### .KNN
#### .Naive Bayes
#### .SVM
#### .Neural network using Keras
#### .Other supervise learning techniques that is not mentioned here 
### The data used needs to be cleaned, many rows containing missing data and there may be erroneous data identifiable as outliers as well 
### Techniques like SVM require the input data to be Normalized first and some other techniques used to need hyperparameters tunning that need to be tunned to give best accuracy score 
### And Multi level perceptron turn out to be best. It has accuracy score of 84%
### I implement the model in a strealit web app and deploy it using streamlit. To see the demo version click the link below 
### https://share.streamlit.io/abayomi2020-data/benign-or-malignant-detection-in-mammogram/app.py
