import gzip
import os


def file_line_count(filename):
    with open(filename) as f:
        lines = 0
        buf_size = 1024 * 1024
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
