import pyautogui
def get_cursor_position():
    x, y = pyautogui.position()
    return (x, y)
if __name__ == "__main__":
    position = get_cursor_position()
    print(f"Current cursor position: X={position[0]}, Y={position[1]}")