
import tkinter
import tkinter.messagebox
import customtkinter
import Manager



class App:

    __slots__ = ["__login", "__tracker" ]
    
    def __init__ (self):
       self.__login = customtkinter.CTk()
       self.__tracker = customtkinter.CTk()
   
    
    def config(self, window):
        
        window._apply_window_scaling(100)
        window.title("SpendingTracker")
        
        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue") # Themes: "blue" (standard), "green", "dark-blue"
    
    
    def login(self):  
        def vailidate():
            if text_1.get() == "7532":
                move_on()
              
        def move_on():
            self.tracker()
            frame_1.quit()
            
          
          
        self.config(self.__login)
                
        frame_1 = customtkinter.CTkFrame(master=self.__login)
        frame_1.pack(pady=20, padx=100, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, text="Ryan \n Enter Your Password To Access The \nSpending Tracker", font=customtkinter.CTkFont(size=25, weight="bold"),  justify=tkinter.CENTER)
        label_1.pack(pady=10, padx=10)
        
        button_2 = customtkinter.CTkButton(master=frame_1, command=quit, text="Quit")
        button_2.pack(pady=40, padx=10)

        frame_2 = customtkinter.CTkFrame(master=self.__login)
        frame_2.pack(pady=20, padx=100, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_2, text="Enter The Password", font=customtkinter.CTkFont(size=25, weight="bold"),  justify=tkinter.CENTER)
        label_1.pack(pady=10, padx=10)
        
        text_1 = customtkinter.CTkEntry(master=frame_2, width=200, height=40)
        text_1.pack(pady=10, padx=10)
        
       
        button_1 = customtkinter.CTkButton(master=frame_2, command=vailidate, text="Enter")
        button_1.pack(pady=10, padx=10)
        
        self.__login.mainloop()
        
    
    def tracker(self):
        money = Manager.Manager()
        self.config(self.__tracker)
        
        frame_1 = customtkinter.CTkFrame(master=self.__tracker)
        frame_1.pack(pady=20, padx=100, fill="both", expand=True, anchor="e")
        
        
        label_1 = customtkinter.CTkLabel(master=frame_1, text="Heres Your Finances Ryan", font=customtkinter.CTkFont(size=25, weight="bold"),  justify=tkinter.CENTER)
        label_1.pack(pady=10, padx=10)
        
        label_2 = customtkinter.CTkLabel(master=frame_1, text="My Money: $" + str(round(money.get_My_Money(), 2)), justify=tkinter.LEFT)
        label_2.pack(pady=10, padx=10)
        progressbar_1 = customtkinter.CTkProgressBar(master=frame_1,)
        progressbar_1.set(money.get_My_Money())
        progressbar_1.pack(pady=10, padx=10)
        
        label_3 = customtkinter.CTkLabel(master=frame_1, text="Investments: $" + str(round(money.get_Investments(), 2)), justify=tkinter.LEFT)
        label_3.pack(pady=10, padx=10)
        progressbar_2 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_2.set(money.get_Investments())
        progressbar_2.pack(pady=10, padx=10)
        
        label_4 = customtkinter.CTkLabel(master=frame_1, text="Food: $" + str(round(money.get_Food(), 2)), justify=tkinter.LEFT)
        label_4.pack(pady=10, padx=10)
        progressbar_3 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_3.set(money.get_Food())
        progressbar_3.pack(pady=10, padx=10)

        label_5 = customtkinter.CTkLabel(master=frame_1, text="Fun: $" + str(round(money.get_Fun(), 2)), justify=tkinter.LEFT)
        label_5.pack(pady=10, padx=10)
        progressbar_4 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_4.set(money.get_Fun())
        progressbar_4.pack(pady=10, padx=10)
        
        label_6 = customtkinter.CTkLabel(master=frame_1, text="Car Parts: $" + str(round(money.get_Car_Parts(), 2)), justify=tkinter.LEFT)
        label_6.pack(pady=10, padx=10)
        progressbar_5 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_5.set(money.get_Car_Parts())
        progressbar_5.pack(pady=10, padx=10)
        
        label_7 = customtkinter.CTkLabel(master=frame_1, text="Coffee: $" + str(round(money.get_Coffee(), 2)), justify=tkinter.LEFT)
        label_7.pack(pady=10, padx=10)
        progressbar_6 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_6.set(money.get_Coffee())
        progressbar_6.pack(pady=10, padx=10)

        label_8 = customtkinter.CTkLabel(master=frame_1, text="Disney: $" + str(round(money.get_Disney(), 2)), justify=tkinter.LEFT)
        label_8.pack(pady=10, padx=10)
        progressbar_7 = customtkinter.CTkProgressBar(master=frame_1)
        progressbar_7.set(money.get_Disney())
        progressbar_7.pack(pady=10, padx=10)
        
        button_1 = customtkinter.CTkButton(master=frame_1, command=quit, text="Transfer")
        button_1.pack(pady=40, padx=10)
        
        button_1 = customtkinter.CTkButton(master=frame_1, command=quit, text="Quit")
        button_1.pack(pady=40, padx=10)
        
        self.__tracker.mainloop()
    
    


def main():
    app = App()
    app.login()
   
    

if __name__ == "__main__":
    main()
