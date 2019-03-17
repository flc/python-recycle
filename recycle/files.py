import gzip
import os
import struct
import hashlib
import six


def file_line_count(path, open_func=open, buf_size=1024**2):
    with open_func(path) as f:
        lines = 0
        read_f = f.read  # loop optimization

        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)

        return lines


def gzip_compress_existing_file(path, keep_original=False, compresslevel=9):
    f_in = open(path, 'rb')
    new_path = '{}.gz'.format(path)
    f_out = gzip.open(new_path, 'wb', compresslevel)
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()

    if not keep_original:
        os.unlink(path)

    return new_path


def tail_file(path, num=100, open_func=open):
    lines = file_line_count(path, open_func)
    tail_lines = []
    tail_from = max(lines - num, 0)
    with open_func(path) as f:
        for idx, line in enumerate(f, 1):
            if idx > tail_from <= lines:
                yield line


def get_gzip_uncompressed_size(path):
    with open(path, 'rb') as f:
        f.seek(-4, 2)
        return struct.unpack('I', f.read(4))[0]


def tail_file_bytes(path, bytes=1000):
    if path.endswith('.gz'):
        size = get_gzip_uncompressed_size(path)
        open_func = gzip.open
    else:
        size = os.path.getsize(path)
        open_func = open
    jump_to = max(size - bytes, 0)
    with open_func(path) as f:
        f.seek(jump_to)
        for line in f:
            yield line


def checksum_file(path, hasher_func=hashlib.md5, buf_size=1024**2):
    hasher = hasher_func()
    with open(path, 'rb') as f:
        read_f = f.read  # loop optimization
        buf = read_f(buf_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = read_f(buf_size)
    return hasher.hexdigest()
