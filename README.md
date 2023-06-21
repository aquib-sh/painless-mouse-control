# Painless Mouse Controller
Tired of dragging your right hand to the mouse? This tool allows you to control your mouse pointer without leaving your keyboard



The Painless Mouse Controller is a Python tool that allows you to control your mouse cursor and perform mouse clicks using keyboard shortcuts. This tool utilizes the `pyautogui` and `keyboard` libraries to provide easy mouse control without the need for manual mouse movements.
</br><b>Note</b>: Currently the script has only been developed and tested on Linux

## Prerequisites

Before using the Painless Mouse Controller, make sure you have the following requirements:

- Python 3.x installed on your system.
- The `pyautogui` and `keyboard` libraries installed. You can install them using the following commands:

  - For Windows:
    ```
    pip install pyautogui keyboard
    ```

  - For Linux and macOS:
    ```
    sudo pip3 install pyautogui keyboard
    ```

## Getting Started

To get started with the Painless Mouse Controller, follow these steps:

1. Download the file `pmc.py` from the provided location.

2. Open a terminal or command prompt with elevated privileges (using `sudo` on Linux and macOS) and navigate to the directory where the `pmc.py` file is located.

3. Run the Python script:
   - For Windows:
     ```
     python pmc.py
     ```
   - For Linux and macOS:
     ```
     sudo python3 pmc.py
     ```

   By default, the script will start without any verbose output.

## Usage

The Painless Mouse Controller provides the following functionalities:

### Mouse Cursor Movement

- Press and hold `Ctrl` + `Shift` while using the following keys to move the mouse cursor:

  - `Up arrow` or `k` (if VIM mode is enabled): Move the cursor upwards.
  - `Down arrow` or `j` (if VIM mode is enabled): Move the cursor downwards.
  - `Left arrow` or `h` (if VIM mode is enabled): Move the cursor to the left.
  - `Right arrow` or `l` (if VIM mode is enabled): Move the cursor to the right.

  Note: The cursor movement speed can be adjusted by specifying a speed parameter when running the script. For example:
  ```
  python pmc.py 4
  ```
  This sets the speed to 4, making the cursor movement faster.

### Mouse Click

- Press and hold `Ctrl` + `Space` to perform a mouse click at the current cursor position.

### Jump
- Jump a significant portion of the screen either to the left or right.

    - Hold `Ctrl` and press:
        - `Shift` + `Tab`: Jump backwards (to the left side).
        - `Tab`: Jump forwards (to the right side).

## Customization

The Painless Mouse Controller provides some customization options through command-line arguments:

- `--verbose`: Enables verbose output, which displays the current cursor position.
  ```
  python pmc.py --verbose
  ```

- `--vim`: Sets the navigation keys to VIM mode, using `k`, `j`, `h`, and `l` instead of arrow keys.
  ```
  python pmc.py --vim
  ```

- `<speed>`: Sets the cursor movement speed. Replace `<speed>` with an integer value. Higher values make the cursor movement faster.
  ```
  python pmc.py 10
  ```

Note: Multiple command-line arguments can be used together. For example:
```
python pmc.py --verbose --vim 8
```

## Exiting the Program

To exit the Painless Mouse Controller, simply close the terminal or command prompt where the script is running.


## Contact

For any questions or feedback regarding the Painless Mouse Controller, feel free to reach out to me at [aquib-shaikh@outlook.com](mailto:aquib-shaikh@outlook.com)