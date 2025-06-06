#!/usr/bin/env python3
"""
CSV to JSON conversion module.

This module provides functionality to read data from a CSV file and convert 
it into JSON format using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json.
    
    Args:
        csv_filename (str): The filename of the input CSV file
        
    Returns:
        bool: True if the conversion was successful, False otherwise
    """
    try:
        # Read CSV data using DictReader
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Write JSON data to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        return False
    except Exception:
        return False
