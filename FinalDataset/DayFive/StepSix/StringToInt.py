# s="0000000000000000000000000000000100000000000000000000000000000000000000010000000000000000000000000000000000000000000"
s="100"
class Binary():
    # def __init__(self, binNumber):
    #     self._binNumber = binNumber
    #     self._binNumber = self._binNumber[::-1]
    #     self._binNumber = list(self._binNumber)
    #     self._x = [1]
    #     self._count = 1
    #     self._change = 2
    #     self._amount = 0
    #     print((self._ToNumber(self._binNumber)))

    def _ToNumber(self, binNumber):
        self._binNumber = binNumber
        self._binNumber = self._binNumber[::-1]
        self._binNumber = list(self._binNumber)
        self._x = [1]
        self._count = 1
        self._change = 2
        self._amount = 0
        # print((self._ToNumber(self._binNumber)))
        self._number = self._binNumber
        for i in range (1, len (self._number)):
            self._total = self._count * self._change
            self._count = self._total
            self._x.append(self._count)
        self._deep = zip(self._number, self._x)
        for self._k, self._v in self._deep:
            if self._k == '1':
                self._amount += self._v
        # x = self._ToNumber(self._binNumber)
        import math
        try:
            x=math.log(self._amount)
        except:
            x=0
        return x


# mo = Binary()._ToNumber(s)
# print(mo)