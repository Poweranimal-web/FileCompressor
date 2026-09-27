import dir
import file

if __name__ == "__main__":
    directory_reader = dir.DirectoryReader("/home/nikita/compressor/test")
    file_compressor = file.FileCompressor(directory_reader)
    file_compressor.compress_files()