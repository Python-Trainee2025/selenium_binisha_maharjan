"""

ID (find_element(By.ID, "element_id"))
Name (find_element(By.NAME, "element_name"))
Class Name (find_element(By.CLASS_NAME, "class_name"))
Tag Name (find_element(By.TAG_NAME, "tag_name")) ,input>
Link Text / Partial Link Text (find_element(By.LINK_TEXT, "link text"))
CSS Selectors (find_element(By.CSS_SELECTOR, "css_selector"))
XPath (find_element(By.XPATH, "//tagname[@attribute='value']"))

xpath::

//{tag}[@attribute='']
//{tag}[contains(@attribute,'value')]
eg: //div//input[@data-test='{user}']
//div//input[contains(@data-test,'username')]
parameterization
"""