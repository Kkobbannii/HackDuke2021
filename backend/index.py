
from flask import Response
from flask import Flask, request, flash, redirect, url_for
from flask import render_template
import os
# from PIL import image
import pytesseract as tesseract



current_directory = os.getcwd()
print(current_directory)
statDir = current_directory+'/static/'
templateDir = current_directory+'/templates/'

print(tesseract.image_to_string(current_directory+'/image.jpg'))

app = Flask(__name__,static_folder=statDir,
            template_folder=templateDir)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/', methods=['GET'])
def home():
    return "Python has communicated with the backend"


if __name__ == '__main__':
  app.run(port=8080, debug=True, use_reloader=True)
  