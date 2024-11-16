from file_scanner import FileScanner
from file_organizer import FileOrganizer

class FileNexus:
    def __init__(self):
        self.scanner = FileScanner()
        self.organizer = FileOrganizer()

    def run(self):
        print("Welcome to FileNexus!")
        while True:
            print("\nMain Menu:")
            print("1. Scan Directory")
            print("2. Organize Files")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                directory = input("Enter the directory to scan: ")
                try:
                    files = self.scanner.scan_directory(directory)
                    print("\nScanned Files:")
                    for file in files:
                        print(file)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                directory = input("Enter the directory to organize: ")
                rules = {
                    ".txt": "TextFiles",
                    ".jpg": "Images",
                    ".png": "Images",
                    ".pdf": "Documents",
                }
                try:
                    self.organizer.organize(directory, rules)
                    print("Files organized successfully!")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Exiting FileNexus. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = FileNexus()
    app.run()
