import redis

r = redis.Redis(host='rd', port=6379, db=0)

r.set("name", "sajjad")
print(r.get("name"))
