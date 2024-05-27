# RealData provider
from random import randint

class _Proxy:
    def __getitem__(self, index):
        print(f"Accessing {index}")
        data = []
        while len(data) <100000000:
            data.append(randint(100,10000))
        return data

def getData():
    return _Proxy()
