# for文

for i in range(10):
    print(i)

print("--------------------------------")

for i in range(1, 11):
    print(i)

print("--------------------------------")

test_list = [2,4,6,8,10]
for i in test_list:
    print(i)

print("--------------------------------")
# 内包表記

list01 = [i for i in range(5)]
print(list01)

print("--------------------------------")

list02 = [i * 2 for i in range(5)]
print(list02)

print("--------------------------------")

list03 = [i for i in range(10) if i % 2 == 0]
print(list03)

print("--------------------------------")

list04 = [i if i % 2 == 0 else i * 100 for i in range(10)]
print(list04)

print("--------------------------------")

list05 = [i * 5 if i % 5 == 0 else i * 2 if i % 2 == 0 else i for i in range(10)]
print(list05)

print("--------------------------------")

