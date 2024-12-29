# 要写入的文字
text_to_write = "你好，世界！这是我ddd dfgf ffff 写入文件的内容。"

# 指定文件名（修改为你的用户名）
file_name = r"C:\Users\hjw\Desktop\pythonceshi.txt"  # Windows示例


# 打开文件并写入内容
file = open(file_name, 'w', encoding='utf-8')
file.write(text_to_write)

# 关闭文件
file.close()

print(f"已将内容写入 {file_name}")





import random

# 读取文本文件并统计单词数
def count_words_in_file(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    
    words = content.split()
    print(f"words内的内容：{words}")
    print(f'文件中的单词总数为: {len(words)}')
    return words

# 随机输出其中的10个单词
def output_random_words(words, n=2):
    random_words = random.sample(words, min(n, len(words)))
    print(f"随机选出的{n}个单词: {random_words}")

# 文件路径
file_path = r'C:\Users\hjw\Desktop\pythonceshi.txt'  # 修改为你的文件路径

# 运行
words = count_words_in_file(file_path)
output_random_words(words)
