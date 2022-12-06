from parser_chml import parse_chml
from generator_chml import generate_html
# Define the compiler for CHML

def compile_chml(chml_code):
    # Parse the CHML code
    parse_tree = parse_chml(chml_code)

    # Generate the Python code
    py_code = generate_html(parse_tree)

    return py_code

# Example usage

chml_code = '''
div#app.container:
  h1#heading.primary-heading:Welcome to our website/:
  p#intro-text.lead:Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.:em#important-note:Please note that all information on this website is for educational purposes only and should not be used as a substitute for professional advice./:  
  '''

print(compile_chml(chml_code))