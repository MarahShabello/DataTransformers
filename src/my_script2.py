import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download necessary resources (if required)
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_entities_spacy(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_entities_nltk(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    ne_tree = ne_chunk(tagged)
    entities = []
    for subtree in ne_tree:
        if isinstance(subtree, nltk.Tree):
            entity = " ".join([word for word, tag in subtree.leaves()])
            entities.append((entity, subtree.label()))
    return entities

# Sample medical report
medical_report = """
"[Encounter ID] : 243607 | [Encounter Start Date] :Apr 30 2021 11:03AM | [End Date] :May  8 2021 10:23AM | [Create Date] :
          Surgical Pathology Cancer Case SummaryProcedure: High anterior resection.Tumor site: Rectosigmoid tumor.Tumor size: 13x5 cm.Macroscopic tumor perforation: Not identified.Histologic type: Adenocarcinoma.Histologic grade: G2: Moderately differentiated.Tumor extension: Tumor invades through the muscularis propria into pericolic tissue. Margins*Proximal margin: Uninvolved by invasive carcinoma, high grade dysplasia / intramucosal carcinoma, and low grade dysplasia.*Distal margin: Uninvolved by invasive carcinoma, high grade dysplasia / intramucosal carcinoma, and low grade dysplasia.     Treatment effect: No known presurgical therapy.Lymphovascular invasion: Not identified.Perineural invasion: Not identified.Type of polyp in which invasive carcinoma arose: Not identified.Tumor deposits: Not identified.Regional lymph nodes:*Number of lymph nodes involved: 0*Number of lymph nodes examined: 15Pathologic stage classification (pTNM, AJCC 8th Edition):*Primary tumor (pT): pT3: Tumor invades through the muscularis propria into pericolorectal tissues*Regional lymph nodes (pN): pN0: No regional lymph node metastasisAdditional pathology: Transmural severe acute inflammation.Final diagnosis:1-Rectosigmoid tumor, high anterior resection:   Invasive moderately differentiated adenocarcinoma, pT3N0.2- Distal donut; biopsy:    Unremarkable colonic wall tissue."

"""

# Extract entities using spaCy
entities_spacy = extract_entities_spacy(medical_report)
print("Entities extracted using spaCy:")
print(entities_spacy)

# Extract entities using NLTK
entities_nltk = extract_entities_nltk(medical_report)
print("Entities extracted using NLTK:")
print(entities_nltk)
