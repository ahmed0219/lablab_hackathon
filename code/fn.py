
import random
import json
def readjson():
    with open('../ASSETS/output.json', 'r') as json_file:
        data = json.load(json_file)
    return data    
def generate_response(prompt):
    # Read the JSON file
   
    data=readjson()
    # Assume the JSON contains a list of items, modify accordingly based on your JSON structure
    for item in data:
        if "Questions" in item and item["Questions"].lower() == prompt.lower():
            print(item.get("Answers"))
            # Return the corresponding answer if found
            return {"response":item.get("Answers"),"show":True}

    # If the question is not found
    return {"response":"as ai model i can't answer that ","show":False}



