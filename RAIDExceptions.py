class ParityCalculationException(Exception):
    def __init__(self, block=None, expected=None, actual=None):
        self.block = block
        self.expected = expected
        self.actual = actual

        if block is None or expected is None or actual is None:
            msg = "Incorrect parity bit calculation"
        else:
            msg = "Incorrect parity bit calculation\nBlock: "
            for x in block:
                msg += x + " "
            msg += "\nExpected: " + repr(expected) + " (" + format(expected, '#010b') + ")\n"
            msg += "Actual:   " + repr(actual) + " (" + format(actual, '#010b') + ")\n"
        super(ParityCalculationException, self).__init__(msg)


class DiskException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super(DiskException, self).__init__(msg)


class DiskFullException(DiskException):
    def __init__(self, disk_id):
        self.disk_id = disk_id
        super(DiskFullException, self).__init__("Error writing file: Target disk '" + repr(disk_id) + "' is full")


class DiskReadException(DiskException):
    def __init__(self, msg):
        self.msg = msg
        super(DiskReadException, self).__init__(msg)


class DiskReconstructException(DiskException):
    def __init__(self, msg):
        self.msg = msg
        super(DiskReconstructException, self).__init__(msg)


class DataMismatchException(DiskException):
    def __init__(self, msg):
        self.msg = msg
        super(DataMismatchException, self).__init__(msg)


