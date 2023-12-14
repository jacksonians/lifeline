import requests
import json
import shutil
from PIL import Image, ImageTk
import io

mainpageImg = "images/mainpage.jpg"
mainpageTxt = "Welcome to LifeLine, a mental health & stress relief app! We wil be here for you in times of stress or to stimulate your motivation. Please choose how you are feeling on the sidebar to the left."
featuresData = [
    "- Utlizes ZenQuotesAPI for motivational quote generation",
        "- Helps improve mental health, depression, stress, and cures lack of motivation",
            "- Made for stressed students by a stressed student"
]

depData = {
    "Do not give the past the power to define your future.": "Unknown",
    "Depression is your body saying, 'I don't want to be this character anymore. I don't want to hold up this avatar that you've created in the world. It's too much for me,' You should think of the word 'depressed' as 'deep rest.' Your body needs to be depressed. It needs deep rest from the character that you've been trying to play.": "Ariana Grande",
    "I found that with depression, one of the most important things you can realize is that you're not alone. You're not the first to go through it, you're not gonna be the last to go through it": "Dwayne The Rock Johnson",
}

burntData = {
    "Well done is better than well said": "Benjamin Franklin",
    "You must be the change you wish to see in the world.": "Mahatma Gandhi",
    "Do one thing every day that scares you.": "Eleanor Roosevelt",
}

stressData = {
    "If you are distressed by anything external, the pain is not due to the thing itself but to your own estimate of it; and this you have the power to revoke at any moment.": "Marcus Aurelius",
    "Yesterday is gone. Tomorrow has not yet come. We have only today. Let us begin.": "Mother Teresa",
    "In the middle of difficulty lies opportunity.": "Albert Einstein",
}

philData = {
    "To live is to suffer, to survive is to find some meaning in the suffering.": "Friedrich Nietzsche",
    "I think, therefore I am.": "René Descartes",
    "I know that I know nothing.": "Socrates",
}

def AddImage(feelingImg):
    if feelingImg == "Depressed":
        category = 'wildlife'
    elif feelingImg == "Stressed":
        category = 'nature'
    elif feelingImg == "Burnt Out":
        category = 'city'
    else:
        category = "nature"
    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'igF6X1s2H3RI+9mNBEdYMw==f2GbQ6KgHO680sym', 'Accept': 'image/jpg'}, stream=True)
    if response.status_code == requests.codes.ok:
        with open('img.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error:", response.status_code, response.text)


# def display_image(category):
#     # make a request to the Unsplash API to get a random image
#     url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=N8LfRHlG13Tn8fwwrLnej2_fXMCsilrro__UFl7ICfY"
#     data = requests.get(url).json()
#     img_data = requests.get(data["urls"]["regular"]).content

#     photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
#     # label.config(image=photo)
#     # label.image = photo





# #quote for depressed
# api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format("happiness")
# response  = requests.get(api_url, headers={'X-Api-Key': 'igF6X1s2H3RI+9mNBEdYMw==f2GbQ6KgHO680sym'})
# if response.status_code == requests.codes.ok:
#     depData = response.text
# else:
#     print("Error:", response.status_code, response.text)


# #quote for burnt out
# api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format("inspirational")
# response  = requests.get(api_url, headers={'X-Api-Key': 'igF6X1s2H3RI+9mNBEdYMw==f2GbQ6KgHO680sym'})
# if response.status_code == requests.codes.ok:
#     burntData = response.text
# else:
#     print("Error:", response.status_code, response.text)


# #quote for stressed
# api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format("dreams")
# response  = requests.get(api_url, headers={'X-Api-Key': 'igF6X1s2H3RI+9mNBEdYMw==f2GbQ6KgHO680sym'})
# if response.status_code == requests.codes.ok:
#     stressData = response.text
# else:
#     print("Error:", response.status_code, response.text)


# #quote for philosophical
# api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format("knowledge")
# response  = requests.get(api_url, headers={'X-Api-Key': 'igF6X1s2H3RI+9mNBEdYMw==f2GbQ6KgHO680sym'})
# if response.status_code == requests.codes.ok:
#     philData = response.text
# else:
#     print("Error:", response.status_code, response.text)
