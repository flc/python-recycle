# import gzip
import os
import hashlib
import pytest

from recycle import files


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


@pytest.mark.parametrize(
    'filename,open_func,expected', [
        ('test.csv', open, 101),
        # ('test.csv.gz', gzip.open, 101)
    ]
)
def test_file_line_count(filename, open_func, expected):
    path = os.path.join(DATA_DIR, filename)
    assert files.file_line_count(path, open_func) == expected


@pytest.mark.parametrize(
    'filename,num,expected', [
        ('test.csv', 2, ['99,198\n', '100,200\n']),
    ]
)
def test_tail_file(filename, num, expected):
    path = os.path.join(DATA_DIR, filename)
    assert list(files.tail_file(path, num)) == expected


@pytest.mark.parametrize(
    'filename,expected', [
        ('test.csv.gz', 744),
    ]
)
def test_get_gzip_uncompressed_size(filename, expected):
    path = os.path.join(DATA_DIR, filename)
    assert files.get_gzip_uncompressed_size(path) == expected


@pytest.mark.parametrize(
    'filename,num,expected', [
        ('test.csv.gz', 9, [b'100,200']),
    ]
)
def test_tail_file_bytes(filename, num, expected):
    path = os.path.join(DATA_DIR, filename)
    assert list(line.strip() for line in files.tail_file_bytes(path, num)) == expected


@pytest.mark.parametrize(
    'filename,hasher_func,expected', [
        ('test.csv', hashlib.md5, '5f77786e3ec279aa545ba21cfecf27b5'),
        ('test.csv.gz', hashlib.md5, '666f5f02e8986913c3fb3049dad55837'),
        ('test.csv', hashlib.sha256, 'e13b6d134b32f2d70d38c37186ebf5782308e91f9a2027cefebc6bae93d9fdc5'),
        ('test.csv.gz', hashlib.sha256, 'f419eb4c9b0884d47b8003e368ee23221441a1ba68c92eac9108d73b2c201e1a'),
    ]
)
def test_checksum_file(filename, hasher_func, expected):
    path = os.path.join(DATA_DIR, filename)
    assert files.checksum_file(path, hasher_func) == expected
