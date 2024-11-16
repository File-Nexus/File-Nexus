import os
import shutil

class FileOrganizer:
    def __init__(self):
        pass

    def organize(self, directory, rules):
        """
        Organizes files in the given directory based on the provided rules.
        :param directory: Path to the directory to organize.
        :param rules: Dictionary mapping file types (extensions) to target folders.
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")
        
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a valid directory.")
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_type = self._get_file_type(filename)
                target_folder = rules.get(file_type, "Other")  # Default to "Other" if no rule matches
                self._move_file(file_path, os.path.join(directory, target_folder))

    def _get_file_type(self, filename):
        """
        Determines the file type based on the extension.
        :param filename: The name of the file.
        :return: File type as a string (e.g., ".txt").
        """
        _, ext = os.path.splitext(filename)
        return ext.lower() if ext else "Unknown"

    def _move_file(self, file_path, target_folder):
        """
        Moves a file to the specified folder, creating the folder if necessary.
        :param file_path: Path to the file.
        :param target_folder: Path to the target folder.
        """
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.move(file_path, target_folder)
        print(f"Moved '{file_path}' to '{target_folder}'")

if __name__ == "__main__":
    organizer = FileOrganizer()
    test_directory = input("Enter the directory to organize: ")
    test_rules = {
        ".txt": "TextFiles",
        ".jpg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
    }
    try:
        organizer.organize(test_directory, test_rules)
    except Exception as e:
        print(f"Error: {e}")
