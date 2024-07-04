import os
import re

# Define your arguments here
ROOT_PATH = r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring"
OUTPUT_FILE = r"C:\Users\jraldua-veuthey\Documents\Github\gh_llm_loader\my_scripts\output_mds\control-evaluations_monitoring.md"
IGNORE_FILES = []
IGNORE_FOLDERS = []
IGNORE_EXTENSIONS = []
REMOVE_PYTHON_COMMENTS = False

# Whitelist mode settings
USE_WHITELIST = True
WHITELIST = [
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring\experiments_setup_notebook.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring\backdoor_funcs.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring\problem_setup.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring\correctness_evaluation_python.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\rrutils\redis_cache_wrapper.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\monitoring\make_plots.py",
    r"C:\Users\jraldua-veuthey\Documents\Github\control-evaluations\elk\func_correct\exec_code.py",
]

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if REMOVE_PYTHON_COMMENTS and file_path.endswith('.py'):
                content = remove_python_comments(content)
            return content
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

def remove_python_comments(content):
    # Remove multi-line comments
    content = re.sub(r'"""[\s\S]*?"""', '', content)
    content = re.sub(r"'''[\s\S]*?'''", '', content)
    
    # Remove single-line comments
    content = re.sub(r'#.*', '', content)
    
    # Remove empty lines
    content = '\n'.join(line for line in content.splitlines() if line.strip())
    
    return content

def should_include(path, root_path):
    if USE_WHITELIST:
        return path in WHITELIST
    else:
        file_name = os.path.basename(path)
        folder_name = os.path.basename(os.path.dirname(path))
        file_extension = os.path.splitext(file_name)[1]
        return not (file_name in IGNORE_FILES or 
                    folder_name in IGNORE_FOLDERS or 
                    file_extension in IGNORE_EXTENSIONS)

def get_new_output_file(output_file):
    directory, filename = os.path.split(output_file)
    name, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(output_file):
        new_name = f"{name}_v{counter}{ext}"
        output_file = os.path.join(directory, new_name)
        counter += 1
    return output_file

def create_markdown(root_path, output_file):
    output_file = get_new_output_file(output_file)
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_path in WHITELIST:
            if os.path.exists(file_path):
                relative_path = os.path.relpath(file_path, root_path)
                output.write(f"# {relative_path}\n\n")
                output.write("```\n")
                output.write(read_file_content(file_path))
                output.write("\n```\n\n")
    return output_file

def main():
    final_output_file = create_markdown(ROOT_PATH, OUTPUT_FILE)
    print(f"Markdown file created at {final_output_file}")

if __name__ == "__main__":
    main()