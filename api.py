# end points
from fastapi import FastAPI, HTTPException
from models import Receipt
from app import store_receipt, receipt_storage, calculate_points


app = FastAPI()

# POST
@app.post("/receipts/process")
def save_receipt(receipt: Receipt):
    receipt_id = store_receipt(receipt)
    return {"id": receipt_id,}

@app.get("/receipts/{id}/points")
def get_points(id: str):
    receipt = receipt_storage.get(id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")

    points = calculate_points(receipt)
    return {"points": points}