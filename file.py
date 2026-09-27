import dir
import zipfile
import time
class FileCompressor:
    def __init__(self, filesEntity : dir.DirectoryReader):
        self.filesEntity = filesEntity
        self.files = self.filesEntity.list_files()
        print(self.files)
    def compress_files(self):
        for file in self.files:
            total_time = time.time() - file["date"] 
            if total_time >= 5256000: # 2 months in seconds
                with open(file['path'] + '.zip', 'wb') as f_compressed:
                    with zipfile.ZipFile(f_compressed, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        zipf.write(file['path'], arcname=file['name'])