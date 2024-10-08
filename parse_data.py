import json
import yaml
import xml.etree.ElementTree as ET


def parse_xml(xml_filename):
    xml_data = ET.parse(xml_filename)
    root = xml_data.getroot()
    print(root.tag)
    for child in root:
        print(f"{child.tag}: {child.text}")

def parse_json(json_filename):
    with open (json_filename, 'r') as json_source:
        json_data = json.load(json_source)
        json_formatting = json.dumps(json_data, indent=4)
        print(json_formatting)

def parse_yaml(yaml_filename):
    with open(yaml_filename, 'r') as yaml_source:
        return yaml.dump(yaml.safe_load(yaml_source))

def main():
    filename = input("Please enter the filename of the data you wish to parse.\n")
    while True:
        match filename:
            case filename if ".xml" in filename:
                parse_xml(filename)
                break
            case filename if ".json" in filename:
                parse_json(filename)
                break
            case filename if ".yaml" in filename or ".yml" in filename:
                parse_yaml(filename)
                break
            case _:
                filename = input("Supported file types are XML, JSON, and YAML. Please try again.\n")

if __name__ == "__main__":
    main()