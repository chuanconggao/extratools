#! /usr/bin/env python3

class DefaultList(list):
    def __init__(self, default, *args):
        super().__init__(*args)

        self.default = default


    def __grow(self, index):
        if index >= len(self):
            self.extend([self.default()] * (index + 1 - len(self)))


    def __getitem__(self, index):
        self.__grow(index)
        return super().__getitem__(index)


    def __setitem__(self, index, value):
        self.__grow(index)
        super().__setitem__(index, value)
