The purpose of this project is to make audio files out of the text.

### How to use the program
- Run virtualenv venv_bookreader to create your new environment (called 'venv_bookreader' here)
- Execute command source venv_bookreader/bin/activate to enter the virtual environment
- Run pip install -r requirements.txt to install the requirements
- Add the file you want to read to the project root (file must have extension .txt) .
- Open script main.py in the project root and change parameter BOOK to the name of file you want to read .
- Execute the program using command: python main.py . Execution may take some time - around 3 minutes for a text of 6000 characters, depending on your computer.
- After the end of execution get audio file at the root of the project. It will have the name you mentioned in parameter BOOK and extension .wav.

### Useful links

- Silero models documentation: 
https://github.com/snakers4/silero-models/blob/master/README.md

- Coqui TTS documentation: 
https://github.com/coqui-ai/TTS
