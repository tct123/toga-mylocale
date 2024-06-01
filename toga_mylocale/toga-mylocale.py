from mylocale.TR import tr
import toga

platform = toga.platform.current_platform


def tr():
    if platform == "android":
        langcode = ""
