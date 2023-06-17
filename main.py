import tkinter as tk
import bot_data as main
import datetime

def load_accounts_name():
    items = main.get_accounts_directory()
    listbox.delete(0,tk.END)
    for item in items:
        try:
            main.make_request(item)
            now = datetime.datetime.now()
            listbox.insert(tk.END, item + ' - Updated ' + now.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            listbox.insert(tk.END, "OFF LINE")

def create_window():
    global listbox
    global countdown

    window = tk.Tk()
    window.title("Lords Mobile Bot")
    window.geometry("800x600")

    label = tk.Label(window, text="Contas")
    label.pack()

    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(window, text="Start Process", command=load_accounts_name)
    button.pack()

    countdown_label = tk.Label(window, text="Countdown: --")
    countdown_label.pack(side=tk.BOTTOM)

    def update_countdown():
        global countdown
        countdown -= 1
        countdown_label.config(text="Refresh: " + str(countdown))
        window.after(1000, update_countdown)
        if countdown == 0:
            countdown = 11
            load_accounts_name()

    countdown = 11
    window.after(1000, update_countdown)

    window.mainloop()

if __name__ == "__main__":
    create_window()