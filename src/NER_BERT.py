from transformers import BertForTokenClassification, BertTokenizer

model = BertForTokenClassification.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

report_text = """     a 74 year old male patient ,non smoker with free PMH .
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
come to continue keytruda in our hospital .


on 14/10/2020 patient presented to daycare unit
looks well m no complain
labs were done
2nd cycle keytruda at our hospital  given as protocol
[Encounter ID] : 209321 | [Encounter Start Date] :Nov  3 2020  9:19AM | [End Date] :Nov  3 2020  3:56PM | [Create Date] :Nov  3 2020  9:29AM
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
come to continue keytruda in our hospital .


on 3/11/2020 patient presented to daycare unit
looks well; no complain
labs were done
3nd cycle keytruda at our hospital given as protocol
[Encounter ID] : 213398 | [Encounter Start Date] :Nov 25 2020  8:53AM | [End Date] :Nov 25 2020  4:06PM | [Create Date] :Nov 25 2020  4:06PM
          acase of metastatic mesothelioma
FOR KEYTRUDA
[Encounter ID] : 217066 | [Encounter Start Date] :Dec 16 2020  9:19AM | [End Date] :Dec 16 2020  4:43PM | [Create Date] :Dec 16 2020  3:56PM
          a case of metastatic mesothelioma
C5 KEYTRUDA
TO F/U CLINIC
[Encounter ID] : 220601 | [Encounter Start Date] :Jan  5 2021  9:20AM | [End Date] :Jan  5 2021  3:28PM | [Create Date] :Jan  5 2021  9:23AM
          a case of metastatic mesothelioma
C5 KEYTRUDA
TO DO CT 
TO F/U CLINIC
[Encounter ID] : 224632 | [Encounter Start Date] :Jan 26 2021  8:31AM | [End Date] :Jan 26 2021  3:51PM | [Create Date] :Jan 26 2021  8:39AM
          a case of metastatic mesothelioma
C6 KEYTRUDA

TO DO CT waiting 
TO F/U CLINIC 

c/o cough 
no fever

cxr : NO INFILTRATIONS
[Encounter ID] : 228796 | [Encounter Start Date] :Feb 15 2021  8:54AM | [End Date] :Feb 15 2021  6:50PM | [Create Date] :Feb 15 2021  9:40AM
          a case of metastatic mesothelioma

Last CT on 3/2/2021: SD

Today C8 KEYTRUDA
[Encounter ID] : 233565 | [Encounter Start Date] :Mar  9 2021  8:46AM | [End Date] :Mar  9 2021  4:49PM | [Create Date] :Mar  9 2021  8:55AM
          a case of metastatic lung cancer to the bone
on keytruda single agent .
lact ct showed stable disease .

Seen by dr bahaa 15/2/2021 ; continue 

today for c9 keytruda as protocol
"""

import torch
# Tokenize the text
tokens = tokenizer.tokenize(report_text)

# Split the tokens into chunks of maximum sequence length
max_length = model.config.max_position_embeddings
token_chunks = [tokens[i:i + max_length - 2] for i in range(0, len(tokens), max_length - 2)]

# Perform NER inference for each chunk
for chunk in token_chunks:
    input_ids = tokenizer.convert_tokens_to_ids(chunk)
    attention_mask = [1] * len(input_ids)
    
    with torch.no_grad():
        inputs = torch.tensor([input_ids])
        masks = torch.tensor([attention_mask])
        outputs = model(inputs, attention_mask=masks)
        predictions = torch.argmax(outputs.logits, dim=2)
    
    predicted_labels = [tokenizer.convert_ids_to_tokens(pred) for pred in predictions[0].tolist()]

    # Process and post-process predicted_labels as needed

