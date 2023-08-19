import spacy

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Sample medical report text
report_text = """    a 74 year old male patient ,non smoker with free PMH .
diagnosed since 2017 as acase of metastatic mesothelioma with obstruction of 2nd rib.
s/p carboplatin alimta
s/p gemzar ,taxol
s/p palliative radiotherapy to the chest mass .
s/p navelbine
PDL1 positive more than 80 %
started on keytruda in al najah hospital .
recieved 13 cycles .
last ct on 6/2020 showed stable disease.
come to continue keytruda in our hospital .


patient presented to daycare unit 
looks well m no complain 
labs were done 
keytruda given as protocol
[Encounter ID] : 205482 | [Encounter Start Date] :Oct 14 2020  9:29AM | [End Date] :Oct 14 2020  7:05PM | [Create Date] :Oct 14 2020  9:37AM
          a 74 year old male patient ,non smoker with free PMH .
diagnosed since 2017 as acase of metastatic mesothelioma with obstruction of 2nd rib.
s/p carboplatin alimta
s/p gemzar ,taxol
s/p palliative radiotherapy to the chest mass .
s/p navelbine
PDL1 positive more than 80 %
started on keytruda in al najah hospital .
recieved 13 cycles .
last ct on 6/2020 showed stable disease.
come to continue keytruda in our hospital """

# Process the text using spaCy's NLP pipeline
doc = nlp(report_text)

# Extract entities and their types
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the extracted entities and their types
for entity, entity_type in entities:
    print(f"Entity: {entity}, Type: {entity_type}")
