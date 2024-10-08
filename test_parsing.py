import unittest
from parse_data import parse_json, parse_xml, parse_yaml
import yaml
import json

class TestYAMLParse(unittest.TestCase):
    def test_yaml(self):
        with open('/home/nhammer/scripting/devproj_1/my_data.yaml', 'r') as yaml_source:
            yaml_data = yaml.safe_load(yaml_source)
        yaml_formatted = yaml.dump(yaml_data)
        self.assertEqual(parse_yaml('/home/nhammer/scripting/devproj_1/my_data.yaml'), yaml_formatted)

class TestJSONParse(unittest.TestCase):
    def test_yaml(self):
        with open('/home/nhammer/scripting/devproj_1/my_data.yaml', 'r') as yaml_source:
            yaml_data = yaml.safe_load(yaml_source)
        yaml_formatted = yaml.dump(yaml_data)
        self.assertEqual(parse_yaml('/home/nhammer/scripting/devproj_1/my_data.yaml'), yaml_formatted)