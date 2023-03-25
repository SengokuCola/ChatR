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

def read_txt(path):
    with open(path,'r') as f:
        text = f.read()
    return text
def split_string(instr,size):
    return [instr[i:i+size] for i in range(0, len(instr),size)]
def summary_message(text):
    messages=[
        {"role":"system","content":"你是一个思维缜密，细致入微，生动有趣的助手"},
        {"role":"user","content":"我有一份有关R语言的教学的文本，这份文本介绍了如何使用R语言，请你将这份文本尽可能详细地进行分段概括"},
        # {"role":"assistant","content":"好的，我将会给把出的文本进行精简，去除无意义的语气词，调整逻辑，润色句法，让文本更像出版物的文字稿,我只给出修改后的文本，不给出其他内容"},
        {"role":"user","content":"这是文本："}
    ]
    messages[2]["content"] += text
    return askChatGPT(messages)

def main():
    re_text = {}
    file_path = 'out.txt'
    text = read_txt(file_path)
    max_size=1000
    splited = split_string(text,max_size)   
    for i in range(len(splited)):
        final_text = summary_message(splited[i])
        re_text[i] = final_text
        with open("out_final.txt","a") as file:
            file.write(final_text)

    print(re_text)

main()

# resp = askChatGPT(messages)
# print(askChatGPT(messages2))








