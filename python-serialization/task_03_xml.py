#!/usr/bin/env python3
"""
XML serialization and deserialization module.

This module provides functionality to serialize a Python dictionary to XML
format and deserialize XML data back to a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to file.
    
    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to
    """
    try:
        # Create root element
        root = ET.Element("data")
        
        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create tree and write to file with formatting
        tree = ET.ElementTree(root)
        
        # Add indentation for better readability (Python 3.9+)
        try:
            ET.indent(tree, space="    ", level=0)
        except AttributeError:
            # For older Python versions, indentation not available
            pass
            
        tree.write(filename, encoding='utf-8', xml_declaration=False)
        
    except Exception as e:
        print(f"Error serializing to XML: {e}")


def deserialize_from_xml(filename):
    """
    Deserialize XML data from file back to a Python dictionary.
    
    Args:
        filename (str): The filename to read the XML data from
        
    Returns:
        dict: The deserialized Python dictionary, or None if error occurs
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct dictionary
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
