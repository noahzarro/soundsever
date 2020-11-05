from playsound import playsound
from flask import Flask

import os
import json

sounds = []

cur_id = 0

for file in os.listdir("sounds"):
    if file.endswith(".mp3"):
        sounds.append({"Name": file.split(".")[0], "id": cur_id})
        cur_id += 1

print(sounds)

app = Flask(__name__, static_url_path='/', static_folder='public')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/sounds')
def show_sounds():
    return json.dumps(sounds)

@app.route('/play/<id>')
def play_sound(id):
    sound_to_play = sounds[int(id)]["Name"]+".mp3"
    print(sound_to_play)
    playsound("sounds/"+sound_to_play)
    return sounds[int(id)]["Name"]


app.run(host="localhost", port=8080)
