# atlassian-python-api Examples

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
 
 