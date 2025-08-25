def main():
    # 让用户输入文件名前缀（不要加 -A.txt）
    filename = input("请输入文件名 (不要加 -A.txt)： ").strip()

    # 文件路径改成当前目录
    file_a = filename + "-A.txt"
    file_b = filename + "-B.txt"
    file_out = filename + "-out.txt"

    # 读取文件
    with open(file_a, "r", encoding="utf-8") as fa:
        lines_a = fa.readlines()
    with open(file_b, "r", encoding="utf-8") as fb:
        lines_b = fb.readlines()

    combined_lines = []

    # 按行交替合并（奇数行 A，偶数行 B）
    for i in range(max(len(lines_a), len(lines_b))):
        if i < len(lines_a):
            combined_lines.append(lines_a[i].rstrip("\n"))
        if i < len(lines_b):
            combined_lines.append(lines_b[i].rstrip("\n"))

    # 保存结果
    with open(file_out, "w", encoding="utf-8") as fout:
        for line in combined_lines:
            fout.write(line + "\n")

    # 打印出来看看“图像”
    print("\n=== 合并后的内容 ===")
    for line in combined_lines:
        print(line)

if __name__ == "__main__":
    main()