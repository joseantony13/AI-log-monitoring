import random
import time

levels = ["INFO", "WARNING", "ERROR"]

while True:
    level = random.choices(levels, weights=[70, 20, 10])[0]
    log = f"{level} - Response time: {random.randint(50, 500)}ms"

    with open("app.log", "a") as f:
        f.write(log + "\n")

    time.sleep(1)

