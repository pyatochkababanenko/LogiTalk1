from customtkinter import *
import threading
from socket import *


class MainWindow(CTk):
   def __init__(self):
       super().__init__()
       self.geometry('400x300')
       self.label = None
       self.frame = CTkFrame(self, width=200, height=self.winfo_height())
       self.frame.pack_propagate(False)
       self.frame.configure(width=0)
       self.frame.place(x=0, y=0)
       self.is_show_menu = False
       self.speed_animate_menu = -5

       self.label = CTkLabel(self.frame, text='Ваше Ім`я')
       self.label.pack(pady=30)
       self.entry = CTkEntry(self.frame)
       self.entry.pack()
       self.label_theme = CTkOptionMenu(self.frame, values=['Темна', 'Світла'], command=self.change_theme)
       self.label_theme.pack(side='bottom', pady=20)
       self.theme = None
       self.btn = CTkButton(self, text='▶', command=self.toggle_show_menu, width=30)
       self.btn.place(x=0, y=0)
       self.menu_show_speed = 20

       self.chat_text = CTkTextbox(self, font=('Arial',14, 'bold'), state='disable')
       self.chat_field.place(x=0, y=0)

       self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
       self.message_entry.place(x=0, y=0)
       self.send_button = CTkButton(self, text='▶', width=50, height=40, command=self.send_message)
       self.send_button.place(x=0, y=0)


       self.username = 'asenko'
       try:
           self.sock = socket(AF_INET, SOCK_STREAM)
           self.sock.connect(('localhost', 8080))
           hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
           self.sock.send(hello.encode('utf-8'))
           threading.Thread(target=self.recv_message, daemon=True).start()
       except Exception as e:
           self.add_message(f"Не вдалося підключитися до сервера: {e}")

       self.adaptive_ui()

   def toggle_show_menu(self):
       if self.is_show_menu:
           self.is_show_menu = False
           self.speed_animate_menu *= -1
           self.btn.configure(text='▶')
           self.close_menu()
       else:
           self.is_show_menu = True
           self.speed_animate_menu *= -1
           self.btn.configure(text='<')
           self.show_menu()

           self.label = CTkLabel(self.menu_frame,text='iм`я')
           self.label.pack(pady=30)
           self.entry = CTkEntry(self.menu_frame)
           self.entry.pack()

   def show_menu(self:)
   self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
   if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:
       self.after(10, self.show_menu)
   elif self.menu_frame.winfo_width() >= 40 and not self.is_show_menu:
       self.after(10, self.show_menu)
       if self.label and self.entry:
           self.label.destroy()
           self.entry.destroy()



   def change_theme(self, value):
       if value == 'Темна':
           set_appearance_mode('dark')
       else:
           set_appearance_mode('light')

   def adaptive_ui(self):
       self.menu_frame.configure(height=self.winfo_height())
       self.chat_field.place(x=self.menu_frame.winfo_width())
       self.chat_field.configure(width=self.winfo_width() - self.menu_frame.winfo_width()
                                 height=self.winfo_height() - 40)
       self.send_button.place(x=self.winfo-width())

       self.message_input.configure(width=self.winfo_width()-self.frame.winfo_width()-self.send_button.winfo_width())
       self.message_input.place(x=self.frame.winfo_width(), y=self.winfo_height()-self.send_button.winfo_height())

       self.send_button.place(x=self.winfo_width()-self.send_button.winfo_width(), y=self.winfo_height()-self.send_button.winfo_height())

       self.after(20, self.adaptive_ui)


win = MainWindow()
win.mainloop()

