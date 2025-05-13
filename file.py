import json

# Function to modify text file
def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (example: converting text to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File has been modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

# Function to handle user input and error for text files
def prompt_for_file():
    filename = input("Please enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError as e:
        print(f"Error: Could not read the file {filename}. Details: {e}")

# Function to modify JSON file
def modify_json_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            data = json.load(input_file)

        # Modify the JSON data
        data['new_key'] = 'new_value'

        with open(output_filename, 'w') as output_file:
            json.dump(data, output_file, indent=4)

        print(f"JSON data has been modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_filename} is not a valid JSON file.")
    except IOError as e:
        print(f"Error: {e}")

# Example usage:
input_filename = "example.txt"
output_filename = "modified_example.txt"
read_and_modify_file(input_filename, output_filename)

prompt_for_file()

input_json_filename = "data.json"
output_json_filename = "modified_data.json"
modify_json_file(input_json_filename, output_json_filename)
