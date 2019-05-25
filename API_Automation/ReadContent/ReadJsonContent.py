import json

def read_request_content():
    file=  open('C:/Z-Udhayakumar/IOT/Automation_Projects/InputData/Request.json','r')
    jsonfile=file.read()
    json_content=json.loads(jsonfile)
    return json_content


