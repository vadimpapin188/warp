import ctypes
import pystray
from PIL import Image
import webview

console_window = ctypes.windll.kernel32.GetConsoleWindow()


class Api:

    def __init__(self):
        self.window_name = "App"
        self.w = 800
        self.h = 600
        self.icon = None
        self.menu = None

    def set_window_name(self, name):
        self.window_name = name
        return name

    def set_size(self, w, h):
        self.w = w
        self.h = h
        return w, h

    def on_exit(self, icon, item):
        icon.stop()
        ctypes.windll.user32.ShowWindow(console_window, 5)

    def create_stray_menu(self, name_item):
        if name_item == "exit":
            self.menu = pystray.Menu(pystray.MenuItem('Exit', self.on_exit))
        else:
            print("WarpError: Invalid System tray menu name item")

    def create_stray_icon(self, name, des, icon_path):
        image = Image.open(icon_path)
        self.icon = pystray.Icon(name, image, des, self.menu)
        self.icon.run_detached()

    def hide_console(self):
        ctypes.windll.user32.ShowWindow(console_window, 0)

    def developer_mode(self):
        ctypes.windll.user32.ShowWindow(console_window, 5)


api = Api()
api.hide_console()

with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

webview.create_window(
    api.window_name,
    html=index,
    js_api=api,
    width=api.w,
    height=api.h,
)
webview.start()
