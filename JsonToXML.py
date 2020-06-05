import xml.etree.cElementTree as ET
import json
import xml.dom.minidom


def _addSubList(root,key1,data):

        subroot = None
        for key in range(len(data)):
            if type(data[key]) in (dict,):
                subroot=ET.SubElement(root,str(key))
                _addSubDict(subroot,data[key])
                continue
            if type(data[key]) in (list,):
                subroot=ET.SubElement(root,str(key))
                _addSubList(subroot,key1,data[key]) 
                continue
            ET.SubElement(root,str(key)).text=str(data[key])

        

def _addSubDict(root,data): 
    subroot = None
    for key in data:
        if type(key) == str and key[0] == "@" and len(key) > 1:
            root.set(key[1:], data[key])
        else:
            if type(data[key]) in (dict,):
                subroot=ET.SubElement(root,str(key)) 
                _addSubDict(subroot,data[key])
                continue
            if type(data[key]) in (list,):
                subroot=ET.SubElement(root,str(key))
                _addSubList(subroot,key,data[key]) 
                continue
            ET.SubElement(root,str(key)).text=str(data[key])


def _jsontoxml(dictionary,rootName="root"):
    root=ET.Element(rootName)
    _addSubDict(root,dictionary)
    return root


def fromFile(file,rootName="root"):
    data=json.loads(open(file,"r").read())
    root=_jsontoxml(data,rootName)
    return root


def fromText(text,rootName="root"):
    data=json.loads(text)
    root=_jsontoxml(data,rootName)
    return root


def fromFiletoFile(inputFile,outputFile,rootName="root"):
    data=json.loads(open(inputFile).read())
    root=_jsontoxml(data,rootName)
    tree = ET.ElementTree(root)
    tree.write(outputFile, encoding='utf-8', xml_declaration=True)
    return None


def fromTexttoFile(text,outputFile,rootName="root"):
    data=json.loads(text)
    root=_jsontoxml(data,rootName)
    tree = ET.ElementTree(root)
    tree.write(outputFile, encoding='utf-8', xml_declaration=True)
    return None


def fromFiletoText(inputFile,rootName="root"):
    data=json.loads(open(inputFile).read())
    root=_jsontoxml(data,rootName)
    s=ET.tostring(root, encoding='utf8', method='xml').decode()
    dom = xml.dom.minidom.parseString(s)
    s = dom.toprettyxml()
    return s


def fromTexttoText(text,rootName="root"):
    data=json.loads(text)
    root=_jsontoxml(data,rootName)
    s=ET.tostring(root, encoding='utf8', method='xml').decode()
    dom = xml.dom.minidom.parseString(s)
    s = dom.toprettyxml()
    return s