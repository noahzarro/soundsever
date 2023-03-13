from playsound import playsound
from flask import Flask
from threading import Thread

import os
import json

print("hello")
sounds = []

cur_id = 0

for file in os.listdir("sounds"):
    if file.endswith(".mp3"):
        sounds.append({"name": file.split(".")[0], "id": cur_id})
        cur_id += 1

app = Flask(__name__, static_url_path="/", static_folder="public")


def play_sound_file(file):
    print("hello gitter")
    playsound(file)


@app.route("/")
def hello_world():
    return "Hello, Gitter!"


@app.route("/sounds")
def show_sounds():
    return json.dumps(sounds)


@app.route("/play/<id>")
def play_sound(id):
    sound_to_play = sounds[int(id)]["name"] + ".mp3"
    t = Thread(target=play_sound_file, args=("sounds/" + sound_to_play,))
    t.start()
    return sounds[int(id)]["name"]


app.run(host="0.0.0.0", port=8080)
