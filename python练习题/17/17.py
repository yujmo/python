#!/usr/bin/python
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element,SubElement,ElementTree,Comment
import xlrd
from xml.dom import minidom

def printXml():
    workbook = xlrd.open_workbook("student.xls")
    sheet1 = workbook.sheet_by_index(0)
    level = 0
    root = Element('root')
    student = SubElement(root,'student')
    student.append(Comment("student's info\"id\":[name,math,chinese,english]"))

    if root:
        for child in root.getchildren():
            if child.text:
                level += 1

    xml_str_cache = sheet1.row_values(0)
    xml_str = str(xml_str_cache[1:])
    for i in range(1,sheet1.nrows):
        cache = sheet1.row_values(i) 
        xml_str = xml_str +"\n" + "\t" * (level+2) + str(cache[1:]) 

    student.text = str(xml_str)
    xml_string = etree.tostring(root)
    tree = minidom.parseString(xml_string)
    xml_string = tree.toprettyxml()
    print (xml_string)

if __name__ == '__main__':
    printXml()

