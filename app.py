from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/response', methods=['POST'])
def response():
    place = request.form.get('place')
    noun = request.form.get('noun')
    verb = request.form.get('verb')
    adjective = request.form.get('adjective')
    plural_noun = request.form.get('plural_noun')
    story = Story([place, noun, verb, adjective, plural_noun], """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    res = story.generate(request.form)
    return render_template("response.html", story=res)