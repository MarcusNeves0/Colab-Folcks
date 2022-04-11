from tkinter import *
import webbrowser

def openlink(url):
    webbrowser.open_new(url)

root = Tk()
root.geometry("230x100")

Facebook = Label(root, text="Facebook Profile", fg="blue", cursor="hand2")
Facebook.pack()
Facebook.bind("<Button-1>", lambda e: openlink("https://m.facebook.com/profile.php"))

Google = Label(root, text="Google Search", fg="green", cursor="hand2")
Google.pack()
Google.bind("<Button-1>", lambda e: openlink("https://www.google.com.br"))

Youtube = Label(root, text="Youtube", fg="red", cursor="hand2")
Youtube.pack()
Youtube.bind("<Button-1>", lambda e: openlink("https://www.youtube.com"))

Creditos = Label(root, text="Créditos", fg="black", cursor="hand2")
Creditos.pack()
Creditos.bind("<Button-1>", lambda e: openlink("https://github.com/MarcusNeves0"))

root.mainloop()
