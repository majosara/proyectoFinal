from wtforrms import Form
from wtforrms import StringField, TextFiel
import forms

class CommentForm(Form):
	"""docstring for CommentForm"""
	username = StringField('username')
	comment = TextField('comentario')