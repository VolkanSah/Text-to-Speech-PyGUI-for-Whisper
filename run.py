# Text to Speech with Whisper (OpenAI)
# Simple GUI for daily work ;))
# Updates: https://github.com/VolkanSah/Text-to-Speech-PyGUI-for-Whisper
# Have fun :))
# Give me a star :Ö)

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import json

def generate_speech():
    api_key = 'You_OPENAI_API_KEY'
    text = text_input.get("1.0", tk.END).strip()
    voice = voice_var.get()
    url = 'https://api.openai.com/v1/audio/speech'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'model': 'tts-1',
        'input': text,
        'voice': voice
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raises an exception for HTTP errors

        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            with open(file_path, "wb") as f:
                f.write(response.content)
            status_label.config(text=f"Speech generated! Saved as '{file_path}'.")
        else:
            status_label.config(text="Save operation cancelled.")
    except requests.RequestException as e:
        error_message = f"Error generating speech: {str(e)}"
        status_label.config(text=error_message)
        show_error_dialog(error_message)

def show_error_dialog(message):
    error_window = tk.Toplevel(root)
    error_window.title("Error")
    error_window.geometry("400x200")

    error_text = tk.Text(error_window, wrap=tk.WORD, font=("Arial", 12))
    error_text.pack(expand=True, fill='both', padx=10, pady=10)
    error_text.insert(tk.END, message)
    error_text.config(state='disabled')  # Makes the text non-editable

    copy_button = tk.Button(error_window, text="Copy", command=lambda: copy_to_clipboard(message))
    copy_button.pack(pady=10)

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

root = tk.Tk()
root.title("Text-to-Speech with Whisper by Volkan Sah")
root.geometry("600x600")

text_input = tk.Text(root, height=10, width=50, font=("Arial", 14))
text_input.pack(pady=20)

voice_var = tk.StringVar(value="alloy")
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
voice_menu = ttk.OptionMenu(root, voice_var, voices[0], *voices)
voice_menu.pack(pady=10)

generate_button = tk.Button(root, text="Generate Speech", command=generate_speech)
generate_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500)
status_label.pack(pady=10)

root.mainloop()
