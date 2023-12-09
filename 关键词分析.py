import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# 读取文本数据
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 分词
def segment_text(text):
    words = jieba.cut(text)
    return list(words)

# 统计词频
def count_words(words):
    word_counts = Counter(words)
    return word_counts

# 生成词云
def generate_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# 主函数
def main():
    # 替换为你的文本文件路径
    file_path = 'your_text_file.txt'
    
    # 读取文本
    text = read_text(file_path)
    
    # 分词
    words = segment_text(text)
    
    # 统计词频
    word_counts = count_words(words)
    
    # 输出词频统计结果
    print("词频统计结果：")
    print(word_counts.most_common(10))  # 输出前10个高频词
    
    # 生成词云
    generate_wordcloud(word_counts)

if __name__ == "__main__":
    main()
