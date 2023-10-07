import tkinter as tk
from tkinter import filedialog
import shutil
import os  # Import the os module for file operations
from File_Details import file_details

# Create a tkinter window
root = tk.Tk()
root.title("Text File Upload Example")
root.geometry("750x1398")

# Function to handle file upload and copy the file to a directory
def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")],  # Specify allowed file types
        title="Select a Text File"
    )
    if file_path:
        # Specify the destination directory where you want to copy the file
        destination_directory = 'Encrypter'  # Replace with your actual destination directory

        # Use shutil to copy the selected file to the destination directory
        try:
            shutil.copy(file_path, destination_directory)
            print(f"File '{file_path}' copied to '{destination_directory}'")

            # Rename the copied file to "file_to_be_encrypted.txt"
            new_file_path = os.path.join(destination_directory, file_details()+"_decrypted"+".txt")
            a=os.rename(os.path.join(destination_directory, os.path.basename(file_path)), new_file_path)
        except Exception as e:
            print(f"Error copying file: {e}")

# Create a button for file upload
upload_button = tk.Button(root, text="Upload Text File", command=upload_file)
upload_button.pack()

# Start the tkinter main loop
root.mainloop()
