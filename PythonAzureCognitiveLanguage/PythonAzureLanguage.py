import json, requests, os

#Read from config JSON file for URL & Key for Azure text analytics or translator
#Can be replaced by Azure Cognitive URLs & Keys respectively 
file=open("c:/BhaskarWD/BhaskarCode/access.json")
accessdata=json.load(file)
TEXTANALYTICS_URL = accessdata["TEXT"]["BASE_URL"]
TEXTANALYTICS_KEY= accessdata["TEXT"]["Key"]
TRANSLATOR_URL = accessdata["TRANSLATE"]["BASE_URL"]
TRANSLATOR_KEY= accessdata["TRANSLATE"]["Key"]

#Select if Azure Text Analytics or Translation API to be used
API_Choice = input ('Select Text(A)nalytics or Text(T)ranslation ?-:')

#Code for language translation
if API_Choice== 'T':
    TargetLang= input('Enter target language German(de)/Italian(it) :-')
    Final_Url = TRANSLATOR_URL+'&to='+TargetLang
    headers   = {"Ocp-Apim-Subscription-Key": TRANSLATOR_KEY}
    
    #content preparation - read from console or from file 
    contentoption = input("Enter console text or read from file C / F :-")
    if contentoption == "C":
        text=input("Enter console text here :-  ")
        documents = [{'text': text }]
    else:
        contentfile=input("Enter filepath with forward / here :-  ")
        file=open(contentfile)
        id=0
        jsonarray = []
        for lines in file.readlines():
            id = id +1
            text = {'text': lines }
            jsonarray.append (text)
            documents = jsonarray

#Code for text analytics API call 
else:
    #Append choice of Azure language API languages / sentiment / keyphrases / entities & build URL & key
    URL_EXT = input('Chose languages / sentiment / keyphrases / entities:- ')
    Final_Url=TEXTANALYTICS_URL+URL_EXT
    headers   = {"Ocp-Apim-Subscription-Key": TEXTANALYTICS_KEY}
    #content preparation - read from console or from file 
    contentoption = input("Enter console text or read from file C / F :-")
    if contentoption == "C":
        text=input("Enter console text here :-  ")
        documents = { 'documents': [{ 'id': '1', 'text': text }]}
    else:
        contentfile=input("Enter filepath with forward / here :-  ")
        file=open(contentfile)
        id=0
        jsonarray = []
        for lines in file.readlines():
            id = id +1
            text = { 'id': id, 'text': lines }
            jsonarray.append ( text)
            documents = { 'documents': jsonarray}

print (json.dumps(documents,indent=4))
response  = requests.post(Final_Url, headers=headers, json=documents)
languages = response.json()
print (json.dumps(languages,indent=4))

