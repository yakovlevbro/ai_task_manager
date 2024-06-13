from openai import OpenAI

# Установите ваш API-ключ
from ai_manager.settings import OPEN_AI_KEY


def get_ai_response(user_message):
    client = OpenAI(
        api_key=OPEN_AI_KEY,
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You’re a strongest product manager, and you’re always willing to help, if you can ask "
                           "questions - you ask"},
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# messages = [
#  {"role": "system", "content": "You’re a kind helpful assistant"}
# ]

# while True:
#     content = input("User: ")
#     messages.append({"role": "user", "content": content})
#
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
#
#     chat_response = completion.choices[0].message.content
#     print(f'ChatGPT: {chat_response}')
#     messages.append({"role": "assistant", "content": chat_response})
