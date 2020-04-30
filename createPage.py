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

try:
    confluence = Confluence(url=confluenceURL,username=confluenceUser,password=confluencePass)
except Exception as e:
    print("Uh oh, can't connect to confluence at " + confluenceURL)
    print(e)

print("########################################################################")
print ("Looking for space : " + confluenceSpace)
status=confluence.get_space(confluenceSpace, expand='description.plain,homepage')    
if "statusCode" in status:
    if status["statusCode"] == 404:
        print("Space not found: " + confluenceSpace)
    else:
        print("Unknown error: " + status["statusCode"])
        print(status)
        exit(8)
else:
    print ("Found Space : " + confluenceSpace + " Name: " + status["name"] )

    
print("########################################################################")
pageTitle = "My Test Page"
print("Looking for page \"" + pageTitle + "\" in space " + confluenceSpace)
pageID=confluence.get_page_id(confluenceSpace, pageTitle)
if pageID is None:
    print("Page not found: " + pageTitle + " in space " + confluenceSpace)
else:
    print ("Found page : " + pageTitle + " pageID: " + str(pageID) )

    
print("########################################################################")
pageTitle = "My New Page " + str(random.randint(0,100))
print("Looking for page \"" + pageTitle + "\" in space " + confluenceSpace)
pageID=confluence.get_page_id(confluenceSpace, pageTitle)
if pageID is None:
    print("Page not found: " + pageTitle + " in space " + confluenceSpace)
    status = confluence.create_page(space=confluenceSpace,title=pageTitle, \
             body='Hello<strong>World</strong>!')
    if "id" in status:
        #print(status)
        print("Created page : " + str(status["id"]) + " title : \"" + status["title"] + "\" in space : " + status["space"]["name"])
    else:
        print("Error creating page : " + pageTitle + " in space " + confluenceSpace)
        print(status)
        exit()
else:
    print ("Found already exists : " + pageTitle + " pageID: " + str(pageID) )    
    exit()