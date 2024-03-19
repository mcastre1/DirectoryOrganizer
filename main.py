import os

'''
Directory Organizer
Will help you organize the given directory, by creating folders
according to the files extensions found in the given directory.
'''


class DirectoryOrganizer():
    def __init__(self, dir=".", dest_dir="./folders") -> None:
        self.dir = dir
        self.dest_dir = dest_dir

    def run(self):
        files = os.listdir(self.dir)

        if os.path.exists(self.dest_dir):
            print("Exists")
        else:
            os.mkdir(self.dest_dir)

        for file in files:
            splitup_path = os.path.splitext(file)
            file_name = splitup_path[0]
            file_extension = splitup_path[1]

            print(f"File Name: {file_name}\n" +
                  f"File Extension: {file_extension}")


if __name__ == "__main__":
    diro = DirectoryOrganizer(".")
    diro.run()
