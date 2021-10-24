
from flask import Response
from flask import Flask, request, flash, redirect, url_for,send_file
from flask import render_template
import os
import urllib 
import pymongo
import gridfs
from bson import Regex
# from PIL import image



current_directory = os.getcwd()
print(current_directory)
statDir = current_directory+'/static/'
templateDir = current_directory+'/templates/'

# print(tesseract.image_to_string(current_directory+'/image.jpg'))



try:
    # connection_url = "mongodb+srv://readOnly:"+urllib.parse.quote("maroondeparture")+"jG@cluster0.0dc2v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    connection_url = "mongodb+srv://Admin:"+urllib.parse.quote("#cUR+3^pdU.:q`")+"jG@cluster0.0dc2v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    print("connection successful!")
except Exception as e:

    print("connection error". e)

# USER PICTURES DATABASE FROM MONGODB

db = client.get_database('memes')
tagsDatabase = db["tags"]
fs = gridfs.GridFS(db)
# print(db.list_collection_names())

app = Flask(__name__,static_folder=statDir,
            template_folder=templateDir)

for f in fs.find({'filename': 'file'}):
    # binary image data
    data = f.read()
    print(data)
    with open("newfile.png","wb") as fi:
        # writing to file
        fi.write(data)
    # close file
    fi.close()

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
    binaries = []
    for f in fs.find({'filename': Regex(r'.*\.(png|jpg)')}):
    # binary image data
        data = f.read()
        print(data)
        # with open("newfile.png","wb") as fi:
        # writing to file
        binaries.append(data)
    # close file
        # fi.close()
    return binaries[0]
    # return index.html


if __name__ == '__main__':
  app.run(port=8080, debug=True, use_reloader=True)
  