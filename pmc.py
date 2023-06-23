from argparse import ArgumentParser, RawTextHelpFormatter
import os
import env_setup_tools

if os.name == "posix":
    env_setup_tools.configure_posix_environment()

import pyautogui
import keyboard
import strings

pyautogui.FAILSAFE = False  # Do not crash if pointer gets out of screen


class PainlessMouseController:
    """Allows basic mouse movements using the keyboard."""

    # Movement: jump values for various directions
    BASE_MOVE_U, BASE_MOVE_D, BASE_MOVE_R, BASE_MOVE_L = -10, 11, 20, -20
    FAST_MOVE_R, FAST_MOVE_L = 350, -350
    # Key mappings:
    KEYS_ARROWS = {"up": "up", "down": "down", "right": "right", "left": "left"}
    KEYS_VIM = {"up": "k", "down": "j", "right": "l", "left": "h"}

    def __init__(self, speed: int = 1, verbose: bool = False, vim_mode: bool = False):
        """Default initializer.
        :param speed: mouse speed, defaults to 1
        :param verbose: verbosity setting, defaults to False
        :param vim_mode: set to True if you want to use VIM-like keys, defaults to False
        """
        self.speed, self.verbose = speed, verbose
        self.keys = self.KEYS_VIM if vim_mode else self.KEYS_ARROWS

    def traverse(self) -> None:
        """Moves the cursor to a new position according to mouse movement speed."""
        movx, movy = 0, 0
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift"):
            if keyboard.is_pressed(self.keys["up"]):
                movy = self.BASE_MOVE_U * self.speed

            if keyboard.is_pressed(self.keys["down"]):
                movy = self.BASE_MOVE_D * self.speed

            if keyboard.is_pressed(self.keys["left"]):
                movx = self.BASE_MOVE_L * self.speed

            if keyboard.is_pressed(self.keys["right"]):
                movx = self.BASE_MOVE_R * self.speed

        if movx != 0 or movy != 0:
            pyautogui.move(movx, movy)
            if self.verbose:
                print(pyautogui.position())

    def jump(self) -> None:
        """Jumps a significant portion of screen either to left or right part"""
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("tab"):
            if keyboard.is_pressed("shift"):  # Jump backwards (left side)
                pyautogui.move(self.FAST_MOVE_L, 0)
            else:
                pyautogui.move(self.FAST_MOVE_R, 0)  # Jump forward (right side)

    def click(self) -> None:
        """Simply clicks on a location."""
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("space"):
            pyautogui.click()

    def run(self):
        """Main run method."""
        if self.verbose:
            print(strings.INTRO_TEXT)
        while True:
            self.traverse()
            self.click()
            self.jump()


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="python pmc.py",
        description=strings.SUMMARY,
        epilog=strings.EXAMPLES_AND_NOTES,
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument("--speed", type=int, default=1, help=strings.SPEED)
    parser.add_argument("--vim", action="store_true", help=strings.VIM)
    parser.add_argument("--verbose", action="store_true", help=strings.VERBOSE)
    args = parser.parse_args()
    PainlessMouseController(
        speed=args.speed, verbose=args.verbose, vim_mode=args.vim
    ).run()
