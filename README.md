# Educational Video Animator

Educational Video Animator is a Python tool that transforms static math equations into captivating animated video lessons. By leveraging OpenCV and Pillow for dynamic visuals, gTTS for AI-generated voice narration, and MoviePy to seamlessly merge audio and video, this project makes learning math engaging, interactive, and fun.

## Features

- **Animated Equation Reveal:** See equations appear step by step to help build understanding.
- **Dynamic Visuals:** Creative gradient backgrounds and custom text effects add visual flair.
- **Voiceover Narration:** gTTS produces clear, synchronized narration for every video.
- **Built-in Subtitles:** Subtitles are directly rendered onto each frame for additional clarity.
- **Open-Source & Extendable:** Modular code allows you to add new features like background music or custom animations.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **FFmpeg**: Download and install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.
  
### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SanthiNani/Educational-Video-Animator.git
   cd Educational-Video-Animator
   
2. **Install all dependencies:**

   ```bash
   pip install opencv-python pillow numpy gTTS moviepy
   ```
   Alternatively, use a requirements.txt file:
    ```
   opencv-python
   Pillow
   numpy
   gTTS
   moviepy
    ```

Usage
Run the main script:

 ```bash

python Education_animator.py
 ```
The tool will generate:

Voiceovers in the audios/ folder

Intermediate videos in the videos/ folder

Final merged videos (with subtitles) in the final_videos/ folder

How It Works
Voiceover Generation: gTTS creates a narration file for each equation.

Frame Animation: The equation is broken down and animated frame-by-frame, rendered over creative gradient backgrounds.

Audio/Video Merging: MoviePy synchronizes the generated audio with the animated video, and subtitles are overlaid for clarity.

Contributing
Contributions, feature requests, and bug reports are welcome! Please fork the repository, create a feature branch, and open a pull request. For major changes, open an issue first to discuss your ideas.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Contact
For questions or suggestions, please contact Peddapati Santhi Raju.
email : santhinani364@gmail.com




