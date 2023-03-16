#通过PriorityQueue是一个优先级队列
from queue import PriorityQueue

class Design:
#
    def __init__(self, data) -> None:
        self.parse(data)

    def parse(self, d):
        # 将参数赋值给类属性
        self.name = d[0]
        self.left_bottom_x = int(d[1])
        self.left_bottom_y = int(d[2])
        self.right_top_x = int(d[3])
        self.right_top_y = int(d[4])
        self.polygon_num = int(d[5])
        self.md5 = d[6]
        # 计算多边形的面积
        self.area = (self.right_top_x - self.left_bottom_x) * (self.right_top_y - self.left_bottom_y)
        # 换算单位
        self.density = self.polygon_num * 1e6 / self.area

    def __repr__(self):
        return self.name
#比较密度数值大小
    def __lt__(self, other):
        return self.density > other.density

class Library:
#初始化变量
    def __init__(self, path):
        self.path = path
        self.data = PriorityQueue()
#输出比较后的数值大小依次排列
    def output(self):
        while not self.data.empty():
            print(self.data.get())
#加载数据
    def load(self):
        with open(self.path, "r") as f:
            header = f.readline()
            print("Header:", header)
            data = f.read().split("\n")
            for i in data:
                d = i.split("\t")
                if len(d) < 7:
                    continue
                self.data.put(Design(d))

def main():
    library = Library("./testdata.txt")
    library.load()
    library.output()


if __name__ == '__main__':
    main()
