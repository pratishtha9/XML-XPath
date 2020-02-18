from lxml import etree as  tr
import re
import sys

filename = sys.argv[1]
output=sys.argv[2] 

fobj= open(filename)
f = fobj.read()

catalog = tr.fromstring(f)
list1=[]
book_dict = {}

for book in catalog.getchildren():
    idx = book.attrib['id']      # to add the book attribute- id

    for elem in book.getchildren():
        if elem.tag in ['description','author','title','genre']:
            list1=filter(None,[l for l in re.sub("[,.;\n]","",elem.text.lower()).split(" ")] )
            for value in list1:
                if value not in book_dict:
                    book_dict[value]=[(idx,elem.tag)]
                else:
                    book_dict[value].append((idx,elem.tag))

root_index_xml = tr.Element('catalog')
for val in book_dict:
    child = tr.SubElement(root_index_xml,'keyword',word =val)
    for idx,tag in book_dict[val]:
        temp= tr.SubElement(child,'element_tag',id=idx)
        temp.text = tag
doc_root = tr.ElementTree(root_index_xml)
doc_root.write(output,xml_declaration =True,encoding ='utf-8',pretty_print = True)

# reference from https://python101.pythonlibrary.org/chapter31_lxml.html