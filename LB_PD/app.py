from flask import Flask
from threading import Thread
from flask import render_template
import serial
import time

app = Flask(__name__)


ArduinoSerial = serial.Serial('COM6', 9600)
app = Flask(__name__)

def readTemp():
    global tempLM
    global tempDS
    while True:
        tempLM = ArduinoSerial.readline().rstrip().decode()
        tempDS = ArduinoSerial.readline().rstrip().decode()

@app.route('/')
def index():
    return render_template("temp.html", dataLM=tempLM, dataDS= tempDS)

T = Thread(target=readTemp)
T.start()

if __name__ == '__main__':
    app.run()