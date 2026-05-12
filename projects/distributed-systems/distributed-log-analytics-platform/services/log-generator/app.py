import json
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()

services = [
    "auth-service",
    "payment-service",
    "iot-gateway",
    "api-service"
]

levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "Request processed successfully",
        "User authenticated",
        "Telemetry data received"
    ],
    "WARNING": [
        "High memory usage detected",
        "Slow API response",
        "Retrying database connection"
    ],
    "ERROR": [
        "Database timeout",
        "Kafka broker unavailable",
        "Unhandled application exception"
    ]
}

log_file = "/app/logs/application.log"

while True:

    level = random.choice(levels)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "service": random.choice(services),
        "level": level,
        "message": random.choice(messages[level]),
        "user_id": random.randint(1000, 9999),
        "ip_address": fake.ipv4(),
        "response_time_ms": random.randint(20, 3000)

        #second step
        ,"status_code": random.choice([200, 201, 400, 401, 404, 500]),
        "region": random.choice(["eu-west", "us-east", "asia-south"]),
        "device_type": random.choice(["mobile", "desktop", "iot"]),
        "endpoint": random.choice([
            "/api/login",
            "/api/payment",
            "/api/telemetry",
            "/api/orders"
        ])
        #
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(log_entry)

    time.sleep(2)