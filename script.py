import argparse
import csv
import re
import os

def main():
    # Parse arguments (Takes in options and Arguments and has -h argument)
    parser = argparse.ArgumentParser(description="Clean up data from a CSV file")
    parser.add_argument("input_file", help="File path to the input CSV")
    parser.add_argument("output_file", help="File path to the output CSV")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Convert data to lowercase")
    parser.add_argument("-o", "--organize", action="store_true", help="Organize data from A-Z")
    args = parser.parse_args()

    # Validate file paths are CSV format (Uses a Regular expression)
    if not re.match(r'.*\.csv$', args.input_file) or not re.match(r'.*\.csv$', args.output_file):
        print("Error: Input and output files must be in CSV format.")
        return

    # Check if file exists (Handles invalid arguments)
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    # Read from CSV
    try:
        with open(args.input_file, 'r', newline='', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            header = next(reader)  # Assuming the first row is the header
            rows = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    # Clean up
    cleaned_rows = []

    # Apply changes (Changes output based on provided args)
    if args.lowercase:
        cleaned_rows = [[cell.lower() for cell in row] for row in rows]

    # Organize A-Z (Changes output based on provided args)
    if args.organize:
        cleaned_rows = [row for row in cleaned_rows if row]
        cleaned_rows.sort(key=lambda x: x[0])  # Assuming the first column contains names

    # Write to CSV
    try:
        with open(args.output_file, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerows(cleaned_rows)
    except PermissionError:
        print(f"Error: Permission denied to write to '{args.output_file}'.")
        return

if __name__ == "__main__":
    main()
