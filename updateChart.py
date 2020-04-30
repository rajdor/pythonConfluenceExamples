import json
import random
import datetime 
#https://pypi.org/project/atlassian-python-api/
#https://atlassian-python-api.readthedocs.io/
from atlassian import Confluence

####################################################################################
print ("Importing config")
input_file = open ('config.json')
c = json.load(input_file)

confluenceURL=c["confluence"]
confluenceUser=c["user"]
confluencePass=c["password"]
confluenceSpace=c["space"]
confluencePage=c["page"]

####################################################################################
print ("Connecting to Confluence : " + confluenceURL)
try:
    confluence = Confluence(url=confluenceURL,username=confluenceUser,password=confluencePass)
except Exception as e:
    print("Uh oh, can't connect to confluence at " + confluenceURL)
    print(e)
    
    
####################################################################################
print ("Generating sample data")
records = []
today = datetime.datetime.today()
numdays = 30
for i in range (0, numdays):
    d1=today - datetime.timedelta(days = i)
    records.append({"date": d1.strftime("%Y.%m.%d"), "downloadspeed":random.randint(70,120)})

    
####################################################################################
print ("Making body")
chartHeading = "Download Speeds last " + str(numdays) + " days"
bodyPart_1 = ""
bodyPart_2 = "" 
bodyPart_3 = ""     

bodyPart_1 = bodyPart_1 + "<ac:structured-macro ac:name=\"chart\" ac:schema-version=\"1\" ac:macro-id=\"03427ec1-7dcf-4b60-a195-3c0b80e63ae7\">"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"timeSeries\">true</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"orientation\">vertical</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"dataDisplay\">after</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"showShapes\">false</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"dateFormat\">yyyy/MM/dd</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"timePeriod\">Second</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"width\">800</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"dataOrientation\">vertical</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"title\">" + chartHeading + "</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:parameter ac:name=\"type\">timeSeries</ac:parameter>"
bodyPart_1 = bodyPart_1 + "  <ac:rich-text-body>"
bodyPart_1 = bodyPart_1 + "      <table class=\"wrapped\">"
bodyPart_1 = bodyPart_1 + "          <colgroup><col /><col /><col /></colgroup>"
bodyPart_1 = bodyPart_1 + "      <tbody><tr><th>Date</th><th>" + chartHeading + "</th></tr>"

for r in records:
    bodyPart_2 = bodyPart_2 + "\n                 <tr><td><div class=\"content-wrapper\"><p>" + str(r["date"]) + "</p></div></td><td>" + str(r["downloadspeed"]) + "</td></tr>"

bodyPart_3 = "      </tbody></table></ac:rich-text-body></ac:structured-macro>"

newBody = bodyPart_1 + bodyPart_2 + bodyPart_3


print("########################################################################")
print("Looking for page \"" + confluencePage + "\" in space " + confluenceSpace)
pageID=confluence.get_page_id(confluenceSpace, confluencePage)
if pageID is None:
    print("Page not found: " + confluencePage + " in space " + confluenceSpace)
    exit()
else:
    print ("Found page : " + confluencePage + " pageID: " + str(pageID) )
    

print("########################################################################")
print("Updating page: " + str(pageID))
try:
    status=confluence.update_page(pageID, confluencePage, newBody, parent_id=None, type='page', representation='storage', minor_edit=False)
    #print (status)
except Exception as e:
    print("Uh oh, can't update pageID " + str(pageID))
    print("Makesure page exists")
    traceback.print_exc()   
    exit()
