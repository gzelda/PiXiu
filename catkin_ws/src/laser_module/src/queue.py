# 定义队列类
class MyQueue(object):
    def __init__(self, size):
        self.size = size  # 定义队列长度
        self.queue = []  # 存储队列 列表

    def __str__(self):
        # 返回对象的字符串表达式，方便查看
        return str(self.queue)

    def inQueue(self, n):
        # 入队
        if self.isFull():
            return -1
        self.queue.append(n)  # 列表末尾添加新的对象

    def outQueue(self):
        # 出队
        if self.isEmpty():
            return -1
        firstelement = self.queue[0]   # 删除队头元素
        self.queue.remove(firstelement)  # 删除队操作
        return firstelement

    def delete(self, n):
        # 删除某元素
        element = self.queue[n]
        self.queue.remove(element)

    def inPut(self, n, m):
        # 插入某元素 n代表列表当前的第n位元素 m代表传入的值
        self.queue[n] = m

    def getSize(self):
        # 获取当前长度
        return len(self.queue)

    def getnumber(self, n):
        # 获取某个元素
        element = self.queue[n]
        return element

    def getlist(self, start, length):
        # 获取某些元素
        element = self.queue[start:start+length+1]
        return element

    def isEmpty(self):
        # 判断是否为空
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self):
        # 判断队列是否满
        if len(self.queue) == self.size:
            return True
        return False