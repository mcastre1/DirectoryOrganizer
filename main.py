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

        # Here we iterate through all files in the specified directory in init.
        for file in files:
            # We split up the file name
            splitup_path = os.path.splitext(file)
            file_name = splitup_path[0]  # Save the file name on this variable.
            # Save the file extension on this variable.
            file_extension = splitup_path[1]

            # We check if the file we are working on has an extension.
            if file_extension:
                # We create a new path for our new folder here, by joining
                # our destination path and the file extension we are currently
                # working on without the dot.
                new_path = os.path.join(
                    self.dest_dir, file_extension.split('.')[1])

                # If such new path doesnt exists then we create the directory
                # For us to use in the future.
                if not os.path.exists(new_path):
                    os.mkdir(new_path)
                else:  # If the path, folder already exists, then we move the current file there.
                    pass

            print(f"File Name: {file_name}\n" +
                  f"File Extension: {file_extension}")


if __name__ == "__main__":
    diro = DirectoryOrganizer(".")
    diro.run()
