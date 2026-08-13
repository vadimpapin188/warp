# ⚡ Warp Framework

A lightweight desktop application framework powered by **Python** and **JavaScript** (built on top of `pywebview`). 

Warp allows you to build modern, fast desktop GUIs using standard Web technologies (HTML/CSS/JS) while giving your frontend access to native window management and system tray functionality through a simple asynchronous JavaScript API. 

**Framework has documentation.**

---

## 🚀 Features

- **Lightweight & Fast:** Uses the native system webview instead of bundling heavy browser engines.
- **Simple JS API:** Async functions to control window parameters, system tray, and developer tools out of the box.
- **Python Backend Integration:** Seamless bridge between Python logic and the JS frontend.

---

## 🛠 Project Structure

Place your frontend files along with `warp_api.js` in your working directory:

```text
├── main.py          # Core Python logic / Warp executor
├── warp_api.js      # JS bridge provided with Warp
├── index.html       # Your app's UI
└── app.js           # Your custom JS logic
