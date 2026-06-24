import requests

def generate_image(prompt):

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    response = requests.get(url)

    image_path = "assets/input_image.png"

    with open(image_path, "wb") as f:
        f.write(response.content)

    return image_path