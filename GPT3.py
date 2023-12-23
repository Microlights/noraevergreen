import openai

# 替换为你的 OpenAI API 密钥
openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt, engine="text-davinci-002", temperature=0.7, max_tokens=150):
    """
    使用 OpenAI GPT-3 API 生成文本的函数。

    参数：
    - prompt: 生成文本的提示
    - engine: 使用的 GPT-3 引擎
    - temperature: 控制生成文本的创造性，值越高创造性越大
    - max_tokens: 生成文本的最大长度

    返回：
    生成的文本字符串
    """
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    generated_text = response['choices'][0]['text']
    return generated_text

def main():
    # 用户提供的输入提示
    user_prompt = "在未来的世界中，人工智能将如何改变我们的生活？"

    # 生成文本
    generated_text = generate_text(user_prompt)

    # 打印用户提示和生成的文本
    print("用户提示：", user_prompt)
    print("生成文本：", generated_text)

    # 提供更多的交互式体验，允许用户进一步探索生成的文本
    explore_more = input("是否要继续生成文本？(yes/no): ")

    while explore_more.lower() == "yes":
        # 用户提供的新提示
        new_prompt = input("请输入新的提示： ")

        # 生成新的文本
        generated_text = generate_text(new_prompt)

        # 打印生成的文本
        print("用户提示：", new_prompt)
        print("生成文本：", generated_text)

        # 继续循环或退出
        explore_more = input("是否要继续生成文本？(yes/no): ")

    print("程序结束。")

if __name__ == "__main__":
    main()
