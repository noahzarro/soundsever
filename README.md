# Sound Server

## Installation
- Install python 3
- Install pip
- Install virtualenv by `pip install virtualenv`
- Run `install.sh` to create a virtual environment and install all pip packages needed

## Usage
Run `run.sh` to start the server

The server runs on port 8080

Use the following GET requests:

- `\play\<id>` to play a sound (request is fulfilled after sound is finished)
- `\sounds` a JSON response containing the sounds available. An array of `"name": <filename_without_extension>, "id": int` objects. They are automatically generated from the files in the sound folder
- `\` for Hello World
- `\sloth` for a surprise 