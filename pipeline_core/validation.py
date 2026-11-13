import re

def validate_customer(record):
    if not re.fullmatch(r"C[0-9]{3}", record["customer_id"]):
        raise ValueError("Invalid customer ID")

    if "@" not in record["email"]:
        raise ValueError("Invalid email")

    if not re.fullmatch(r"[0-9]{6}", record["pincode"]):
        raise ValueError("Invalid pincode")

    if float(record["spend"]) < 0:
        raise ValueError("Invalid spend")

    return True