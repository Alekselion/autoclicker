import keyboard
import pyautogui

pyautogui.FAILSAFE = False


def autoClicker(delay=0.001):
    """
    ENG:
    -- press 'a' to start autoclicker
    -- press 'd' to stop autoclicker
    -- press 'esc' to finish program
    
    RU:
    -- нажмите 'a' для запуска автокликера
    -- нажмите 'd' для остановки автокликера
    -- нажмите 'esc' для завершения программы
    """
    while True:
        if keyboard.is_pressed('a'):  # start
            while True:
                pyautogui.click(interval=delay)
                if keyboard.is_pressed('d'):  # stop
                    break
        if keyboard.is_pressed('esc'):  # exit
            break


if __name__ == '__main__':
    autoClicker()
