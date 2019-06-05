#Music Mood Classifier 
Aim: Build a machine learning model to classify Chinese songs in between happy or sad. 

Step 1: File: https://bit.ly/2IdPsuZ
Preparing the data:
    For the purpose of this exercise, we will build models using these datasets:
    • https://raw.githubusercontent.com/rasbt/musicmood/master/dataset/training/train_lyrics_1000.csv
    • https://github.com/rasbt/musicmood/blob/master/dataset/validation/valid_lyrics_200.csv


We divided the above dataset into test and train, vectorizing the data, removed the stops words.
Used to-idf to rank the words and classify them into happy or sad words.

The accuracy of the model:

Accuracy for the test is:  70.0.
Precision for the test is:  75.28089887640449.
Recall for the test is:  63.8095238095238.
F1 score for the test is:  69.0721649484536.
Pickled the model in Finalmodel.pkl file and used this to predict the sentiment.
The function model_predict is used to make the prediction.


 
Step 2 Application :
Building a flask application which will take the input of Chinese song and translate it to english. The model_predict function is used to predict whether the song is happy or sad.

Step 3:
We finally deployed the application on heroku. 
 
https://assignment4musicmood.herokuapp.com
https://musicmoodversion2.herokuapp.com

Claat: https://codelabs-preview.appspot.com/?file_id=1jG89Wz1-M-ZfXXaEVbqBMbEGy5P5gxnOW7UNrh4cLwI#0
Youtube Link: https://youtu.be/p35Iqu4k3Rs
