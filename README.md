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

## Steps to Create a systemctl .service File on Linux

Follow these steps to create a `.service` file for your service:

1. Open a terminal your Linux system.

2. Navigate to the appropriate directory where `.service` files are stored. On most systems, this is typically `/etc/systemd/system/`.

   ```bash
   cd /etc/systemd/system/
   ```

3. Create a new `.service` file using a text editor (e.g., `nano`, `vim`).

   ```bash
   sudo nano pmc.service
   ```

4. In the text editor, add the following content to the `.service` file:

   ```ini
   [Unit]
   Description=Painless Mouse Controller
   After=multi-user.target
   
   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/painless-mouse-control/pmc.py --verbose 8
   WorkingDirectory=/path/to/your/painless-mouse-control
   User=root
   Group=root
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   ```

   Modify the content to fit your specific service:
   - Modify `/path/to/your/` to the actual path of your painless-mouse-controller's directory.
   - Customize other options within the `[Service]` section as per your requirements. You can explore additional options in the systemd documentation.

5. Save the file and exit the text editor.

6. Run the following command to reload the systemd daemon and make it aware of the new `.service` file:

   ```bash
   sudo systemctl daemon-reload
   ```

7. Start your service using the `systemctl` command:

   ```bash
   sudo systemctl start pmc
   ```

8. Verify that your service is running correctly:

   ```bash
   sudo systemctl status pmc
   ```

   This command will display the current status of your service.

9. Enable your service to start automatically at boot:

    ```bash
    sudo systemctl enable pmc
    ```

    This will create the necessary symlinks to ensure your service starts automatically.

Congratulations! You have successfully created a `.service` file for `systemctl` and started your custom service.

## Managing the Service

Now that your service is set up, you can use various `systemctl` commands to manage it:

- To start the service: `sudo systemctl start pmc`
- To stop the service: `sudo systemctl stop pmc`
- To restart the service: `sudo systemctl restart pmc`
- To check the status of the service: `sudo systemctl status pmc`
- To enable the service to start at boot: `sudo systemctl enable pmc`
- To disable the service from starting at boot: `sudo systemctl disable pmc`

For more advanced usage and additional options, refer to the `systemctl` documentation.


## Contact

For any questions or feedback regarding the Painless Mouse Controller, feel free to reach out to me at [aquib-shaikh@outlook.com](mailto:aquib-shaikh@outlook.com)