import re

# Define the CHML syntax and semantics

CHML_ELEMENT_RE = re.compile(r'([a-zA-Z0-9]+)(#[a-zA-Z0-9-]+)?(\.[a-zA-Z0-9-]+)*:')
CHML_ATTRIBUTE_RE = re.compile(r'([a-zA-Z0-9-]+): ([^/:]+)')
CHML_CLOSING_RE = re.compile(r'/:')

# Define the parser for CHML

def parse_chml(chml_code):
    # Split the code into lines and remove leading/trailing whitespace
    lines = [line.strip() for line in chml_code.split('\n')]

    # Initialize the parse tree and the current indent level
    tree = []
    indent_level = 0

    # Iterate over the lines of code
    for line in lines:
        # Check if the line is an element
        element_match = CHML_ELEMENT_RE.match(line)
        if element_match:
            # Extract the element name, ID attribute, and class attributes
            element_name = element_match.group(1)
            element_id = element_match.group(2)[1:] if element_match.group(2) else None
            element_classes = element_match.group(3)[1:].split('.') if element_match.group(3) else []

            # Create a new element node
            node = {
                'type': 'element',
                'name': element_name,
                'id': element_id,
                'classes': element_classes,
                'attributes': {},
                'children': []
            }

            # print(tree)

            # Add the node to the parse tree
            if indent_level == 0:
                tree.append(node)
            else:
                if len(tree[-1]['children']) == 0:
                    tree[-1]['children'].append(node)
                else:
                    tree[-1]['children'][-1]['children'].append(node)

            # Increment the indent level
            indent_level += 1

        # Check if the line is an attribute
        attribute_match = CHML_ATTRIBUTE_RE.match(line)
        if attribute_match:
            # Extract the attribute name and value
            attribute_name = attribute_match.group(1)
            attribute_value = attribute_match.group(2)

            # Add the attribute to the current element
            tree[-1]['attributes'][attribute_name] = attribute_value

        # Check if the line is a closing tag
        closing_match = CHML_CLOSING_RE.match(line)
        if closing_match:
            # Decrement the indent level
            indent_level -= 1

    return tree

# Define the code generator for CH
