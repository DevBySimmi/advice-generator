<<<<<<< HEAD
# 🌟 Random Advice Generator 🌟

## 🚀 Overview
Looking for a quick dose of wisdom? This Python-based GUI application delivers random advice straight from the Advice Slip API! Built with Tkinter, it features an easy-to-use interface and a one-click copy option.

## ✨ Features
✅ Fetches insightful advice from `https://api.adviceslip.com/advice`  
✅ Uses threading for a smooth, lag-free experience  
✅ Copy advice to your clipboard with a single click  
✅ Lightweight and easy to use  
✅ Can be converted into a one-click executable for Windows & Mac  

## 🛠 Installation
### 📌 Prerequisites
- Python (3.x recommended)  
- Active internet connection  

### 📥 Install Dependencies
Run the following command to install the required dependencies:
```sh
pip install requests tkinter
```

## ▶️ How to Run
Launch the application using:
```sh
python main.py
```

## 🎯 How It Works
1️⃣ The app fetches a random piece of advice when started.  
2️⃣ Click **"Get Advice"** to retrieve a new one.  
3️⃣ Click **"Copy Advice"** to save it to your clipboard.  
4️⃣ Paste it anywhere and share the wisdom!  

## 🎯 Usage
- Open the application.
- Click **"Get Advice"** to receive a random thought-provoking tip.
- Click **"Copy Advice"** to save it and share with friends.

## 💻 Creating an Executable for One-Click Access
### 🖥️ Windows
1️⃣ Install `pyinstaller`:
```sh
pip install pyinstaller
```
2️⃣ Create an executable:
```sh
pyinstaller --onefile --noconsole main.py
```
3️⃣ The executable will be found inside the `dist/` folder. Move it to a preferred location.
4️⃣ Create a shortcut:
   - Right-click the `.exe` file and select **Create Shortcut**.
   - Move the shortcut to the Desktop or Taskbar for easy access.

### 🍏 macOS
1️⃣ Install `pyinstaller`:
```sh
pip install pyinstaller
```
2️⃣ Create an executable:
```sh
pyinstaller --onefile --windowed main.py
```
3️⃣ The `.app` file will be found inside the `dist/` folder. Move it to a convenient location.
4️⃣ Create a shortcut:
   - Drag the `.app` file to the Dock for quick access.

## 📜 License
This project is open-source and available under the **MIT License**.

---
💡 Get inspired with just a click! 🚀

=======
# advice-generator
A fun Python app for daily motivational advice.
>>>>>>> 55a7da7c732dfcb1af2de9e8f544cb5403dd7c71
