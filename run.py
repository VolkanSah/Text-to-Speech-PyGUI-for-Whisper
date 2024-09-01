# Text-to-Speech-PyGUI-for-Whisper by Volkan Sah
# Small Gui tool ;))
# Updates: https://github.com/VolkanSah/Text-to-Speech-PyGUI-for-Whisper/
import tkinter as tk
from tkinter import ttk
import requests
import json

# Function to send a request to the OpenAI API to generate speech from text
def generate_speech():
    api_key = 'sk-your key'  # Replace with your actual API key
    text = text_input.get("1.0", tk.END).strip()  # Get the text input from the user
    voice = voice_var.get()  # Get the selected voice from the dropdown menu
    url = 'https://api.openai.com/v1/audio/speech'  # OpenAI API endpoint for speech generation
    
    headers = {
        'Content-Type': 'application/json',  # Set the content type to JSON
        'Authorization': f'Bearer {api_key}'  # Add the API key for authorization
    }

    # Data to be sent in the API request
    data = {
        'model': 'tts-1',  # Model ID for text-to-speech
        'input': text,  # The text to be converted to speech
        'voice': voice  # The selected voice for the speech
    }

    # Sending the request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Handling the API response
    if response.status_code == 200:
        # If the response is successful, save the audio file as "speech.mp3"
        with open("speech.mp3", "wb") as f:
            f.write(response.content)
        status_label.config(text="Speech generated! Saved as 'speech.mp3'.")
    else:
        # If there's an error, display the error message
        status_label.config(text=f"Error generating speech: {response.text}")

# Create the main GUI window
root = tk.Tk()
root.title("Text-to-Speech with OpenAI")
root.geometry("600x400")  # Set the window size

# Text field for user input
text_input = tk.Text(root, height=10, width=50, font=("Arial", 14))
text_input.pack(pady=20)

# Dropdown menu for voice selection
voice_var = tk.StringVar(value="alloy")
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]  # List of available voices
voice_menu = ttk.OptionMenu(root, voice_var, voices[0], *voices)
voice_menu.pack(pady=10)

# Button to trigger speech generation
generate_button = tk.Button(root, text="Generate Speech", command=generate_speech)
generate_button.pack(pady=10)

# Status label to display messages to the user
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Start the main event loop for the GUI
root.mainloop()
