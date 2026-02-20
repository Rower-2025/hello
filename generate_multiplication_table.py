# 生成九九乘法表并写入example.txt
with open('example.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 10):
        line = ''
        for j in range(1, i + 1):
            line += f'{j}×{i}={i*j}\t'
        f.write(line.strip() + '\n')