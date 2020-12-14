import tensorflow as tf
import keras
import numpy as np
import cv2
from keras.models import load_model
from mtcnn import MTCNN


model=load_model("facenet_keras.h5")

def img_enc(img,model=model):
    img=croping_face(img)
    img=cv2.resize(img, (160,160))
    img=np.reshape(img,(1,160,160,3))
    enc=model.predict(img)
    return enc

def croping_face(img):
    img = cv2.imread(img)
    detector = MTCNN()
    res=detector.detect_faces(img)
    x=res[0]["box"][0]
    y=res[0]["box"][1]
    w=res[0]["box"][2]
    h=res[0]["box"][3]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w]
    return roi_color


def verify(inp_img,name,db,model=model):
    enc=img_enc(inp_img,model)
    dist=np.linalg.norm(db[name]-enc)
    print(dist)
    if dist>0.7:
        print("not him")
    else:
        print("him")
        
def recognition(inp_img,db,model=model):
    enc=img_enc(inp_img,model)
    m=100
    encs=[]
    for(name,db_enc) in db.items():
        dist=np.linalg.norm(db_enc-enc)
        encs.append(dist)
        if dist<m:
            m=dist
            identity=name
    print("it's "+identity+".")
    return m,identity,encs

def insert_data_to_db(db_obj,model=model):
    print("enter image path :")
    img_path=input()
    if db_obj.db==None:
        db_obj.create_db()
    db_obj.insert_db(img_enc(img_path,model))

