# transcribeWithPython

Utilize the OpenAI Whisper library to transcribe audio files efficiently.
For more details about Whisper, check the official repository. (https://github.com/openai/whisper)

Installation and Usage:

Step 1 - Python Installation: Ensure you have the latest version of Python. The project was tested on Python 3.10.6.

Step 2 - PyTorch and CUDA:
Visit the PyTorch official setup page (https://pytorch.org/get-started/locally/) and identify the compatible CUDA version. This project was validated with CUDA 11.7.
Navigate to the official Nvidia website and download the appropriate CUDA version you identified earlier. Proceed with the installation.

Step 3 - PyTorch Installation: Return to the PyTorch setup page and execute the provided command in your terminal or command prompt to install PyTorch.

Step 4 - FFMPEG Installation: Download FFMPEG for Windows from this link https://ffmpeg.org/download.html#build-windows. After extracting the files, add the path to the bin directory to your system's PATH environment variable.
To confirm the successful installation, type ffmpeg in the command prompt. It should recognize the command.

Step 5 - Whisper Installation: Install whisper using two commands Run,  1) pip install setuptools-rust
                                                                  Then, 2) pip install git+https://github.com/openai/whisper.git
                                                                  
Step 6 - Transcribing Audio: To transcribe audio files using Whisper, navigate to the directory containing your audio file in the command prompt.
Execute the command: whisper [name of audio file] --model [model size]
Example: whisper OverwatchAudioFile.mp3 --model base

Additional Resources:
The tutorial video here https://www.youtube.com/watch?v=XX-ET_-onYU was instrumental in understanding and setting up this project and serves as a valuable resource for newcomers.

