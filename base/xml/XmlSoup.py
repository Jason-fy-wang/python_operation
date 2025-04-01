from bs4 import BeautifulSoup
import os

current = os.getcwd()
filepath = os.path.join(current, "base", "xml", "analyse.xml")
destfile = os.path.join(current, "base", "xml", "dest.xml")

# get file content
with open(filepath, "r")  as file:
    content = file.read()

## parse file content
soup = BeautifulSoup(content, features="lxml-xml")

## find all movie node
items = soup.find_all("movie", {"title": "Transformers"})

for item in items: 
    #print(dir(item))   # inspect the fields and methods
    print(f"tag: {item.name}, text: {item.text}, attrs: {item.attrs} ")
print("*" * 50)
## find sibling node
node = items[0]
nextnode = node.find_next_sibling()
print(f"next_node: {nextnode.name}, text: {nextnode.text}, attrs: {nextnode.attrs}")

print("*" * 20, "encoding to string ", "*" * 20)
## dump to string
result = soup.decode_contents()
print(result)
