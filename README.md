# CAD 2 Abgabe 2


docker-compose up --build


  a.	IP für Result-App: http://127.0.0.1:3001/
  
  b.	IP für Voting-App: http://127.0.0.1:3000/
   
Verwendete Container:
•	Result-App
•	PostgreSQL-Container
•	Worker-Container
•	Redis-Container
•	Voting-WebApp


# Fehler bei mir am Rechner

Ich habe alles versucht, aber mein vote-node will einfach nicht mit der Postgres verbinden. Hier die gesamte Ausgabe:

`hubert-schwaiger@hubert-schwaiger-3-04:~/Dokumente/Joanneum/CAD2/Nestler/CAD2_UE02-main_rewritten/CAD2_UE02-main$ docker-compose up --build
Creating network "cad2_ue02-main_backend" with the default driver
Creating volume "cad2_ue02-main_db-data" with default driver
Building vote
[+] Building 1.4s (10/10) FINISHED                                                                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                              0.0s
 => => transferring dockerfile: 132B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                1.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                   0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:4ee0613170ac55ebc693a03b6655a5c6f387126f6bc3390e739c2e6c337880ef                                          0.0s
 => [internal] load build context                                                                                                                                 0.0s
 => => transferring context: 1.22kB                                                                                                                               0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                     0.0s
 => CACHED [3/4] COPY . .                                                                                                                                         0.0s
 => CACHED [4/4] RUN pip install flask redis                                                                                                                      0.0s
 => exporting to image                                                                                                                                            0.0s
 => => exporting layers                                                                                                                                           0.0s
 => => writing image sha256:c05723175175026a38dc9db7e8387ec953451fee207c7f1f9cb96db291033169                                                                      0.0s
 => => naming to docker.io/library/cad2_ue02-main_vote                                                                                                            0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/r5ym8jgrin4d436tpeb0ufcpb

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
Building worker
[+] Building 0.8s (9/9) FINISHED                                                                                                                  docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                              0.0s
 => => transferring dockerfile: 145B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                0.7s
 => [internal] load .dockerignore                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                   0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:4ee0613170ac55ebc693a03b6655a5c6f387126f6bc3390e739c2e6c337880ef                                          0.0s
 => [internal] load build context                                                                                                                                 0.0s
 => => transferring context: 682B                                                                                                                                 0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                     0.0s
 => CACHED [3/4] COPY . .                                                                                                                                         0.0s
 => CACHED [4/4] RUN pip install redis psycopg2-binary                                                                                                            0.0s
 => exporting to image                                                                                                                                            0.0s
 => => exporting layers                                                                                                                                           0.0s
 => => writing image sha256:e6807f1f65d15a9fba2259ac0b698f753b38e45a893654502bcf8d127b196866                                                                      0.0s
 => => naming to docker.io/library/cad2_ue02-main_worker                                                                                                          0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/bmx60pna8udfp6ndfwvnwpyu4

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
Building result
[+] Building 1.4s (10/10) FINISHED                                                                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                              0.0s
 => => transferring dockerfile: 127B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/node:14                                                                                                        1.3s
 => [auth] library/node:pull token for registry-1.docker.io                                                                                                       0.0s
 => [internal] load .dockerignore                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                   0.0s
 => [1/4] FROM docker.io/library/node:14@sha256:a158d3b9b4e3fa813fa6c8c590b8f0a860e015ad4e59bbce5744d2f6fd8461aa                                                  0.0s
 => [internal] load build context                                                                                                                                 0.0s
 => => transferring context: 1.76kB                                                                                                                               0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                     0.0s
 => CACHED [3/4] COPY . .                                                                                                                                         0.0s
 => CACHED [4/4] RUN npm install express pg                                                                                                                       0.0s
 => exporting to image                                                                                                                                            0.0s
 => => exporting layers                                                                                                                                           0.0s
 => => writing image sha256:45520a26cd9e0ff4bec597f3e5f7a7c1355cb00112d03d249acaead9c7f9c3cd                                                                      0.0s
 => => naming to docker.io/library/cad2_ue02-main_result                                                                                                          0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/qdaioo585npgu4a70ecaz0jqj

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
Creating cad2_ue02-main_redis_1 ... done
Creating cad2_ue02-main_db_1     ... done
Creating cad2_ue02-main_worker_1 ... done
Creating cad2_ue02-main_vote_1   ... done
Creating cad2_ue02-main_result_1 ... done
Attaching to cad2_ue02-main_redis_1, cad2_ue02-main_db_1, cad2_ue02-main_worker_1, cad2_ue02-main_vote_1, cad2_ue02-main_result_1
db_1      | The files belonging to this database system will be owned by user "postgres".
db_1      | This user must also own the server process.
db_1      | 
db_1      | The database cluster will be initialized with locale "en_US.utf8".
db_1      | The default database encoding has accordingly been set to "UTF8".
db_1      | The default text search configuration will be set to "english".
db_1      | 
db_1      | Data page checksums are disabled.
db_1      | 
db_1      | fixing permissions on existing directory /var/lib/postgresql/data ... ok
redis_1   | 1:C 13 Dec 2024 22:34:07.258 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1   | 1:C 13 Dec 2024 22:34:07.258 * Redis version=7.4.1, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1   | 1:C 13 Dec 2024 22:34:07.258 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
db_1      | creating subdirectories ... ok
redis_1   | 1:M 13 Dec 2024 22:34:07.258 * monotonic clock: POSIX clock_gettime
db_1      | selecting dynamic shared memory implementation ... posix
redis_1   | 1:M 13 Dec 2024 22:34:07.259 * Running mode=standalone, port=6379.
redis_1   | 1:M 13 Dec 2024 22:34:07.259 * Server initialized
redis_1   | 1:M 13 Dec 2024 22:34:07.259 * Ready to accept connections tcp
db_1      | selecting default max_connections ... 100
db_1      | selecting default shared_buffers ... 128MB
db_1      | selecting default time zone ... UTC
db_1      | creating configuration files ... ok
db_1      | running bootstrap script ... ok
worker_1  | Traceback (most recent call last):
worker_1  |   File "/app/worker.py", line 6, in <module>
worker_1  |     connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")
worker_1  |   File "/usr/local/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
worker_1  |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
worker_1  | psycopg2.OperationalError: connection to server at "db" (172.21.0.3), port 5432 failed: Connection refused
worker_1  | 	Is the server running on that host and accepting TCP/IP connections?
worker_1  | 
result_1  | Result app running on port 80
result_1  | (node:1) UnhandledPromiseRejectionWarning: Error: connect ECONNREFUSED 172.21.0.3:5432
result_1  |     at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1159:16)
result_1  | (Use `node --trace-warnings ...` to show where the warning was created)
result_1  | (node:1) UnhandledPromiseRejectionWarning: Unhandled promise rejection. This error originated either by throwing inside of an async function without a catch block, or by rejecting a promise which was not handled with .catch(). To terminate the node process on unhandled promise rejection, use the CLI flag `--unhandled-rejections=strict` (see https://nodejs.org/api/cli.html#cli_unhandled_rejections_mode). (rejection id: 1)
result_1  | (node:1) [DEP0018] DeprecationWarning: Unhandled promise rejections are deprecated. In the future, promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
db_1      | performing post-bootstrap initialization ... sh: locale: not found
db_1      | 2024-12-13 22:34:07.881 UTC [35] WARNING:  no usable system locales were found
cad2_ue02-main_worker_1 exited with code 1
vote_1    |  * Serving Flask app 'app'
vote_1    |  * Debug mode: off
vote_1    | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
vote_1    |  * Running on all addresses (0.0.0.0)
vote_1    |  * Running on http://127.0.0.1:80
vote_1    |  * Running on http://172.21.0.6:80
vote_1    | Press CTRL+C to quit
db_1      | ok
db_1      | syncing data to disk ... initdb: warning: enabling "trust" authentication for local connections
db_1      | You can change this by editing pg_hba.conf or using the option -A, or
db_1      | --auth-local and --auth-host, the next time you run initdb.
db_1      | ok
db_1      | 
db_1      | 
db_1      | Success. You can now start the database server using:
db_1      | 
db_1      |     pg_ctl -D /var/lib/postgresql/data -l logfile start
db_1      | 
db_1      | waiting for server to start....2024-12-13 22:34:08.493 UTC [41] LOG:  starting PostgreSQL 13.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 14.2.0) 14.2.0, 64-bit
db_1      | 2024-12-13 22:34:08.496 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1      | 2024-12-13 22:34:08.501 UTC [42] LOG:  database system was shut down at 2024-12-13 22:34:08 UTC
db_1      | 2024-12-13 22:34:08.506 UTC [41] LOG:  database system is ready to accept connections
db_1      |  done
db_1      | server started
db_1      | 
db_1      | /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
db_1      | CREATE TABLE
db_1      | 
db_1      | 
db_1      | waiting for server to shut down....2024-12-13 22:34:08.640 UTC [41] LOG:  received fast shutdown request
db_1      | 2024-12-13 22:34:08.642 UTC [41] LOG:  aborting any active transactions
db_1      | 2024-12-13 22:34:08.645 UTC [41] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
db_1      | 2024-12-13 22:34:08.645 UTC [43] LOG:  shutting down
db_1      | 2024-12-13 22:34:08.675 UTC [41] LOG:  database system is shut down
db_1      |  done
db_1      | server stopped
db_1      | 
db_1      | PostgreSQL init process complete; ready for start up.
db_1      | 
db_1      | 2024-12-13 22:34:08.776 UTC [1] LOG:  starting PostgreSQL 13.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 14.2.0) 14.2.0, 64-bit
db_1      | 2024-12-13 22:34:08.776 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1      | 2024-12-13 22:34:08.776 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1      | 2024-12-13 22:34:08.780 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1      | 2024-12-13 22:34:08.785 UTC [56] LOG:  database system was shut down at 2024-12-13 22:34:08 UTC
db_1      | 2024-12-13 22:34:08.791 UTC [1] LOG:  database system is ready to accept connections
vote_1    | 172.21.0.1 - - [13/Dec/2024 22:35:30] "GET / HTTP/1.1" 200 -
vote_1    | 172.21.0.1 - - [13/Dec/2024 22:35:30] "GET /favicon.ico HTTP/1.1" 404 -`


