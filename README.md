Touken Ranbu Auto-Clicker

A simple Python-based auto-clicker for Touken Ranbu

🛠️ Requirements

- Python 3.x  
- pynput
- pyautogui

Install dependencies using pip:

pip install pynput pyautogui

Install dependencies using py:

py -m install pynput pyautogui

🚀 Usage

1. Run the script:

py auto_clicker.py

2. Use the following hotkeys:
   - `*`: Start or pause the auto-clicker.
   - `~`: Exit the program.

⚙️ Customization

You can adjust the click position by modifying these variables in the script:

xaxis = 1314  # X-coordinate of the click
yaxis = 680   # Y-coordinate of the click

You can use cursor_location_detector.py to find the x-axis and y-axis of the location you want to auto-click

py cursor_location_detector.py

❗ Notes

- Make sure your screen resolution and target application match the coordinates.
- Run with appropriate permissions if your OS restricts simulated input.
