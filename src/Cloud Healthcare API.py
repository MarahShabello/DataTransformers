import os
import requests
import pandas as pd

# Replace with your actual project ID and location
project_id = 'data-transformer-396716'
location = 'asia-south1'

# Path to the downloaded JSON key file
credentials_path = 'C:\\Users\\zaytona\\Downloads\\data-transformer-396716-5e63dc8f7f6d.json'

# Get the access token
access_token = os.popen('gcloud auth application-default print-access-token').read().strip()

# Set the API endpoint
api_url = f"https://healthcare.googleapis.com/v1/projects/{project_id}/locations/{location}/services/nlp:analyzeEntities"

# Request headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json; charset=utf-8"
}

# List of document content for analysis
document_contents = [
    """he above mentioned patient  was in his usual state of health of unlimited exercise tolerance till 4 mo prior to admission ,when he started to develop epigastric pain  , that was aching in nature, constant described as being discomfort , it was non radiating , has no relation to food intake , did not got improved by analgesics like  paracetamol or antacids nor been triggered by any factor.

epigastric discomfort lasts for days and patient has no relief .
in addition , patient noticed to have significant weight loss ( as his weight was 74 then became 63 within a period of about 4 months ) 

patient complained form early satiety and anorexia with loss of apatite.""",
    "Another document content for analysis."
    # Add more document contents here
]

# Create an empty list to hold DataFrames
dfs = []

for document_content in document_contents:
    # Request payload
    payload = {
        "nlpService": f"projects/{project_id}/locations/{location}/services/nlp",
        "documentContent": document_content
    }

    # Make the API request
    response = requests.post(api_url, json=payload, headers=headers)

    # Parse the JSON response
    response_data = response.json()

    # Extract entities from the response
    entities = response_data.get('entities', [])

    # Create a DataFrame from the extracted entities
    df = pd.DataFrame(entities)
    
    # Append the DataFrame to the list
    dfs.append(df)

# Combine DataFrames in the list using pd.concat
all_results = pd.concat(dfs, ignore_index=True)

# Specify the Excel file path
excel_file_path = 'output.xlsx'

# Export all_results DataFrame to Excel
all_results.to_excel(excel_file_path, index=False)

print(f"Data exported to '{excel_file_path}'")
