from flask import Flask, render_template
import speech_recognition as sr


app = Flask(__name__)


def recognize_language(is_english):
    """
       This Function recognize the voice in different langauge
       based on the is_english bool value.
       it ends the text when  the user stops speaking,
       if the user does not speak or there is any other error it will send a message
    """
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.energy_threshold = 300
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Speak Anything .. : ')
        audio = r.listen(source)
        language = 'ar-AR' if not is_english else 'en-US'
        try:
            return r.recognize_google(audio,language=language)
        except:
            # non-recognizable
            return "Could not Recognize your voice"


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/get-text/<en>")
def get_text(en):
    is_english = True if en == "True" else False
    text = recognize_language(is_english)
    return render_template("index.html", result=text)


if __name__ == '__main__':
    app.run(debug=True)
