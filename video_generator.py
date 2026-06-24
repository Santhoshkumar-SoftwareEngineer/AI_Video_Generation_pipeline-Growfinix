import cv2

def create_video(
    image_path,
    output_path,
    fps=10,
    duration=6,
    style="Zoom In"
):

    img = cv2.imread(image_path)

    height, width, _ = img.shape

    total_frames = fps * duration

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    for i in range(total_frames):

        if style == "Zoom In":
            scale = 1 + i * 0.003

        elif style == "Zoom Out":
            scale = 1.2 - i * 0.003

            if scale < 1:
                scale = 1

        resized = cv2.resize(
            img,
            None,
            fx=scale,
            fy=scale
        )

        h, w, _ = resized.shape

        start_x = (w - width) // 2
        start_y = (h - height) // 2

        frame = resized[
            start_y:start_y + height,
            start_x:start_x + width
        ]

        writer.write(frame)

    writer.release()