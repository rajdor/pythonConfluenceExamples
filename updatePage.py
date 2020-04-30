import json
import random
#https://pypi.org/project/atlassian-python-api/
#https://atlassian-python-api.readthedocs.io/
from atlassian import Confluence

input_file = open ('config.json')
c = json.load(input_file)

confluenceURL=c["confluence"]
confluenceUser=c["user"]
confluencePass=c["password"]
confluenceSpace=c["space"]
confluencePage=c["page"]

try:
    confluence = Confluence(url=confluenceURL,username=confluenceUser,password=confluencePass)
except Exception as e:
    print("Uh oh, can't connect to confluence at " + confluenceURL)
    print(e)
   
print("########################################################################")
print("Looking for page \"" + confluencePage + "\" in space " + confluenceSpace)
pageID=confluence.get_page_id(confluenceSpace, confluencePage)
if pageID is None:
    print("Page not found: " + confluencePage + " in space " + confluenceSpace)
    exit()
else:
    print ("Found page : " + confluencePage + " pageID: " + str(pageID) )
    
print("########################################################################")
print("Getting page by ID: " + str(pageID))
contents=confluence.get_page_by_id(pageID, expand="body.storage,version", status="current")
print("ID           : " + str(contents["id"]))
print("Status       : " + contents["status"])
print("Title        : " + contents["title"])
print("Version      : " + str(contents["version"]["number"]))
print("Last Updated : " + str(contents["version"]["when"]))
print("Body         : " + contents["body"]["storage"]["value"])
#print("Full Contents:")
#print(contents)

print("########################################################################")
print("Update page: " + str(pageID))
newBody="<p>Hello World " + str(random.randint(0,100)) + "</p>"
try:
    status=confluence.update_page(pageID, confluencePage, newBody, parent_id=None, type='page', representation='storage', minor_edit=False)
    #print (status)
except Exception as e:
    print("Uh oh, can't update pageID " + str(pageID))
    print("Makesure page exists")
    traceback.print_exc()   



 