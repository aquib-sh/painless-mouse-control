import os


def configure_posix_environment():
    """Configures the environment variables for POSIX environment."""
    os.environ["DISPLAY"] = ":0"
    if "XAUTHORITY" not in os.environ:
        print("not found now we are setting")
        home_dir = os.path.expanduser("~")
        run_user_dir = os.path.join("/run/user", str(os.getuid()))

        xauth_home_dir = os.path.join(home_dir, ".Xauthority")

        if os.path.exists(xauth_home_dir):
            os.environ["XAUTHORITY"] = xauth_home_dir
        elif home_dir == "/root":
            for item in os.listdir(home_dir):
                if item.startswith(".xauth"):
                    os.environ["XAUTHORITY"] = os.path.join(home_dir, item)
                    break
        else:
            for item in os.listdir(run_user_dir):
                if item.startswith("xauth_"):
                    os.environ["XAUTHORITY"] = os.path.join(run_user_dir, item)
                    break
