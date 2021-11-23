# 関数

def avg(a: int, b: int):
    return (a + b) / 2

result = avg(100, 50)
print(result)

# class
class Student:
    
    # コンストラクタ
    def __init__(self, id):
        self.id = id
    
    def avg(self, math, english):
        print((math + english) / 2)

# インスタンス化
a001 = Student(1)

# メソッドの実行
a001.avg(30, 70)

# アトリビュートの定義
a001.name = "Machida"
print(a001.name)

print(a001.id)
