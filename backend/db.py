from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Test connection
    client.server_info()
    db = client[DB_NAME]
except Exception as e:
    print(f"ERROR: Could not connect to MongoDB: {e}")
    print(f"MONGO_URI: {MONGO_URI}")
    print("Please ensure MongoDB is running and the connection string is correct.")
    raise  # Raise the error to prevent the server from starting with a broken DB

# Collections
users_col = db.users
vehicles_col = db.vehicles
telemetry_col = db.telemetry_events
