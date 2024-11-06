from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[20:30, 12/6/2024] haseeb: hi how are you
[20:30, 12/6/2024] Albert: im good how about you
[20:31, 12/6/2024] haseeb: I am doing fine
[20:31, 12/6/2024] haseeb: send me some english songs
[20:31, 12/6/2024] haseeb: but wait
[20:31, 12/6/2024] haseeb: send me some hindi song also
[20:31, 12/6/2024] Albert: hold on
[20:31, 12/6/2024] haseeb: I know what you are about to send
[20:32, 12/6/2024] haseeb: 😂😂
[20:32, 12/6/2024] Alberts: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] haseeb: okok
[20:33, 12/6/2024] Albert: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named haseeb who speaks hindi as well as english. He is from Pak and is a coder. You analyze chat history and respond like haseeb"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)