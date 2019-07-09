# JsonToXML

A module to convert JSON to XML format.

# Details

The module contains functions to convert a JSON File/String to an XML File/String. In case the XML is to be processed further, the pointer root node containing the XML data can also be returned using the specific function.

The module has following functions:

Function | Description
-------- | -----------
fromFile( filename [, rootName ]) | Takes JSON data from the specified filename and returns the root pointer.
fromText( text [, rootName ]) | Takes JSON data in form of a string and returns the root pointer.
fromFiletoFile( inputFile, outputFile [, rootName ]) | Takes JSON data from the specified inputFile and writes the XML data to the specified outputFile.
fromTexttoFile( text, outputFile [, rootName ]) | Takes JSON data in form of a string and writes the XML data to the specified outputFile.
fromFiletoText( inputFile [, rootName ]) | Takes JSON data from the specified inputFile and returns the XML data in form of a string.
fromTexttoText( text [, rootName ]) | Takes JSON data in form of a string and returns the XML data as a string.

**Note:** The root node of the XML data is by default "root", but can be specified by passing the argument 
`rootName = "Custom Name"` to the function.

**This Module works well with Python 3**

# Installation

The module can be installed using the pip command:

    pip install JsonToXML

# Usage

The usage of Module is pretty simple, you have to just import the library and use the functions directly.

### fromFile( file [, rootName ] )

	import JsonToXML
	import xml.etree.cElementTree as ET
	import xml.dom.minidom
	root = JsonToXML.fromFile("example.json", rootName="Employees") # convert the file to XML and return the root node
	xmlData = ET.tostring(root, encoding='utf8',method='xml').decode() # convert the XML data to string
	dom = xml.dom.minidom.parseString(xmlData) 
	prettyXmlData = dom.toprettyxml() # properly format the string of XML data
	print(prettyXmlData) # print the formatted XML data

The above program reads JSON data from a file and *pretty prints* (With proper Indentation and line breaks) XML data on the screen.

### fromText( text [, rootName ] )

	import JsonToXML
	import xml.etree.cElementTree as ET
	import xml.dom.minidom
	exampleJSON = "{ 'employee': { 'name':'sonoo', 'salary':56000, 'married':true } }"
	root = JsonToXML.fromText(exampleJSON) # convert the string to XML and return the root node
	xmlData = ET.tostring(root, encoding='utf8',method='xml').decode() # convert the XML data to string
	dom = xml.dom.minidom.parseString(xmlData) 
	prettyXmlData = dom.toprettyxml() # properly format the string of XML data
	print(prettyXmlData) # print the formatted XML data

The above program reads JSON from a string and prints the XML data on the screen.

### fromFiletoFile( inputFile, outputFile [, rootName ] )

	import JsonToXML
	JsonToXML.fromFiletoFile("example1.json","example2.xml") # converts the JSON data from the file to XML and writes it on the XML file.

The above program simply converts the JSON data from the inputFile and writes XML data to the outputFile.

### fromTexttoFile( text, outputFile [, rootname ] )

	import JsonToXML
	exampleJSON = "{ 'employee': { 'name':'sonoo', 'salary':56000, 'married':true } }"
	JsonToXML.fromFiletoFile(exampleJSON,"example2.xml") # converts the JSON data from the string to XML and writes it on the XML file.

The above program simply converts the JSON data from the string and writes XML data to the outputFile.

### fromFiletoText( inputFile [, rootName ] )

	import JsonToXML
	xmlData = JsonToXML.fromFiletoText("example1.json") # converts the JSON data from the file to XML and returns string of XML data.
	print(xmlData)

The above program reads JSON data from a file and returns a formatted string of XML data.

### fromTexttoText( inputFile [, rootName ] )

	import JsonToXML
	exampleJSON = "{ 'employee': { 'name':'sonoo', 'salary':56000, 'married':true } }"
	xmlData = JsonToXML.fromTexttoText(exampleJSON) # converts the JSON data from the string to XML and returns string of XML data.
	print(xmlData)

The above program reads JSON data from a string and returns a formatted string of XML data.

# Author

* Author: Bhavyadeep Purswani
* E-Mail: bhavyadeep.purswani98@gmail.com
* Repository: https://github.com/bhavyadeep-purswani/JsonTOXML