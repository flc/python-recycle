# based on http://code.activestate.com/recipes/577610-decoding-binary-files/
import struct
import six


class BinaryReaderEOFException(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Not enough bytes in file to satisfy read request'


class BinaryReader:

    # Map well-known type names into struct format characters.
    types = {
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q',
        'float': 'f',
        'double': 'd',
        'char': 's',
        }

    def __init__(self, path_or_buff):
        if isinstance(path_or_buff, str):
            self.file = open(path_or_buff, 'rb')
        else:
            self.file = path_or_buff

    def read(self, type_name):
        type_format = self.types[type_name.lower()]
        type_size = struct.calcsize(type_format)
        value = self.file.read(type_size)
        if type_size != len(value):
            raise BinaryReaderEOFException
        return struct.unpack(type_format, value)[0]

    def __del__(self):
        self.file.close()
