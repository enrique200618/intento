
from moviepy.editor import ImageSequenceClip

def generate_video_from_images(images, fps=24):
    clip = ImageSequenceClip(images, fps=fps)
    video_path = "output_video.mp4"
    clip.write_videofile(video_path, codec="libx264")
    return video_path
