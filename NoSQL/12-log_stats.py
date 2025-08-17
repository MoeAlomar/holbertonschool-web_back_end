#!/usr/bin/env python3
"""
12-log_stats.py
Display statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status count
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
