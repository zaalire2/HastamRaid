bin_format = '#010b'    # Binary format to store data. '#010b' = 8 bits/1 byte not including '0b' append


class RAIDFile:
    data_B = []
    start_addr = None
    padding = 0

    def __init__(self, file_id, data):
        self.id = file_id
        self.data_S = data
        self.data_B = self.convert_string(data)

    def __len__(self):
        return len(self.data_B)

    def __repr__(self):
        return repr(self.id) + ": '" + self.data_S + "'"

    def __eq__(self, other):
        if type(other) is type(self):
            return self.data_B == other.data_B
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def convert_string(d):
        bin_list = []
        for x in d:
            bin_list.append(format(ord(x), bin_format))  # Change character -> integer -> binary string and append to list
        return bin_list

    @staticmethod
    def from_bits(file_id, b):
        ret_str = ""
        for x in b:
            ret_str += chr(int(x, 2))
        return RAIDFile(file_id, ret_str)
