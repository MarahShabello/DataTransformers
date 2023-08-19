import re

# Function to clean the report
def clean_report(report):
    # Remove lines with the pattern [Encounter ID] : ...
    cleaned_report = re.sub(r'\[Encounter ID\] :\s*[^\n]*\n', '', report)
    return cleaned_report

# Get input file path from the user
input_path = input("Enter the path to the input file: ")

# Read the input file
try:
    with open(input_path, 'r') as file:
        report = file.read()
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit(1)

# Clean the report
cleaned_report = clean_report(report)

# Specify the output directory
output_path = input("Enter the path to the output directory (leave empty for the current directory): ")
if not output_path:
    output_path = './'

output_file = 'cleaned_report.txt'

# Save the cleaned report
try:
    with open(output_path + output_file, 'w') as file:
        file.write(cleaned_report)
    print(f"Report cleaned and saved to '{output_path + output_file}'.")
except Exception as e:
    print(f"An error occurred while saving the cleaned report: {str(e)}")
