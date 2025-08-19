# 1️⃣ 让用户输入 要输入多少个数字
while_check = True
while while_check:
    number = input("Please enter how many number you going to enter: ")
    try:
# try：告诉 Python “我打算运行这段代码，但它有可能出错”
# except：告诉 Python “如果出错了，不要直接崩溃，按我说的去处理”
        number = int(number)
        while_check = False
    except:
        print("The text you entered is not a number!")

# 2️⃣ 用列表存储 所输入的 所有数字
numbers = []  # 定义一个空列表，用来存数字
for i in range(number):  # 循环 count 次数，让用户一个一个输入数字
    while True:  # while True 是一个死循环，意思是“一直重复执行里面的代码”，直到我们用 break 跳出来
        try:
            value = float(input("please enter a number: "))  # float() 可以处理小数
            numbers.append(value)  # 把合法的数字存到列表 numbers 中
            break  # 输入成功就跳出循环
        except:
            print("The text you entered is not a number!")

# 3️⃣ 做计算
max_num = max(numbers)  # 列表中的最大值
min_num = min(numbers)  # 列表中的最小值
total = sum(numbers)    # 列表中所有数字的总和
average = total / len(numbers) # 平均数 = 总和 ÷ 个数

# 4️⃣ 找最大值和最小值的位置（可能有重复）
max_pos = []
min_pos = []
for i in range(len(numbers)):
# 在 Python 里，len() 的含义就是：获取某个容器（字符串、列表、元组、）里面元素的数量
# len(numbers) → 列表有多少个元素，比如上面是 6
# range(len(numbers)) → 生成 0, 1, 2, 3, 4, 5（这些是索引）
# for i in ... → 依次取出每个索引 i
    if numbers[i] == max_num:
        max_pos.append(i)  # 把位置存起来
    if numbers[i] == min_num:
        min_pos.append(i)

# 5️⃣ 输出结果
print(f"The max number is {max_num} and position at {','.join(str(pos) for pos in max_pos)}")
print(f"The min number is {min_num} and position at {','.join(str(pos) for pos in min_pos)}")
# max_pos 是存了最大值位置的列表，比如 ["1", "3"]
# ",".join(max_pos) 会把它变成 "1,3"，中间用逗号隔开
# 这样输出就不会是列表形式 [“1”, “3”]，而是“1,3”

print(f"The total is {total}")
print(f"The average number is {average}")

