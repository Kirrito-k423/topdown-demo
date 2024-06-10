import os
import re

def add_numbers_to_headers(markdown_text):
    # Initialize counters for headers
    header_counters = {2: 0, 3: 0, 4: 0}
    
    # Split the markdown text into lines
    lines = markdown_text.split('\n')
    
    # Regular expressions to match headers with and without numbers
    header2_pattern = re.compile(r'^## (\d+) (.+)$')
    header3_pattern = re.compile(r'^### (\d+\.\d+) (.+)$')
    header4_pattern = re.compile(r'^#### (\d+\.\d+\.\d+) (.+)$')
    
    # Process each line
    for i, line in enumerate(lines):
        if line.startswith('## '):
            match = header2_pattern.match(line)
            # If it's a level 2 header, increment the level 2 counter and reset the level 3 and 4 counters
            header_counters[2] += 1
            header_counters[3] = 0
            header_counters[4] = 0
            if match:
                # If already numbered, skip
                continue
            lines[i] = f"## {header_counters[2]} {line[3:]}"
        elif line.startswith('### '):
            match = header3_pattern.match(line)
            # If it's a level 3 header, increment the level 3 counter and reset the level 4 counter
            header_counters[3] += 1
            header_counters[4] = 0
            if match:
                # If already numbered, skip
                continue
            lines[i] = f"### {header_counters[2]}.{header_counters[3]} {line[4:]}"
        elif line.startswith('#### '):
            match = header4_pattern.match(line)
            # If it's a level 4 header, increment the level 4 counter
            header_counters[4] += 1
            if match:
                # If already numbered, skip
                continue
            lines[i] = f"#### {header_counters[2]}.{header_counters[3]}.{header_counters[4]} {line[5:]}"
    
    # Join the lines back into a single string
    return '\n'.join(lines)

def process_markdown_files_in_directory(directory_path):
    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    markdown_text = file.read()
                
                # Add numbers to headers
                new_markdown_text = add_numbers_to_headers(markdown_text)
                
                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_markdown_text)

if __name__ == "__main__":
    import argparse
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Add numbers to headers in Markdown files.")
    parser.add_argument("directory", help="The path to the directory containing the Markdown files.")
    
    args = parser.parse_args()
    
    # Process the Markdown files in the specified directory
    process_markdown_files_in_directory(args.directory)
