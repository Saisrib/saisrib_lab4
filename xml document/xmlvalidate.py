import xmlschema
xml_file = "employee.xml"
xsd_file = "employee.xsd"

validator = xmlschema.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid")
else:
    print("XML file is invalid")
    print(validator.validate(xml_file))








