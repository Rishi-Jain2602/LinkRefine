from ..chain.llm import client

def backgrd_picture_optimizer(image_url):
    if image_url == '':
        return {"content":"Please add a background picture. A well-designed background image adds personality and highlights your professional brand, making your profile visually appealing and helping you stand out from others."}
    completion = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": 
            [
                {
                    "type": "text",
                    "text": "Analyze the provided LinkedIn background picture of user and suggest actionable improvements. Highlight the strengths and weaknesses of the image in terms of professionalism, approachability, and alignment with industry standards. Provide tips on how the user can enhance their profile background picture to better represent themselves, such as posture, facial expression, background, lighting, or attire, to create a stronger professional presence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"{image_url}"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    )
    return completion.choices[0].message

