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


def simplify_message(text):
    messages=[
        {"role":"system","content":"你是一个思维缜密的助手"},
        {"role":"user","content":"我开设了一门有关心理学的统计课程，并且为整个课程进行了录音，并将录音转成了文字稿，但是这份文字稿过于口语化且逻辑不清晰，请你帮助我简化录音稿的语言，并且理清逻辑。注意，只需要给出修改后的文本，不需要其他内容"},
        {"role":"assistant","content":"好的，我将会给把出的文本进行精简，去除无意义的语气词，调整逻辑，润色句法，让文本更像出版物的文字稿,我只给出修改后的文本，不给出其他内容"},
        {"role":"user","content":"这是文本："}
    ]
    messages[3]["content"] += text
    return askChatGPT(messages)

def rewrite_message(text):
    messages_rewrite=[
    {"role":"system","content":"你是一个精通中文的助手"},
    {"role":"user","content":"有一种中文文本，由于翻译自英文，因而带有许多英文的语法特点和措辞，带有英语母语者的思维痕迹，这样的文本被称作”翻译腔“的文本，请你帮助我使用更加本土化，地道的中文重写以下给出的文本，注意，只需要给出修改后的文本，不需要其他内容"},
    {"role":"assistant","content":"好的，我将会给把出的文本进行重写，使其更加符合中文母语者的用词习惯"},
    {"role":"user","content":"这是文本："}
    ]
    messages_rewrite[3]["content"] += text
    return askChatGPT(messages_rewrite)

def main():
    re_text = {}
    file_path = 'audio_to_txt.txt'
    text = read_txt(file_path)
    max_size=1200
    splited = split_string(text,max_size)   
    for i in range(len(splited)):
        resp_re = rewrite_message(simplify_message(splited[i]))
        print(resp_re)
        re_text[i] = resp_re
        with open("out.txt","a") as file:
            file.write(resp_re)

    print(re_text)

main()

# resp = askChatGPT(messages)
# print(askChatGPT(messages2))








