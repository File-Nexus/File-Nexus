import os
from datetime import datetime

class FileScanner:
    def __init__(self):
        pass

    def scan_directory(self, directory):
        """
        Scans a directory and returns a list of files with metadata.
        :param directory: Path of the directory to scan.
        :return: List of dictionaries containing file metadata.
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")
        
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a valid directory.")
        
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                file_stats = os.stat(file_path)
                files.append({
                    "name": filename,
                    "path": file_path,
                    "size": file_stats.st_size,  # File size in bytes
                    "last_modified": datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    "type": self._get_file_type(filename),
                })
        return files

    def _get_file_type(self, filename):
        """
        Determines the file type based on the extension.
        :param filename: The name of the file.
        :return: File type as a string.
        """
        _, ext = os.path.splitext(filename)
        return ext.lower() if ext else "Unknown"

if __name__ == "__main__":
    scanner = FileScanner()
    test_directory = input("Enter the directory to scan: ")
    try:
        results = scanner.scan_directory(test_directory)
        for file in results:
            print(file)
    except Exception as e:
        print(f"Error: {e}")
