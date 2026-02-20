# 打开文件并读取所有内容
print("=== 读取整个文件 ===")  # 打印一行标题，让人知道程序在做什么

# with open('文件名', '模式', encoding='编码') as 变量名:
with open('example.txt', 'r', encoding='utf-8') as file:
    # 'example.txt' - 要打开的文件名
    # 'r' - 模式：r表示读取（read）
    # encoding='utf-8' - 编码方式，支持中文
    # as file - 把打开的文件叫做file，方便后面使用
    
    content = file.read()  # 读取文件所有内容，存到content变量里
    print(content)  # 把读取到的内容打印出来
# 注意：with语句块结束后，文件会自动关闭，不需要我们操心
print("\n=== 逐行读取文件 ===")  # \n是换行符，让输出有个空行

with open('example.txt', 'r', encoding='utf-8') as file:
    # for循环：把文件里的每一行都拿出来看看
    for line in file:  # line会依次变成文件的每一行
        # strip()：去掉每行末尾的换行符和多余的空格
        print(f"行内容: {line.strip()}")  
        # f"字符串{变量}" 是格式化字符串，可以把变量值插入到字符串中
        