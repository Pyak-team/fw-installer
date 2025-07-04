import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import os

def check_adb():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "List of devices" in result.stdout:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

    def check_adb():
        try:
            result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            if "List of devices" in result.stdout:
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def reboot_bootloader():
            try:
                result = subprocess.run(["adb", "reboot", "bootloader"], capture_output=True, text=True)
                if "List of devices" in result.stdout:
                    return True
                else:
                    return False
            except FileNotFoundError:
                return False

def flashing_3():
                try:
                result = subprocess.run(["fastboot", "flash", 'vendor_boot'], capture_output=True, text=True)
                if "Successful" in result.stdout:
                    return True
                else:
                    return False
            except FileNotFoundError:
                return False

def flashing_2():
                try:
                result = subprocess.run(["fastboot", "flash", "dtbo"], capture_output=True, text=True)
                if "Successful" in result.stdout:
                    return True
                else:
                    return False
                except FileNotFoundError:
                return False
def flashing_1():
            try:
                result = subprocess.run(["fastboot", "flash", "boot"], capture_output=True, text=True)
                if "Successful" in result.stdout:
                    return True
                else:
                    return False
            except FileNotFoundError:
                return False


def check_device():
    output = run_adb_command("devices")
    text_output.insert(tk.END, f":\n{output}\n")

def reboot_device():
    output = run_adb_command("reboot")
    text_output.insert(tk.END, "Rebooting...\n")

def take_screenshot():
    screenshot_path = "Screenshot.png"
    run_adb_command(f"exec-out screencap -p > {screenshot_path}")
    text_output.insert(tk.END, f"Скриншот сохранён: {os.path.abspath(screenshot_path)}\n")

def install_apk():
        output = run_adb_command(f" {file_path}")
        text_output.insert(tk.END, f"Установка APK:\n{output}\n")

root = tk.Tk()
root.title("ADB GUI Tool")
root.geometry("500x400")

if not check_adb():
    messagebox.showerror("Ошибка", "ADB не найден! Убедитесь, что он установлен и добавлен в PATH.")
    root.destroy()
    exit()

text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text_output.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

btn_check = tk.Button(button_frame, text="ADB devices", command=check_device)
btn_check.grid(row=0, column=0, padx=5)

btn_check = tk.Button(button_frame, text="Reboot to Bootloader", command=check_device)
btn_check.grid(row=3, column=0, padx=5)

btn_check = tk.Button(button_frame, text="Fastboot devices", command=check_device)
btn_check.grid(row=0, column=0, padx=5)

btn_reboot = tk.Button(button_frame, text="Flash boot", command=reboot_device)
btn_reboot.grid(row=0, column=1, padx=5)

btn_screenshot = tk.Button(button_frame, text="Flash dtbo", command=take_screenshot)
btn_screenshot.grid(row=0, column=2, padx=5)

btn_install = tk.Button(button_frame, text="Flash vendor_boot", command=install_apk)
btn_install.grid(row=0, column=3, padx=5)

btn_install = tk.Button(button_frame, text="Reboot to recovery", command=install_apk)
btn_install.grid(row=0, column=3, padx=5)

btn_install = tk.Button(button_frame, text="Sideload frimware", command=install_apk)
btn_install.grid(row=3, column=3, padx=5)

btn_install = tk.Button(button_frame, text="Reboot", command=install_apk)
btn_install.grid(row=3, column=1, padx=5)

root.mainloop()