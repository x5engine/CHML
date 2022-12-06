# Define the code generator for CHML

def generate_py(parse_tree):
    # Initialize the Python code as an empty string
    py_code = ''

    # Iterate over the nodes in the parse tree
    for node in parse_tree:
        # Check if the node is an element
        if node['type'] == 'element':
            # Generate the Python code for the element
            element_code = f'Element("{node["name"]}")'

            # Add the ID attribute, if present
            if node['id']:
                element_code += f'.set_attribute("id", "{node["id"]}")'

            # Add the class attributes, if present
            if node['classes']:
                element_code += f'.set_attribute("class", "{ " ".join(node["classes"]) }")'

            # Add the attributes, if present
            if node['attributes']:
                for attribute_name, attribute_value in node['attributes'].items():
                    element_code += f'.set_attribute("{attribute_name}", "{attribute_value}")'

            # Add the children, if present
            if node['children']:
                for child in node['children']:
                    element_code += f'.append({generate_py([child])})'

            # Add the element code to the Python code
            py_code += element_code

    return py_code

# Define the compiler for CHML

