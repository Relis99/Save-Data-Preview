import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db

from riotwatcher import LolWatcher, ApiError

db_url = 'db-url'

cred = credentials.Certificate('secret-db-key-file')
defalut_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})

watcher = LolWatcher('riot-api-key')
rotation = watcher.champion.rotations('KR')
rotation_ids = rotation['freeChampionIds']

ref = db.reference()
ref.update({'rotation-champions':rotation_ids})