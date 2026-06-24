from datetime import datetime
from image_generator import generate_image
from video_generator import create_video

try:
    prompt = input("Enter your video prompt: ")

    print("Generating image...")
    image_path = generate_image(prompt)

    print("Generating video...")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_video = f"videos/generated_video_{timestamp}.mp4"

    create_video(image_path, output_video)

    print("Done!")
    print("Saved to:", output_video)

except Exception as e:
    print("Error:", e)