import pymongo
import gridfs
import pytesseract
import urllib 
from bson import Regex
import json
from os import listdir
import os
from PIL import Image
# CONNECT TO DATABASE

tesseract = pytesseract
current_directory = os.getcwd()

try:
    connection_url = "mongodb+srv://Admin:"+urllib.parse.quote("#cUR+3^pdU.:q`")+"jG@cluster0.0dc2v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    print("connection successful!")
except Exception as e:
    print("connection error". e)

# USER PICTURES DATABASE FROM MONGODB

db = client.get_database('memes')
tagsDatabase = db["tags"]
fs = gridfs.GridFS(db)
print(db.list_collection_names())

data = {"tags":
            [{"IDs":["unga bunga"],"tagName":"peggable"}
            ]}

# for filename in listdir("photos"):
for i in range(1):
    # filename = "IMG_8432.jpg"
# filename = "vqyn2sto9lu71.jpeg"
    filename = "filename1.png"
    print("new photo")
    phototags = (tesseract.image_to_string(current_directory+"/photos/"+filename)).lower().replace("\n", "").split(" ")
    print(phototags)
    for newTag in phototags:
        exists = False
        for tag in data["tags"]:

            print("new iteration")
            print(str(newTag))
            print(str(tag['tagName']))
            if str(newTag) == str(tag['tagName']):
                print(str(tag['IDs']))
                tag['IDs'].append(filename)
                exists = True
                break
        
            print(exists)
        print("data added")
        if not exists:
            data["tags"].append({"IDs":[filename],"tagName": str(newTag)})
            print({"IDs":[filename],"tagName": "peggable"})
            with open('data.json','w',encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            exists = False




# #Open the image in read-only format.

for fn in listdir("photos"):
    if fn.endswith('.png'):
        try:
            img = Image.open("photos/"+fn)
        except:
            os.remove("photos/"+fn)

for fn in listdir("photos"):            
    with open("photos/"+fn, 'rb') as f:
        contents = f.read()

    fs.put(contents, filename=fn)

with open('data.json') as dataJson:
    file_data = json.load(dataJson)
tagsDatabase.insert(file_data)

client.close()
# # Regex(r'.*\.(png|jpg)')
# # READ IMAGES

# # searches for an image based on filename
# for f in fs.find({'filename': 'file'}):
#     # binary image data
#     data = f.read()
#     print(data)
#     with open("newfile.png","wb") as fi:
#         # writing to file
#         fi.write(data)
#     # close file
#     fi.close()