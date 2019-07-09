# JsonToXML

A library to convert JSON to XML format.

# Details

The library contains functions to convert a JSON File/String to an XML File/String. In case the XML is to be processed further, the pointer root node containing the XML data can also be returned using the specific function.

The library has following functions:

Function | Description
-------- | -----------
fromFile( filename [, rootname ]) | Takes JSON data from the specified filename and returns the root pointer.
