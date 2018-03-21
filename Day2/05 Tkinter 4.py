import tkinter as tk

def main():
    window = tk.Tk()

    def callback():
        print("Button clicked", var1.get())


    var1 =tk.StringVar()
    ent_msg = tk.Entry(window)
    ent_msg["textvariable"] = var1
    ent_msg.pack()
    btn = tk.Button(window, text="Click me", command=callback)
    btn.pack()
    window.mainloop()


if __name__ == '__main__':
    main()