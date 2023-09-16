def count_word_frequency(text):
    # 将文本转换为小写并分割成单词列表
    words = text.lower().split()
    
    # 创建一个空字典来存储单词及其频率
    word_frequency = {}
    
    # 统计每个单词的频率
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

# 测试例子
text = "This is a sample text. This text is used to demonstrate word frequency counting."
result = count_word_frequency(text)
print(result)
