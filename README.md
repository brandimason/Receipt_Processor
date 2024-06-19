# Receipt Processor

This is a FastAPI application that processes receipts and calculates points based on various rules.

## Running Locally

### Requirements
- Python 3.9+
- FastAPI
- Uvicorn

### Steps
1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```bash 
pip install -r requirements.txt
```
5. Start the FastAPI server:
```bash
uvicorn api:app --reload
```
<br>

### Running with Docker:
1. Build the Docker image:
```bash
docker build -t receipt-processor .
```
2. Run the Docker container:
```bash
docker run -p 8000:8000 receipt-processor
```


## Usage
Visit http://localhost:8000/docs to access the API documentation.

### Endpoints
POST /receipts/process <br>
Submit a receipt for processing.

Request JSON:
```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
    {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
    {"shortDescription": "Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
  ],
  "total": "35.35"
}
```

Response JSON:
```json
{
  "id": "some-unique-id"
}
```
<br>
<br>
GET /receipts/{id}/points <br>
Retrieve the points for a given receipt ID.

Response JSON:
```json
{
  "points": 28
}
```

<br>

### Testing
Run tests using pytest
```bash
pytest
```