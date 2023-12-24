
import random
import json
def readjson():
    with open('../ASSETS/output.json', 'r') as json_file:
        data = json.load(json_file)
    return data    
def generate_response(prompt):
   
   
    data=readjson()
   
    for item in data:
        if "Questions" in item and item["Questions"].lower() == prompt.lower():
            print(item.get("Answers"))
            
            return {"response":item.get("Answers"),"show":True}

   
    return {"response":"as ai model i can't answer that ","show":False}



