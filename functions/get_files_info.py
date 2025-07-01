import os

def get_files_info(working_directory, directory=None):
    try:
        
        if directory is None:
            directory = "."

        full_path = os.path.join(working_directory, directory)
        absolute_path = os.path.abspath(full_path)
        working_directory_abs = os.path.abspath(working_directory)

        if os.path.commonpath([absolute_path, working_directory_abs]) != working_directory_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory'
        
        entries = os.listdir(absolute_path)
        if not entries:
            return "Directory is empty"
        
        res = []
        for entry in entries:
            entry_path = os.path.join(absolute_path, entry)
            try:
                size = os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                res.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as e:
                res.append(f"- {entry}: Error: {e}")
        return "\n".join(res)
    except Exception as e:
        return f"Error: {e}"
