#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
#this is user's info

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "unknown"
my_user.last_name = "abokhabar"
my_user.email = "unknown456543@gmail.com"
my_user.password = "khabo"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
Iam_user2 = User()
Iam_user2.first_name = "mossab"
Iam_user2.email = "amossab89@gmail.com"
Iam_user2.password = "khabo"
Iam_user2.save()
print(Iam_user2)
