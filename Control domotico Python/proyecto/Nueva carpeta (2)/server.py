from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    return "Juan me lo mama"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='172.17.228.86', port=port)