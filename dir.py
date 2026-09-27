import os
class DirectoryReader:
    def __init__(self, directory_path):
        self.directory_path = directory_path
    def list_files(self):
        files = [f for f in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, f)) and not f.endswith('.zip')]
        files_dict = []
        for file in files:
            file_entity = {
                'name': file,
                'path': os.path.join(self.directory_path, file),
                'date': self.read_date(os.path.join(self.directory_path, file))
            }
            files_dict.append(file_entity)
        return files_dict
    def read_date(self, file_path):
        return os.path.getmtime(file_path)
        