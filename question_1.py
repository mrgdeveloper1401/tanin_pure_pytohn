import os


class Folder:

    def __init__(self, command, topfolder=None):
        self.comment = command
        self.topfolder = topfolder
        self.sub_folders = []
        self.sub_files = []
        self.current_folder = '/'

        if self.comment == 'mkdir':
            self.mkdir(self.current_folder)
        elif self.comment == 'cd':
            self.cd(self.current_folder)
        elif self.comment == 'touch':
            self.touch(self.current_folder)
        elif self.comment == 'ls':
            self.ls()
        elif self.comment == 'pwd':
            self.pwd()
        elif self.comment == 'vi':
            self.vi(self.current_folder)
        elif self.comment == 'rn':
            self.rn(self.current_folder)
        elif self.comment == 'rmdir':
            self.rmdir(self.current_folder)
        elif self.comment == 'rm':
            self.rm(self.current_folder)
        elif self.comment == 'mv':
            self.mv(self.current_folder)
        else:
            raise Exception('Invalid Command')

    def mkdir(self, folder_name):
        if os.path.exists(folder_name):
            raise Exception('Folder Already Exists')
        else:
            os.mkdir(folder_name)

    def cd(self, folder_name):
        if folder_name == '..':
            self.current_folder = os.path.dirname(self.current_folder)
            new_folder_path = os.path.join(self.current_folder, folder_name)
            os.chdir(new_folder_path)
            if os.path.isdir(new_folder_path):
                self.current_folder = new_folder_path
            else:
                raise Exception('Folder Does Not Exist')

    def touch(self, parent_file, file_name):
        try:
            with open(os.path.join(self.current_folder, parent_file, file_name), 'w') as f:
                pass
        except FileNotFoundError:
            raise Exception('File Does Not Exist')
        except FileExistsError:
            raise Exception('File Already Exists')

    def ls(self):
        content = os.listdir(self.current_folder)
        return sorted(content)

    def pwd(self, folders, aim):
        return self.current_folder

    def vi(self, file_name):
        if not os.path.exists(file_name):
            raise Exception('File Does Not Exist')
        else:
            while True:
                type_here = input('')
                if type_here == '!q':
                    break
                elif type_here == 'cat':
                    return type_here
                elif type_here == 'close':
                    with open(file_name, mode='w') as f:
                        f.write(type_here)

    def rn(self, old_name, new_name):
        if os.path.exists(new_name):
            raise Exception('A file with the new name has already been created')
        elif not os.path.exists(old_name):
            raise Exception('File Does Not Exist')
        else:
            os.rename(os.path.join(self.current_folder, old_name), os.path.join(self.current_folder, new_name))

    def rmdir(self, folders, folder_name):
        file_path = os.path.join(folders, folder_name)
        if not os.path.exists(file_path):
            raise Exception('Folder Does Not Exist')
        else:
            os.rmdir(file_path)

    def rm(self, folders, file_name):
        file_path = os.path.join(folders, file_name)
        if not os.path.exists(file_path):
            raise Exception('File Does Not Exist')
        else:
            os.remove(file_path)

    def mv(self, folders, name, destination_folder):
        source_path = os.path.join(folders, name)
        destination_path = os.path.join(destination_folder, name)
        if not os.path.exists(source_path):
            raise Exception('Folder Does Not Exist')
        else:
            os.rename(source_path, destination_path)
        
# mkdir
# f1 = Folder('mkdir')
# f1.mkdir('test')

# cd
f2 = Folder('cd')
# f2.cd('../cd')

# touch
# f3 = Folder()

# ls
f4 = Folder('ls')
print(f4.ls())

# f5 = Folder('')




