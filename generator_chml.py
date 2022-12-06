# Define the HTML generator

def generate_html(parse_tree):
    # Initialize the HTML code as an empty string
    html_code = ''

    # Iterate over the nodes in the parse tree
    for node in parse_tree:
        # Check if the node is an element
        if node['type'] == 'element':
            # Generate the HTML code for the element
            element_code = f'<{node["name"]}'

            # Add the ID attribute, if present
            if node['id']:
                element_code += f' id="{node["id"]}"'

            # Add the class attributes, if present
            if node['classes']:
                element_code += f' class="{ " ".join(node["classes"]) }"'

            # Add the attributes, if present
            if node['attributes']:
                for attribute_name, attribute_value in node['attributes'].items():
                    element_code += f' {attribute_name}="{attribute_value}"'

            # Add the closing angle bracket
            element_code += '>'

            # Add the children, if present
            if node['children']:
                element_code += generate_html(node['children'])

            # Add the closing tag, if necessary
            if node['name'] not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                element_code += f'</{node["name"]}>'

            # Add the element code to the HTML code
            html_code += element_code

    return html_code
