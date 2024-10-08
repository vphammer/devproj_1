
# CNIT-383 Dev Project 1

This project intends to parse different data types, and utilize unit testing to ensure functions for parsing work.



## Parsing
The parsing functions return information that a user could use; the main function of parse_data.py asks a user for a file to read through for parsing, either a .yaml/.yml, .json, or .xml, and calls each function depending on the file extension. XML returns the root tag, and JSON/YAML functions return all of the data. 
## Testing
Each function is tested in a unit test that ensures that each function gives an exact match that is needed when calling the example data files in the repository. 
