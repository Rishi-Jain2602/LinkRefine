from ..chain.llm import client

def profile_picture_optimizer(image_url):
    if image_url == '':
        return {"content":"Please consider adding a profile picture. A professional photo creates a strong first impression and builds trust with potential employers or connections, making your profile more approachable and credible."}
    completion = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": 
            [
                {
                    "type": "text",
                    "text": "Analyze the provided LinkedIn profile picture and suggest actionable improvements. Highlight the strengths and weaknesses of the image in terms of professionalism, approachability, and alignment with industry standards. Provide tips on how the user can enhance their LinkedIn profile picture to better represent themselves, such as posture, facial expression, background, lighting, or attire, to create a stronger professional presence."
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

# print(profile_picture_optimizer('https://media.licdn.com/dms/image/v2/D4D03AQFcR_yanjjhrQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1696502980766?e=1743638400&v=beta&t=wtyXAzbtCsaX7JFOLNpx4NAw9kfl8LE6HgawDDtk43M'))