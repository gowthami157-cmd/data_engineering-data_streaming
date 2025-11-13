from datetime import datetime
import json
import uuid

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 11, 12, 5, 0),
}


def get_data():
    """Return a single random user payload."""
    res = requests.get("https://randomuser.me/api/", timeout=10)
    res.raise_for_status()
    return res.json()["results"][0]


def format_data(res):
    """Flatten user payload into a Kafka-friendly dict."""
    location = res["location"]
    data = {
        "id": str(uuid.uuid4()),
        "first_name": res["name"]["first"],
        "last_name": res["name"]["last"],
        "gender": res["gender"],
        "address": f"{location['street']['number']} {location['street']['name']}, "
        f"{location['city']}, {location['state']}, {location['country']}",
        "post_code": location["postcode"],
        "email": res["email"],
        "username": res["login"]["username"],
        "dob": res["dob"]["date"],
        "registered_date": res["registered"]["date"],
        "phone": res["phone"],
        "picture": res["picture"]["medium"],
    }
    return data


def stream_data():
    """Fetch and print a single formatted record (placeholder for Kafka push)."""
    user_payload = get_data()
    formatted = format_data(user_payload)
    print(json.dumps(formatted))


with DAG(
    "user_automation",
    default_args=default_args,
    description="Fetch random users and push to Kafka",
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    streaming_task = PythonOperator(
        task_id="streaming_data_from_kafka",
        python_callable=stream_data,
    )


if __name__ == "__main__":
    stream_data()
