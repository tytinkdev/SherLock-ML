This python virtual environment is used for a multi-part lab in the creation of a Flask app which will later be deployed on Heroku. 

The purpose of this pickled model is to provide predictions on whether a phone is currently running a malicious application or not. 

In order to use this virtual environment, follow these steps: 

1. Create a virtual python environment using 'python3 -m venv SHvenv'
2. Active the venv by typing 'source SHvenv/bin/activate'
3. Install requirements using !pip install -r requirements.txt
4. Fit the model by loading in your data as a url that downloads a T4 file. This means that the download should be in csv format, and should be a raw text file. The code will drop duplicate and blank rows for you, select the required labels and features, scale them, split the dataset into training in test and training splits, then run a logistic regression on the data. It will then pickle (serialize) the model for future testing against new data. 
5. To test a new file using the pre-built model, simply load scaled T4 test data into newdata.py, and type the terminal command !python3 test_pickled_model.py. The script should print out a list of predictions # SherLock-ML
