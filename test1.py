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
    print(response)

messages=[
        {"role":"system","content":"你是一个思维缜密的助手"},
        {"role":"user","content":"你能帮我写一段西游记风格的小说吗？"}
    ]






print(askChatGPT(messages))


# messages = [
#     {"role": "system", "content": "你是chatgpt"}
# ]

# while True:

#     # Add the user's input to the messages list and user the 'user' role
#     user_input = input("Q: ")
#     messages.append({"role": "user", "content": user_input})

#     # Call the OpenAI api for Chat GPT, and pass our complete list of messages
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         temperature=0
#     )

#     # Show ChatGPT's response and add the response to our list of messages
#     print('A: ' + str(response['choices'][0]['message']['content']) + '\n')
#     messages.append(response['choices'][0]['message'])