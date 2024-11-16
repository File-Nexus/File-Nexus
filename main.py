import os
import sys
from file_scanner import FileScanner
from file_organizer import FileOrganizer
from ui import UserInterface

class FileNexus:
    def __init__(self):
        self.scanner = FileScanner()
        self.organizer = FileOrganizer()
        self.ui = UserInterface()

    def run(self):
        print("Welcome to FileNexus!")
        while True:
            choice = self.ui.show_main_menu()
            if choice == "1":
                directory = self.ui.get_directory()
                files = self.scanner.scan_directory(directory)
                self.ui.display_files(files)
            elif choice == "2":
                rules = self.ui.get_organizer_rules()
                directory = self.ui.get_directory()
                self.organizer.organize(directory, rules)
            elif choice == "3":
                print("Exiting FileNexus. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = FileNexus()
    app.run()
