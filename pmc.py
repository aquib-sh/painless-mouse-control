import os
import env_setup_tools

if os.name == "posix":
    env_setup_tools.configure_posix_environment()

import sys
import pyautogui
import keyboard
import strings


class PainlessMouseController:
    def __init__(self) -> None:
        self.SPEED = 1
        self.VERBOSE = False

        pyautogui.FAILSAFE = False  # Do not crash if pointer gets out of screen

        self.KEYS = {"up": "up", "down": "down", "right": "right", "left": "left"}
        self.__set_preferences()

        if "--help" in sys.argv:
            print(strings.HELP_TEXT)
            sys.exit(0)

    def __digit_indx(self) -> int:
        """Find the index of digit in sys arguments"""
        for i in range(len(sys.argv)):
            arg = sys.argv[i]
            if arg.isdigit():
                return i
        return -1

    def __set_preferences(self) -> None:
        """Set preferences provided by the user."""
        if len(sys.argv) > 1:
            if "--verbose" in sys.argv:
                self.VERBOSE = True

            # set VIM navigation keys instead of arrow
            if "--vim" in sys.argv:
                self.KEYS["up"] = "k"
                self.KEYS["down"] = "j"
                self.KEYS["left"] = "h"
                self.KEYS["right"] = "l"

            if (dindx := self.__digit_indx()) != -1:
                self.SPEED = int(sys.argv[dindx])

    def traverse(self) -> None:
        """Traverse to specific X, Y position in relative to current.
        The speed of the movement can be increased by incrementing the SPEED constant.
        """
        movx = 0
        movy = 0
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift"):
            if keyboard.is_pressed(self.KEYS["up"]):
                movy = -10 * self.SPEED  # UP

            if keyboard.is_pressed(self.KEYS["down"]):
                movy = 11 * self.SPEED  # Down

            if keyboard.is_pressed(self.KEYS["left"]):
                movx = -20 * self.SPEED  # Left

            if keyboard.is_pressed(self.KEYS["right"]):
                movx = 20 * self.SPEED  # Right

        if movx != 0 or movy != 0:
            pyautogui.move(movx, movy)
            if self.VERBOSE:
                print(pyautogui.position())

    def jump(self) -> None:
        """Jumps a significant portion of screen either to left or right part"""
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("tab"):
            if keyboard.is_pressed("shift"):  # Jump backwards (left side)
                pyautogui.move(-350, 0)
            else:
                pyautogui.move(350, 0)  # Jump forwards (right side)

    def click(self) -> None:
        """Simply clicks on a location."""
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("space"):
            pyautogui.click()

    def run(self):
        if self.VERBOSE:
            print(strings.INTRO_TEXT)
        while True:
            self.traverse()
            self.click()
            self.jump()


if __name__ == "__main__":
    PainlessMouseController().run()
