#!/usr/bin/python3
# coding=utf-8

import xml.sax
import os

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.currentdata = tag
        if tag == 'movie':
            print("***************Movie****************")
            title = attributes['title']
            print("Title:", title)

    def endElement(self, tag):
        print("*" * 20 , "ending element", "*"*20)
        if self.currentdata == 'type':
            print("Type :", self.type)
        elif self.currentdata == 'format':
            print("Format :", self.format)
        elif self.currentdata == 'year':
            print("Year :", self.year)
        elif self.currentdata == 'rating':
            print("Rating: ",self.rating)
        elif self.currentdata == 'stars':
            print("Stars :",self.stars)
        elif self.currentdata == 'description':
            print("Description:", self.description)
        self.currentdata = "";

    def characters(self, content):
        print("*" * 20 , "characters element", "*"*20)
        if self.currentdata == 'type':
            self.type = content
        elif self.currentdata == 'format':
            self.format = content
        elif self.currentdata == 'year':
            self.year = content
        elif self.currentdata == 'rating':
            self.rating = content
        elif self.currentdata == 'stars':
            self.stars = content
        elif self.currentdata == 'description':
            self.description = content

if __name__ == "__main__":
    # create XML Reader
    parser = xml.sax.make_parser();
    # close namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # rewrite handler
    parser.setContentHandler(MovieHandler())
    current = os.getcwd()
    filepath = os.path.join(current, "base", "xml", "analyse.xml")
    parser.parse(filepath)