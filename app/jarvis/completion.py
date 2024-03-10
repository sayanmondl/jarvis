def get_response(client, text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, your name is jarvis, if you are said to open a website, you are going to return link to the website only(no text along with it)",
            },
            {
                "role": "user",
                "content": "Open amazon",
            },
            {
                "role": "assistant",
                "content": "https://www.amazon.com/",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )
    return response.choices[0].message.content
