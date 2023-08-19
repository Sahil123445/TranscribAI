# transcribeWithPython

Uses OpenAi-whisper to transcribe audio files.
https://github.com/openai/whisper

Steps to run:
Step 1 : You need to have the latest version of Python installed. (Was tested on Python 3.10.6)
Step 2 : Visit https://pytorch.org/get-started/locally/ and look at the compute platform for the CUDA version. (Was tested with CUDA 11.7)
Step 3 : Visit the official Nvidia website (https://developer.nvidia.com/search?page=1&sort=relevance&term=CUDA%2011.7) and search for the CUDA version you found from the last step and install.
Step 4 : Go back to https://pytorch.org/get-started/locally/ and run the command present in a command prompt to install pytorch.
Step 5 : Install FFMPEG by visiting https://ffmpeg.org/download.html#build-windows, extract and create a PATH file in the Edit System Enviorment and verify it works by typing ffmpeg in command prompt.
Step 6 : Install whisper using two commands 1) pip install setuptools-rust
                                            2) pip install git+https://github.com/openai/whisper.git
Step 7 : Finally to run whisper and transcribe audio files, simply open command prompt in the audio file location or navigate to it, run the command : whisper (name of audio file) --(what size model you want to use)
                                                                                                                                                   Eg: whisper OverwatchAudioFile --model base

I have used https://www.youtube.com/watch?v=XX-ET_-onYU youtube video to understand and run it myself and I believe it is a good resource to learn
