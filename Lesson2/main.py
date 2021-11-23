# if文

a: int = 5
b: int = 10

if a < b:
    print("bが大きい")
else:
    print("aが大きい")

if a < 1:
    print("a小さい")
elif a < b:
    print("b大きい")
else:
    print("それ以外")