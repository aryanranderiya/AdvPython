
import zipfile
import os
import tarfile
import gzip
import shutil

# 1. Compressing Files Using zipfile
def compress_files_zip(files, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            if os.path.exists(file):
                zipf.write(file, compress_type=zipfile.ZIP_DEFLATED)
            else:
                print(f"File not found: {file}")

# 2. Decompressing Files Using zipfile
def decompress_zip(input_zip, output_dir):
    with zipfile.ZipFile(input_zip, 'r') as zipf:
        zipf.extractall(output_dir)

# 3. Compressing Files Using tarfile
def compress_files_tar(files, output_tar):
    with tarfile.open(output_tar, 'w:gz') as tarf:
        for file in files:
            tarf.add(file)

# 4. Decompressing Files Using tarfile
def decompress_tar(input_tar, output_dir):
    with tarfile.open(input_tar, 'r:gz') as tarf:
        tarf.extractall(output_dir)

# 5. Compressing Files Using gzip
def compress_file_gzip(file, output_gzip):
    with open(file, 'rb') as f_in:
        with gzip.open(output_gzip, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# 6. Decompressing Files Using gzip
def decompress_file_gzip(input_gzip, output_file):
    with gzip.open(input_gzip, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Usage examples (comment/uncomment to use)
# files_to_compress = ['file1.txt', 'file2.txt', 'file3.txt']
# compress_files_zip(files_to_compress, 'compressed_files.zip')
# decompress_zip('compressed_files.zip', './decompressed_files')

# compress_files_tar(files_to_compress, 'compressed_files.tar.gz')
# decompress_tar('compressed_files.tar.gz', './decompressed_files')

# compress_file_gzip('file1.txt', 'file1.txt.gz')
# decompress_file_gzip('file1.txt.gz', 'file1.txt')
