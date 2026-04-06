class DataStream:

    def __init__(self, value: int, k: int):
        self.value= value
        self.k= k
        self.stack= []

    def consec(self, num: int) -> bool:
        
        stream= False
        self.stack.append(num)
        if self.stack[-1] != self.value:
            self.stack.clear()

        else:
            if len(self.stack) >= self.k:
                stream= True
        return stream  


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)