from flask import Flask, render_template
import json
import random

app = Flask(__name__)

with open('mood_songs.json', 'r') as f:
    mood_songs = json.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood']
    if mood in mood_songs:
        song = random.choice(mood_songs[mood])
        return render_template('recommend.html', song=song, mood=mood)

if __name__ == '__main__':
    app.run(debug=True)
