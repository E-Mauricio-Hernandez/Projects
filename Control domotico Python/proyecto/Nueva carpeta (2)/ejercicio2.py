from flask import Flask, render_template
import datetime
import time
import os
global aux
global hora1
global hora2
global hora3
global hora4
global hora5
global hora6
global hora7
global hora8
global hora9
global hora10
aux=0
hora1=""
hora2=""
hora3=""
hora4=""
hora5=""
hora6=""
hora7=""
hora8=""
hora9=""
hora10=""
app = Flask(__name__)
@app.route("/")
def hello():
    global horass
    global aux
    global hora1
    global hora2
    global hora3
    global hora4
    global hora5
    global hora6
    global hora7
    global hora8
    global hora9
    global hora10
    f = open ('datos.txt','r')
    mensaje = f.read()
    aux =mensaje.split(",")
    f.close()
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
        'time': timeString,
        'valor1': aux[10],
        'valor2': aux[11],
        'valor3': aux[12],
        'valor4': aux[13],
        'valor5': aux[14],
        'valor6': aux[15],
        'valor7': aux[16],
        'valor8': aux[17],
        'valor9': aux[18],
        'valor10': aux[19],
        'valor11': aux[0],
        'valor12': aux[1],
        'valor13': aux[2],
        'valor14': aux[3],
        'valor15': aux[4],
        'valor16': aux[5],
        'valor17': aux[6],
        'valor18': aux[7],
        'valor19': aux[8],
        'valor20': aux[9],

      
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    if port == 5001:
        app.debug = True
    app.run(host='192.168.43.44', port=port)    
