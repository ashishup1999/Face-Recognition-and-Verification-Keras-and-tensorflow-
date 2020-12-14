import face_rec
from database import database

def get_created_db():
    return db_obj

db_obj=database()

db_obj.db={}
db_obj.db["Amitabh Bachan"]=face_rec.img_enc("images/amitabh1.jfif")
db_obj.db["Pankaj Tripathi"]=face_rec.img_enc("images/pnkj1.jfif")
db_obj.db["Shahrukh Khan"]=face_rec.img_enc("images/srk1.jpg")
db_obj.db["Akshay Kumar"]=face_rec.img_enc("images/aki1.jfif")
db_obj.db["Nawazudin Sidique"]=face_rec.img_enc("images/nawaj1.jfif")
db_obj.db["Raj Kumar Rao"]=face_rec.img_enc("images/rkr1.jfif")


# for entering an encoding into db we can use  
"""face_rec.insert_data_to_db(db_obj)"""
