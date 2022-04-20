import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db

db_url = 'db-url'

cred = credentials.Certificate('secret-db-key-file')
defalut_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})

ref = db.reference('rotation-champions')
row = ref.get()
print(row)