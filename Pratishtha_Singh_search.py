from lxml import etree as  tr

import sys

filename1 = sys.argv[1]

filename2=sys.argv[2]

output=sys.argv[4] 



f1 = open(filename1)

f2 = open(filename2)

key_name=sys.argv[3]
list3=['a','the','in','of']
list2=[]

dictionary = dict()

dictionary2 = dict()

parse_file1 = tr.parse(f1)

parse_file2 = tr.parse(f2)

list2=key_name.split(" ")

list2=[x.lower() for x in list2]



i=0

for values in list2:

    i+=1

    p = parse_file2.xpath('//keyword[@word="{}"]'.format(values))                

    if len(p)!=0:

        k=p[0].attrib['word']    

    p1=parse_file2.xpath('//keyword[@word="{}"]/element_tag'.format(values))

    

    for val in p1:

        if val.attrib['id'] not in dictionary:

                dictionary[val.attrib['id']] = [(val.text)]

        else:
            if k in list3:
                if val.text in dictionary[val.attrib['id']]:
                    j=1
            else:
                dictionary[val.attrib['id']].append((val.text))  



for keys in dictionary:  

    for val in dictionary[keys]:

        if dictionary[keys].count(val) >= i:

            if keys not in dictionary2:

                dictionary2[keys] = [val]

            else:

                 if val not in dictionary[keys]:

                    dictionary2[keys].append(val)



                    

                                   

if i is 1:

    output_xml=tr.Element('results')

    for a in dictionary:

        t=tr.SubElement(output_xml,'book',id=a)

        for b in dictionary[a]:

            p3= parse_file1.xpath('//book[@id="{}"]/{}'.format(a,b))

            for val1 in p3:

                tr.SubElement(t,val1.tag).text = val1.text

    

    

    

else:

    

    if len(dictionary2)==0:

        output_xml=tr.Element('results')

       

       

    else:

        output_xml=tr.Element('results')

        for a in dictionary2:

            t=tr.SubElement(output_xml,'book',id=a)

            for b in dictionary2[a]:

                p3= parse_file1.xpath('//book[@id="{}"]/{}'.format(a,b))

                for val1 in p3:

                    tr.SubElement(t,val1.tag).text = val1.text

        

doc_root = tr.ElementTree(output_xml)

doc_root.write(output,xml_declaration =True,encoding ='utf-8',pretty_print = True)        

