import csv
from datetime import datetime
import os

def convert_to_month_date(record):
    try:
        # Explicit conversion for 'Jun-00' to '6.0'
        if record == 'Jun-00':
            return '6.0'

        # Explicit conversion for 'Jul-00' to '7.0'
        elif record == 'Jul-00':
            return '7.0'

        # Try parsing the record as a date
        date_obj = datetime.strptime(record, '%b-%d')
        # If successful, return the month and day as numbers in the format 'month.date'
        day = date_obj.day
        month = date_obj.month

        # Explicit conversion for '00' to '0'
        if day == 0:
            day_str = '0'
        else:
            day_str = str(day)

        return f"{month}.{day_str}"
    except ValueError:
        # If parsing fails, return the original record
        return record

def process_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Process each record in the row
            modified_row = [convert_to_month_date(record) if '-' in record else record for record in row]
            writer.writerow(modified_row)

# Get the absolute path to the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV files
input_csv = os.path.join(script_directory, 'newHeight.csv')
output_csv = os.path.join(script_directory, 'newnew.csv')

process_csv(input_csv, output_csv)
