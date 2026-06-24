import streamlit as st
from datetime import datetime
from image_generator import generate_image
from video_generator import create_video
import time

# Page configuration
st.set_page_config(page_title="AI Video Generation Pipeline")

# Title
st.title("🎬 AI Video Generation Pipeline")

# Prompt input
prompt = st.text_input(
    "Enter your video prompt",
    "slow-motion fireworks and gold glitter effects over 3D golden text"
)

# Settings
fps = st.slider("Frames Per Second (FPS)", 5, 30, 10)

duration = st.slider(
    "Video Duration (seconds)",
    3,
    10,
    6
)

animation_style = st.selectbox(
    "Animation Style",
    [
        "Zoom In",
        "Zoom Out"
    ]
)

# Generate button
if st.button("Generate Video"):

    start_time = time.time()

    # Save prompt history
    with open("history.txt", "a", encoding="utf-8") as history_file:
        history_file.write(prompt + "\n")

    # Generate image
    with st.spinner("Generating image..."):
        image_path = generate_image(prompt)

    # Show image
    st.subheader("Generated Image")
    st.image(image_path)

    # Timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_video = f"videos/generated_video_{timestamp}.mp4"

    # Generate video
    with st.spinner("Generating video..."):
        create_video(
            image_path,
            output_video,
            fps=fps,
            duration=duration,
            style=animation_style
        )

    st.success("Video generated successfully!")

    # Video preview
    with open(output_video, "rb") as video_file:
        video_bytes = video_file.read()

    st.subheader("Video Preview")
    st.video(video_bytes)

    # Download button
    with open(output_video, "rb") as file:
        st.download_button(
            label="⬇ Download Video",
            data=file,
            file_name=output_video.split("/")[-1],
            mime="video/mp4"
        )

    # Generation time
    end_time = time.time()

    st.info(
        f"Generation completed in {end_time - start_time:.2f} seconds"
    )