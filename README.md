# atlassian-python-api Examples

## Things to know
### How to get page id
 * Click the page ellipsis and select Page Information
 * The page id is found in the web browser url i.e. http://192.168.1.224:8090/pages/viewinfo.action?pageId=10256402
### Hot to get macros and other confluence page source
 * Option 1, use the REST API and your browser with the page id, i.e. http://192.168.1.224:8090/rest/api/content/10256402?expand=body.storage
 * Option 2, copy and modify the included script updatePage.py to print the returned values from contents=confluence.get_page_by_id(pageID, expand="body.storage,version", status="current")

Using config.json
   ```json
{
  "confluence":"http://192.168.1.224:8090"
 ,"user":"username"
 ,"password":"password"
 ,"space":"HOME"
 ,"page":"My Test Page"
}
   ```

## createPage.py
  * Verify Space exists
  * Get Page ID by Space and Page Title
  * Create Page in Space with Page Title and return Page ID
  
## updatePage.py
  * Get Page ID by Space and Page Title
  * Get Page contents and properties by Page ID
  * Update page body and title by Page ID

## updateChart.py
  * Get Page ID by Space and Page Title
  * Generate random data for 'Internet download speeds'
  * Use confluence chart macro and html table for page body
  * Update page body and title by Page ID
  
 ![example chart output](https://github.com/rajdor/pythonConfluenceExamples/blob/master/updateChart.png?raw=true)
 
 