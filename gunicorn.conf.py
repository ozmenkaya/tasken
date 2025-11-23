import multiprocessing
import os

# Bind
bind = "0.0.0.0:5004"

# Workers
# SocketIO requires 1 worker if no message queue is used
workers = 1
worker_class = "eventlet"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 60
keepalive = 2

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
access_log_format = "%({x-forwarded-for}i)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\" %(D)s"

# Process naming
proc_name = "tasken"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (optional)
# keyfile = None
# certfile = None
