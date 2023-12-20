import tkinter as tk
import random


def generate_zalgo(text, intensity):
    zalgo_chars = [chr(i) for i in range(768, 814)]
    return ''.join(
        c + ''.join(random.choice(zalgo_chars) for _ in range(int(intensity))) if c.isalnum() else c for c in text)


def update_text(*args):
    intensity = intensity_scale.get()
    original_text = text_entry.get()
    zalgo_text.set(generate_zalgo(original_text, intensity))


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(zalgo_text.get())


root = tk.Tk()
root.title("Zalgo font generator")
root.geometry("640x480")

zalgo_text = tk.StringVar()

text_entry_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
text_entry_frame.pack(pady=10, padx=10, fill="x")
text_entry = tk.Entry(text_entry_frame)
text_entry.pack(expand=True, fill="both")

intensity_scale = tk.Scale(root, from_=0, to=10, orient="horizontal", command=update_text)
intensity_scale.pack()

result_label_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
result_label_frame.pack(pady=10, padx=10, fill="both", expand=True)
result_label = tk.Label(result_label_frame, textvariable=zalgo_text, wraplength=620)
result_label.pack(expand=True, fill="both")

copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

text_entry.bind("<KeyRelease>", update_text)

root.mainloop()
