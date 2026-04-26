# lib/generate_log.py
import requests
from datetime import datetime

def generate_log(log_data=None):
    if log_data is None:
        log_data = ["User logged in", "User updated profile", "Report exported"]
    
    # Check if log_data is a list, if not, raise a ValueError
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")
    return filename  # Return the filename for potential tests
