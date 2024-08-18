import os
import re

# Define your arguments here

# CONTROL EVALUATIONS
ROOT_PATH = r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar"
RELATIVE_FILE = "backdoor_control_spar.md"

## CYBERSECURITY BENCHMARKS
# ROOT_PATH = r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts"
# RELATIVE_FILE = "CybersecurityBenchmarks.md"

# # MAROS
# ROOT_PATH = r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\schemas"
# ROOT_PATH = r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples"
# RELATIVE_FILE = "AT_schemas.md"
# RELATIVE_FILE = "AT_samples.md"

BASE_PATH = r"C:\Users\jraldua-veuthey\Documents\Github\gh_llm_loader\my_scripts\output_mds"
OUTPUT_FILE = os.path.join(BASE_PATH, RELATIVE_FILE)
IGNORE_FILES = []
IGNORE_FOLDERS = []
IGNORE_EXTENSIONS = []
REMOVE_PYTHON_COMMENTS = False

# Whitelist mode settings
USE_WHITELIST = True
WHITELIST = [
    # CONTROL EVALUATIONS
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\src\code_evaluation",
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\src\model_querying",
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\src\monitoring",
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\src\pipeline",
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\src\runners",
    r"C:\Users\jraldua-veuthey\Documents\Github\backdoor_control_spar\core\llm_api",
    
    # CYBERSECURITY BENCHMARKS
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\analysis_instruct.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\move_bad_data_instruct.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\plot_cyberattack_helpfulness_results.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\plot_insecure_code_results.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\process_false_positives.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\remove_bad_data_instruct.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\remove_bad_examples_from_instruct_json.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\run_lint.sh",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\run_tests.sh",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\second_pass_bad_data_instruct.py",
    # r"C:\Users\jraldua-veuthey\Documents\Github\cyberseceval-errors\CybersecurityBenchmarks\scripts\with_versus_without_instruct_comparison.py",

    # # CYBERSECURITY BENCHMARKS
    # r"C:\Users\jraldua-veuthey\Videos\PRIVAT!\Apart\Zainab_Suhas_28-06-2024 13-30-56.md",
    # r"C:\Users\jraldua-veuthey\Videos\PRIVAT!\Apart\08-07-2024 20-00-35.md",
    # r"C:\Users\jraldua-veuthey\Videos\PRIVAT!\Apart\03-07-2024 20-20-22.md",

    # # MAROS - AT schemas
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\schemas\ATinterface.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\schemas\Components.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\schemas\Geometries.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\schemas\Objects.json",

    # MAROS - AT samples
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\BufferStop.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\CatenaryPole.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\Fence.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\FuseBox.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\HandRail.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\Platform.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\Rail.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\SignalPole.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\SignPole.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\Wall.json",
    # r"C:\other_prjs\sim_alg\Map\map_related_functions_matlab\local_tests\AT\AT Map Interface v1\samples\Wire.json",

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

def get_python_files_in_folder(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def expand_whitelist(whitelist):
    expanded_whitelist = []
    for item in whitelist:
        if '.' not in item.split('\\')[-1] and '.' not in item.split('/')[-1]:  # It's a folder
            expanded_whitelist.extend(get_python_files_in_folder(item))
        else:  # It's a file
            expanded_whitelist.append(item)
    return expanded_whitelist

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
    expanded_whitelist = expand_whitelist(WHITELIST)
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_path in expanded_whitelist:
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