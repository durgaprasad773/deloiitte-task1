import json
from datetime import datetime

def convert_iso_to_milliseconds(iso_timestamp):
    """
    Convert an ISO timestamp to milliseconds timestamp.
    
    Args:
        iso_timestamp (str): The ISO format timestamp.
        
    Returns:
        int: The timestamp in milliseconds.
    """
    # Parse the ISO timestamp to a datetime object
    iso_datetime = datetime.fromisoformat(iso_timestamp)
    
    # Convert the datetime object to a Unix timestamp in milliseconds
    milliseconds_timestamp = int(iso_datetime.timestamp() * 1000)
    
    return milliseconds_timestamp

def convert_data(data):
    """
    Convert data from ISO format to milliseconds format.
    
    Args:
        data (list): A list of data entries in ISO format.
        
    Returns:
        list: A list of data entries with timestamps in milliseconds format.
    """
    converted_data = []
    
    for entry in data:
        entry['timestamp'] = convert_iso_to_milliseconds(entry['timestamp'])
        converted_data.append(entry)
    
    return converted_data

# Read the input data from data-1.json
with open("data-1.json", "r") as file:
    data_1 = json.load(file)

# Convert the data to milliseconds format
converted_data_1 = convert_data(data_1)

# Save the converted data to data-result.json
with open("data-result.json", "w") as file:
    json.dump(converted_data_1, file, indent=2)

