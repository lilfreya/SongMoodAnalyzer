# pythonspot.com
from flask import Flask, render_template, flash, request
from  MoodOfSong.code.FinalModel import ngram_vectorize, model_predict
import pickle
from googletrans import Translator
translator = Translator()
classifier = pickle.load(open('Finalmodel.pkl', 'rb'))


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

pickle_in= open('Finalmodel.pkl', 'rb')
Mymodel= pickle.load(pickle_in)




@app.route("/", methods=['GET', 'POST'])
def lyrics_form():
    if request.method == 'POST':
        lyrics = request.form.get('lyrics')
        translation = translator.translate(lyrics)
        lyricData=translation.text
        value, value2=model_predict(lyricData)
        probabvalue=" "
        if (value==['happy']):
            probavalue =(1- (value2[:, 1])) * 100

            val="Happy"


            return """
            <h1> Mood of the song is {}</h1>
            <h2> The probability : {} is {}%</h2>
            <img src="https://media.giphy.com/media/1MTLxzwvOnvmE/giphy.gif" style="max-width:30%;height:40%;">
            <h3>
                        Translated Song:
                         </h3>
                         <h4>{}. 
                        </h4>
                        
                    
    
                        """.format(val, val, probavalue, translation.text)


        else:
            probabvalue = ( (value2[:, 1])) * 100
            val = "Sad"
            print(value)
            probabvalue = (value2[:, 1]) * 100
            return """
            <h1> Mood of the song is {} </h1>
            <h2> The probability : {} is {}%</h2>
            <h3><img src="https://media1.tenor.com/images/30e8e3e8c85accdcd0702ef2bb859e84/tenor.gif?itemid=5823074" style="max-width:30%;height:40%;">
                        </h3>
                        <h3>Translated Song:
                         </h3>
                         <h4>{}. 
                        </h4>
            

                        """.format(val, val, probabvalue, translation.text)


    return '''
    <!doctype html>
<html>
<head>
    <title>Song mood classification based on lyrics</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
   .hero-image {
  background: url(https://assetplanningcorp.com/wp-content/uploads/2019/01/Contentment.jpg) no-repeat center;
  background-size: cover;
  height: 800px;
  position: relative;
}

.hero-text {
  text-align: center;
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
}

.xyz{
  color:green;
  text-align: left;
  position: absolute;
  top: 60%;
  left: 10%;
}

.abc{
  text-align: left;
  position: absolute;
  top: 70%;
  left: 10%;
}

.def{
text-align: left;
  position: absolute;
  top: 90%;
  left: 10%;
}

input[type=submit] {
  background-color:green;
  color: white;
  font-size:100%;
  font-style:bold;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: left;
}
    </style>
  </head>
  <body>
  <div class="hero-image">
   <div class="hero-text">
      <h1 style="font-size:50px">Welcome to K3G Music</h1>
      <h2>Sentiment analyzer</h2>
      <h3>Easily analyze the feelings behind the words with just a click !!!!</h3>
      <h3>Enter your lyrics in any language and know the sentiment of the song :)</h3>
   </div>
      <div class="xyz">
        <h2>Please enter the lyrics below</h2>
      </div>

    <form method=POST>
        <div class="abc">
          <textarea rows="10" cols="50" id="songtext" name="lyrics" placeholder="Enter lyrics.."></textarea>
        </div>
        <div class="def">
	      <input type=submit value='Submit' name='submit_btn'>
	    </div>
    </form>
  </div>
  </body>
</html>
    '''

if __name__ == "__main__":
    # Getting the classifier ready
    app.run()

#<input type="text" name="lyrics" value="Enter the lyrics" cols="30" rows="10">
# <body>
    #   <form method ="POST">
    #     <h1>Please enter the songtext below:</h1>
    #     <textarea name="lyrics" rows="10" cols="30" value="Enter ther lyrics"></textarea></br>
    #     <input type ="submit" value="Submit songtext" name="sbmtbtn"></form>
    # </body>