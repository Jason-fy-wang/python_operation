from lxml import etree
import os

current = os.getcwd()
filepath = os.path.join(current, "base", "xml", "analyse.xml")
destpath = os.path.join(current, "base", "xml", "dest.xml")

with open(filepath) as file:
    content = file.read()

## parse content
tree = etree.fromstring(content)

## get field and methods
print(dir(tree))

## find all 'movie' node
movies = tree.findall("movie")
print(dir(movies[0]))
for m in movies:
    print(f"tag: {m.tag}, text: {m.text}, ")


## find node with xpath
trans = tree.xpath("//movie[@title='Transformers']")[0]
print(f"trans tag: {trans.tag}, attributs: {trans.attrib}")

## update trans node value
trans.attrib.update({"title":"transformer from soup"})

## print final xml content
result = etree.tounicode(tree)
print(f"result: {result}")


