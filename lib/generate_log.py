import requests
from datetime import datetime

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

log_data = ["User logged in", "User updated profile", "Report exported"]
filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

# Open the file in write mode to write the log data
with open(filename, "w") as file:
    for entry in log_data:
        file.write(f"{entry}\n")

# Fetch data from the API and include in the log (open in append mode)
post = fetch_data()
with open(filename, "a") as file:  # Open the file in append mode
    file.write(f"Fetched Post Title: {post.get('title', 'No title found')}\n")

print(f"Log written to {filename}")
