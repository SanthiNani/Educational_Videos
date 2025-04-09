import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

# Create folders if not exist
os.makedirs("videos", exist_ok=True)
os.makedirs("audios", exist_ok=True)
os.makedirs("final_videos", exist_ok=True)

def text_to_speech(text, filename):
    tts = gTTS(text)
    tts.save(filename)
    print(f"✅ Voiceover saved: {filename}")

def generate_gradient_bg(width, height, start_color, end_color):
    base = Image.new("RGB", (width, height), start_color)
    top_r, top_g, top_b = ImageColor.getrgb(start_color)
    bot_r, bot_g, bot_b = ImageColor.getrgb(end_color)

    draw = ImageDraw.Draw(base)
    for y in range(height):
        r = int(top_r + (bot_r - top_r) * y / height)
        g = int(top_g + (bot_g - top_g) * y / height)
        b = int(top_b + (bot_b - top_b) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return base

def create_animation_sequence(equation, output_path, subtitle_text=None, eq_index=0):
    frames = []
    frame_width, frame_height = 1280, 720
    font = ImageFont.truetype("arial.ttf", 80)

    background_colors = [
        "#FFD6E8", "#C5FAD5", "#FFEDD5", "#E0F2FE", "#F5D0FE",
        "#FFF3C4", "#D1FADF", "#FDE2FF", "#E4EFFF", "#FFDFD3",
    ]
    base_bg_color = background_colors[eq_index % len(background_colors)]

    steps = [equation[:i+1] for i in range(len(equation))]

    for text in steps:
        start_color = base_bg_color
        end_color = "#FFFFFF"  # fade to white for subtle gradient
        img = generate_gradient_bg(frame_width, frame_height, start_color, end_color)
        draw = ImageDraw.Draw(img)

        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (frame_width - text_width) // 2
        text_y = (frame_height - text_height) // 2

        draw.text((text_x, text_y), text, font=font, fill="black")

        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        frames.append(frame)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 6, (frame_width, frame_height))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"✅ Video saved: {output_path}")

def merge_audio_video(video_path, audio_path, output_path, subtitle_text=None):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    video_clip = video_clip.subclip(0, min(video_clip.duration, audio_clip.duration))
    final = video_clip.set_audio(audio_clip)

    final.write_videofile(output_path, codec='libx264', audio_codec='aac')

def generate_all_sequences():
    equations = [
        "1 + 1 = 2",
        "2 × 3 = 6",
        "4 ÷ 2 = 2",
        "5 − 3 = 2",
        "3² = 9",
        "√16 = 4"
    ]

    for i, eq in enumerate(equations):
        audio_path = f"audios/voice_seq_{i}.mp3"
        video_path = f"videos/video_seq_{i}.mp4"
        final_path = f"final_videos/final_seq_{i}.mp4"

        print(f"🔊 Generating voiceover for: {eq}")
        text_to_speech(eq, audio_path)

        print(f"🎞 Creating animation for: {[eq[:j+1] for j in range(len(eq))]}")
        create_animation_sequence(eq, video_path, subtitle_text=eq, eq_index=i)

        merge_audio_video(video_path, audio_path, final_path)

if __name__ == "__main__":
    generate_all_sequences()
