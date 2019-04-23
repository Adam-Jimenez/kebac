from flask import Flask
from kebac import Kebac
k = Kebac()
app = Flask(__name__)

@app.route('/')
def kebac():
    french_str = request.args.get('french')
    return k.convert_input(french_str)
