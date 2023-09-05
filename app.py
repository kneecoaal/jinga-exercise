from flask import Flask, request, render_template 
from stories import Story 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('questions.html')

@app.route('/story', methods = ['POST'])
def generate():
    place = request.form.get("place")
    adjective = request.form.get("adjective")
    noun = request.form.get("noun")
    verb = request.form.get("verb")
    plural_noun = request.form.get("plural_noun")
    new_story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
"""Once upon a time in a long-ago {place}, there lived a
    large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    ans = {'place':place, 'adjective':adjective, 'noun':noun, 'verb':verb, 'plural_noun':plural_noun}
    story = new_story.generate(ans)
    return render_template("story.html", story=story)

