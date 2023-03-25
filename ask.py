import json
import openai
api_key = "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"
openai.api_key = api_key


def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages = messages,
        temperature=0,
    )
    return response['choices'][0]['message']['content']
    # print(response)

def simplify_message(text):
    messages=[
        {"role":"system","content":"你是一个思维缜密的助手"},
        {"role":"user","content":"我开设了一门有关心理学的统计课程，并且为整个课程进行了录音，并将录音转成了文字稿，但是这份文字稿过于口语化且逻辑不清晰，请你帮助我简化录音稿的语言，并且理清逻辑。注意，只需要给出修改后的文本，不需要其他内容"},
        {"role":"assistant","content":"好的，我将会给把出的文本进行精简，去除无意义的语气词，调整逻辑，润色句法，让文本更像出版物的文字稿,我只给出修改后的文本，不给出其他内容"},
        {"role":"user","content":"这是文本："}
    ]
    messages[3]["content"] += text
    return askChatGPT(messages)


def main():
    messages=[
        {"role":"system","content":"你是一个思维缜密的助手"},
        {"role":"user","content":"请问如何在python中将mp3音频文件分割成固定市场的数个文件？"}
    ]
    print(askChatGPT(messages))

main()

# resp = askChatGPT(messages)
# print(askChatGPT(messages2))








