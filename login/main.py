from flask import Flask
from flask import render_template

import forms

app = Flask(__name__)

@app.route('/')
def index():
	comment_form = forms.CommentForm()
	title = 