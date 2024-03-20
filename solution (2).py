class Folder:

    def __init__(self, command, topfolder=None):
        self.command = command
        self.topfolder = topfolder
        self.sub_folders = []
        self.sub_files = []
        self.current_folder = 'root'

    def mkdir(self, folder_name):
        if folder_name in self.sub_folders:
            raise Exception('Folder Already Exists')
        else:
            self.sub_folders.append(folder_name)

    def cd(self, folder_name):
        if folder_name == '..':
            if folder_name in self.sub_folders:
                self.current_folder = folder_name
            else:
                raise Exception('Folder Does Not Exist')

    def touch(self, parent_folder, file_name):
        if parent_folder not in self.sub_folders:
            raise Exception('Folder Does Not Exists')
        if file_name in self.sub_files:
            raise Exception('File Already Exists')
        else:
            self.sub_files.append(file_name)
            parent_index = self.sub_folders.index(parent_folder)
            self.sub_folders[parent_index].sub_files.append(file_name)

    def ls(self, folder_name):
        if folder_name == '++':
            all_items = []
            all_items.extend(self.sub_folders)
            all_items.extend(self.sub_files)
            seen = set()
            for item in all_items:
                if item.name in seen:
                    raise Exception('There are duplicate files in the folder')
                else:
                    seen.add(item.name)

            return sorted(all_items, key=lambda x: x.name)

    def pwd(self, folders, aim):
        if aim == "":
            return "/".join([folder.name for folder in folders])

        paths = []
        for folder in folders:
            if aim in folder.sub_folders or aim in folder.sub_files:
                paths.append(folder.name)
                paths.append(aim)
                return "/".join(paths)

    def vi(self, file_name):
        found = False
        for file in self.sub_files:
            if file.name == file_name:
                found = True
                new_content = input("Enter new content for the file. Enter 'q !' to save and exit: ")
                while new_content != "q !":
                    file.content = new_content
                    new_content = input("Enter new content for the file. Enter 'q !' to save and exit: ")
                print("Successfully edited the file.")
                return
        if not found:
            raise Exception("File Does Not Exist")

    def rn(self, old_name, new_name):
        for folder in self.sub_folders:
            if old_name in folder.sub_files:
                if new_name in folder.sub_files:
                    raise Exception("A file with the new name has already been created")
                folder.sub_files[folder.sub_files.index(old_name)] = new_name
                return
        for folder in self.sub_folders:
            if folder.name == old_name:
                if new_name in folder.sub_folders:
                    raise Exception("A folder with the new name has already been created")
                folder.name = new_name
                return
        raise Exception("Exist Not Does File")

    def rmdir(self, folder_name):
        found = False
        for folder in self.sub_folders:
            if folder.name == folder_name:
                self.sub_folders.remove(folder)
                found = True
        if not found:
            raise Exception("Exist Not Does Folder")

    def rm(self, file_name):
        found = False
        for folder in self.sub_folders:
            if file_name in folder.sub_files:
                folder.sub_files.remove(file_name)
                found = True
        if not found:
            raise Exception("File Does Not Exist")

    def mv(self, name, destination_folder):
        found_source = False
        found_dest = False
        for folder in self.sub_folders:
            if folder.name == name:
                found_source = True
                for dest_folder in self.sub_folders:
                    if dest_folder.name == destination_folder:
                        found_dest = True
                        dest_folder.sub_folders.append(folder)
                        self.sub_folders.remove(folder)
                        return
        if not found_source:
            raise Exception("Exist Not Does Folder")
        if not found_dest:
            raise Exception("Exist Not Does Folder")
