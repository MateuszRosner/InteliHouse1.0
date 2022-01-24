class RedbusFrame():
    def __init__(self, data_length):
        self.address = 0
        self.command = 0
        self.data_length = data_length
        self.data = [0 for _ in range(data_length)]
        self.CRC = 0

    def calcCRC(self):
        length = len(self) - 2                          # length of header and payload
        temp = 0
        crcWord = 0xFFFF
        self.__iter__()

        while(length):
            temp = (self.__next__() ^ crcWord) & 0xFF   # reduce value to 8-bit length
            crcWord = crcWord >> 8
            crcWord ^= crcTable[temp]
            length -= 1

        self.CRC = crcWord

    def clear(self):
        self.address = 0
        self.command = 0
        self.data.clear()
        self.CRC = 0

    def __repr__(self):
        return (f"Address: {self.address}, Command: {self.command}, Data: {self.data}, CRC: {self.CRC}")

    def __len__(self):
        len = 0
        for _ in self:
            len += 1

        return len

    def __iter__(self):
        self.index = 0
        return(self)

    def __next__(self):
        if self.index < 8:
            if self.index == 0:
                data = self.address
            elif self.index == 1:
                data = self.command
            elif self.index == 2:
                data = self.data[0]
            elif self.index == 3:
                data = self.data[1]
            elif self.index == 4:
                data = self.data[2]
            elif self.index == 5:
                data = self.data[3]
            elif self.index == 6:
                data = self.CRC & 0xFF
            elif self.index == 7:
                data = ((self.CRC >> 8) & 0xFF)

            self.index += 1

            return data
        else:
            raise StopIteration            
