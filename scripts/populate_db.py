"""
Script to create companies, devices, and measurements.
"""
import json
import random

import requests


def create_company(name="A", location="Berlin"):
    url = "http://localhost:8000/api/companies/"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": name,
        "location": location
    })
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    return response.json()["id"]


def create_device(company=None, device_id="QWE", active=True, labels=["label1", "label2"]):
    url = "http://localhost:8000/api/devices/"

    payload = json.dumps({
        "company": company,
        "device_id": device_id,
        "active": active,
        "labels": labels
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    return response.json()["device_id"]



def create_measurement(date=1659692787, device="QWE"):
    url = "http://localhost:8000/api/measurements/"

    sample_data = {
        "temperature": random.uniform(20, 38),
        "rssi": random.randrange(0, 50),
        "humidity": random.uniform(0, 100)
    }

    payload = json.dumps({
        "date": date,
        "device": device,
        "data": sample_data
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    company_1 = create_company(name="apple")
    company_2 = create_company(name="google")
    company_3 = create_company(name="microsoft")

    device_1 = create_device(company=company_1)
    device_2 = create_device(company=company_2, device_id="POI", labels=["big4"])
    device_3 = create_device(company=company_2, device_id="LKJ", labels=["big4", "trick"])
    device_4 = create_device(company=company_2, device_id="MMMM", labels=None)
    
    create_measurement(device=device_1)
    create_measurement(date=1659693887, device=device_1)
    create_measurement(date=1659793000, device=device_1)

    create_measurement(date=1659695111, device=device_2)
    create_measurement(date=1659699999, device=device_2)
