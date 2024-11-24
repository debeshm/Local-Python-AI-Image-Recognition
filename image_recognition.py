import ollama

res = ollama.chat(
    model = 'llava:7b',
    messages = [
        {
            'role': 'user',
            'content': 'Just extract 5 hashtags',
            'images': ['./image2.jpg']
        }
    ]
)

print(res['message']['content'])