from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest
import time

app = Flask(__name__)

error_counter = Counter("log_errors", "Number of detected anomalies")
response_gauge = Gauge("response_time", "Response time")

@app.route("/metrics")
def metrics():
    return generate_latest()

@app.route("/log")
def log():
    response_time = random.randint(50, 800)
    response_gauge.set(response_time)

    if response_time > 600:
        error_counter.inc()

    return "Logged"

app.run(host="0.0.0.0", port=5000)

