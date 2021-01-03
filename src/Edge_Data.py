from numpy.core import double


class Edge_Data:
    def __init__(self, src: int, des: int, w: double, info: str, tag: int):
        self.tag = tag
        self.info = info
        self.w = w
        self.des = des
        self.src = src



