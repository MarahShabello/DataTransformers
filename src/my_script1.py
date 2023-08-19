import spacy

# Load spaCy model (you can use a more specialized medical model if available)
nlp = spacy.load("en_core_web_sm")

# Clinical report
report = """
70 years old female.
FH negative
PMH free

Diagnosis breast ca
... (rest of the report)
"""

# Process the report with spaCy
doc = nlp(report)

# Extract patient demographics (age, gender) using custom rule-based parsing
for sent in doc.sents:
    if "years old" in sent.text:
        print("Patient Age:", sent.text.split(" years old")[0])
    if "female" in sent.text.lower():
        print("Patient Gender: Female")

# Extract medical conditions and diagnoses
for ent in doc.ents:
    if ent.label_ in ["DISEASE", "DIAGNOSIS"]:
        print("Diagnosis:", ent.text)

# Extract medications (rule-based)
medications = []
for sent in doc.sents:
    if "ON " in sent.text:
        medications.append(sent.text)
print("Medications:", medications)

# Extract procedures (rule-based)
procedures = []
for sent in doc.sents:
    if "Plan :" in sent.text:
        procedures.append(sent.text.split("Plan :")[1].strip())
print("Procedures:", procedures)

# Additional parsing based on specific patterns and keywords
# ...

# Note: This is a simplified example and may require fine-tuning based on the actual report format and data.
