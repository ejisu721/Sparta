from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
target_star = target_movie['star']

search_query = {'star':target_star}
update_query = {'$set':{'star':0}}

db.movies.update_many(search_query, update_query)
