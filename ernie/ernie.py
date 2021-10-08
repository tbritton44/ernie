from flask import Flask, render_template
from transformers import pipeline

app = Flask(__name__, template_folder='../templates')
unmasker = pipeline('fill-mask', model='distilbert-base-uncased')

@app.route("/")
def hello_world():
    masks = unmasker("Hello, This is Farmer Ernie. You might wonder why a city kid like me is doing out here in the [MASK]?")
    return render_template("index.html", masks=masks)
