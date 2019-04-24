import os
from flask import Flask
from flask import request
from kebac import Kebac
k = Kebac()
app = Flask(__name__)

@app.route('/')
def kebac():
    french_str = request.args.get('french')
    if french_str is not None:
        return k.convert_input(french_str)
    return "salu toua! ta mal utilise lapi! fait ?french=kekchose"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=os.environ['PORT'])
