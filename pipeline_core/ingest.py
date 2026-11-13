import csv
import json

def read_csv(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))

def save_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)