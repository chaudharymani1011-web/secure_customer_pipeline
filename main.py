import logging
from pathlib import Path
from pipeline_core.ingest import read_csv, save_json
from pipeline_core.validation import validate_customer
from pipeline_core.security import safe_path, calculate_hash

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO
)

# Create sample customer data
with open("customers.csv", "w", newline="") as file:
    import csv
    writer = csv.DictWriter(
        file,
        fieldnames=["customer_id", "email", "pincode", "spend"]
    )
    writer.writeheader()
    writer.writerow({
        "customer_id": "C101",
        "email": "student@gmail.com",
        "pincode": "110001",
        "spend": "500.0"
    })

# Read and validate data
records = read_csv("customers.csv")
valid_records = []

for record in records:
    try:
        validate_customer(record)
        record["email"] = record["email"].strip().lower()
        valid_records.append(record)
        logging.info("Record validated")
    except ValueError as error:
        logging.error(str(error))

# Save output
Path("output").mkdir(exist_ok=True)
output_file = safe_path("output", "customers.json")
save_json(valid_records, output_file)

# Generate SHA-256 checksum
print("Valid records:", len(valid_records))
print("SHA-256:", calculate_hash(output_file))
print("Pipeline completed successfully!")