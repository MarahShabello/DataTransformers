import os
import requests
import json

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
    """
    # ... (document content here) ...
    """,
    "Another document content for analysis."
    # Add more document contents here
]

# Create a directory to save JSON files
json_output_dir = 'json_output'
os.makedirs(json_output_dir, exist_ok=True)

for idx, document_content in enumerate(document_contents, start=1):
    # Request payload
    payload = {
        "nlpService": f"projects/{project_id}/locations/{location}/services/nlp",
        "documentContent": document_content
    }

    # Make the API request
    response = requests.post(api_url, json=payload, headers=headers)

    # Parse the JSON response
    response_data = response.json()

    # Save the response data as a JSON file
    json_output_path = os.path.join(json_output_dir, f"document_{idx}_response.json")
    with open(json_output_path, 'w') as json_file:
        json.dump(response_data, json_file, indent=2)

    print(f"Response Data for Document {idx} saved to '{json_output_path}'")
import os
import requests
import json

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
    """
    70 years old female.
FH negative
PMH free

Diagnosis breast ca
Due to breast mass 2019 follow up was done

Biopsy IDC ER,PR POSITIVE,HER-2 NGATIVE
PET-CT was done bone mets
ON letrozole 2019 - 02/2023
PET-CT 02/2023 DP n the breast, bone, axillary L.N

Pt came from Gaza for KISQALI AND FASLODEX

O/E LT breast mass with mass with axillary L.N

Seen By Dr. Feras on 11/4, planned for : kisqali with faslodex
CT and TM
evaluation after 2 month

Oncology CT 11/4/2023 : Thoracic T5 and T6 spinal cord compression 
Clinically , the patient has mild upper limbs parathesis. 
O/E: Unremarkable 

Plan :
Admission Regular Diet
DECORT 4 mg 1*2 IV 
NEXIUM 40 mg *1 IV
KISQALI as protocol 
Please do Urgent  Neurosurgery consultation and manage SCC accordingly 

          SPINE MRI DONE AND SEEN BY NEUROSURGERY TEAM 
 THEY REPORTED THAT THERE'S NO SPINAL CORD COMPRESSION 
AND BEST TREATMENT FOR HER IS RADIOTHERAPY , 
AND TO RETURN BACK TO NEUROSURGERY CLINIC FOR BETTER EVALUATION
          &#x0D;
 Subjective Notes:&#x0D;
&#x0D;
Chief Complaints:&#x0D;
Presented for evaluation with CT oncology 

    """,

]

# Create a directory to save JSON files
json_output_dir = 'json_output'
os.makedirs(json_output_dir, exist_ok=True)

for idx, document_content in enumerate(document_contents, start=1):
    # Request payload
    payload = {
        "nlpService": f"projects/{project_id}/locations/{location}/services/nlp",
        "documentContent": document_content
    }

    # Make the API request
    response = requests.post(api_url, json=payload, headers=headers)

    # Parse the JSON response
    response_data = response.json()

    # Save the response data as a JSON file
    json_output_path = os.path.join(json_output_dir, f"document_{idx}_response.json")
    with open(json_output_path, 'w') as json_file:
        json.dump(response_data, json_file, indent=2)

    print(f"Response Data for Document {idx} saved to '{json_output_path}'")
