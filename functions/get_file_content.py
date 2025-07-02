import os
MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)
        working_directory_abs = os.path.abspath(working_directory)

        if os.path.commonpath([absolute_path, working_directory_abs]) != working_directory_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS+1)

            if len(file_content_string) <= MAX_CHARS:
                return file_content_string
            else:
                truncated = file_content_string[:MAX_CHARS]
                truncated += f'[...File "{file_path}" truncated at 10000 characters]'
                return truncated
    except Exception as e:
        return f"Error: {e}"