class VideoCard:
    def __init__(self):
        self.a = [0] * 20

    def __add__(self, b):
        if isinstance(b, int):
            for i in range(len(self.a)):
                self.a[i] += b
        return self.a

V1 = VideoCard()

result1 = V1 + 5
print(result1)  

result2 = V1 + 5
print(result2)  
