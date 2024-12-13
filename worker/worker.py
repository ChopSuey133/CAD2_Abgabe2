import psycopg2
import redis
import time

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)
connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")

while True:
    votes = redis_client.lrange("votes", 0, -1)
    with connection.cursor() as cur:
        for vote in votes:
            cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote.decode("utf-8"),))
        connection.commit()
    redis_client.delete("votes")
    time.sleep(25)