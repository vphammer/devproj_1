import unittest
from parse_data import parse_json, parse_xml, parse_yaml
import yaml
import json
import xml.etree.ElementTree as ET

class TestYAMLParse(unittest.TestCase):
    def test_yaml(self):
        with open('/home/nhammer/scripting/devproj_1/my_data.yaml', 'r') as yaml_source:
            yaml_data = yaml.safe_load(yaml_source)
        yaml_formatted = yaml.dump(yaml_data)
        self.assertEqual(parse_yaml('my_data.yaml'), yaml_formatted)

class TestJSONParse(unittest.TestCase):
    def test_json(self):
        with open('/home/nhammer/scripting/devproj_1/my_data.json', 'r') as json_source:
            json_data = json.load(json_source)
        json_formatted = json.dumps(json_data, indent=4)
        self.assertEqual(parse_json('my_data.json'), json_formatted)

class TestXMLParse(unittest.TestCase):
    def test_xml(self):
        self.assertEqual(parse_xml('my_data.xml'), 'data')