import face_rec
from created_db import get_created_db

#geting created db
db_obj=get_created_db()
#face recognition
print("enter the input image path :\n")
input_img_path=input()
res=face_rec.recognition(input_img_path,db_obj.db)
