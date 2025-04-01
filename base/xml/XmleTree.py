import xml.etree.ElementTree as ET
import os

current = os.getcwd()
filepath = os.path.join(current, "base", "xml", "analyse.xml")
destfile = os.path.join(current, "base", "xml", "dest.xml")
print(filepath)

## parse xml file
tree = ET.parse(filepath)

## get root node
root = tree.getroot()
print(f"root is {root.tag}")
## find node 
for item in root.iter("movie"):
    print(f"tag: {item.tag}, text: {item.text},title: {item.attrib}")

# get sibling node of '<movie title="Enemy Behind">'
movie = root.find(".//movie[@title='Enemy Behind']")
print(f"tag: {movie.tag}, title: {movie.attrib.get('title')}")

## update movie's attribute and child's text
movie.attrib.update({"title":"update1"})


## print all content or write to files
result = ET.tostring(root, encoding="unicode")
print(f"result = {result}")

### write to new file
tree.write(destfile,method="xml")

