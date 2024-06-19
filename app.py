# logic - this is where I make a call to the endpoints
from models import Receipt
from uuid import uuid4
from datetime import datetime
import math

receipt_storage = {}

# store receipt
def store_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    receipt_storage[receipt_id] = receipt
    return receipt_id

# total points
def calculate_points(receipt: Receipt):
    points = 0
    retailer = receipt.retailer
    total = float(receipt.total)
    items = receipt.items
    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")

    # Rule 1: 1 point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in retailer)

    # Rule 2: 50 points if the total is a round dollar amount with no cents
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt
    points += (len(items) // 2) * 5

    # Rule 5: Item description length is a multiple of 3
    for item in items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    # Rule 6: 6 points if the day in the purchase date is odd
    if purchase_date.day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the time of purchase is between 2:00pm and 4:00pm
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points