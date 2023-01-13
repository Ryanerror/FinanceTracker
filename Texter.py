from TexterH
import Manager

my_phone_number = "3477839604"

class texter:

    __slots__ = ["__info", "__number", ]

    def __init__(self, info,):
        self.__info = info
        self.__number = "3477839604@vtext.com"
        

    def set_info(self, new_info):
        self.__info = new_info
    
    def get_info(self):
        return self.__info

    def email_alert(self):
        user = "ryangarvin7@gmail.com"
        password = "bannqusamcgnsoul"
        my_messenger = Messenger(user, password)
        
        msg = SMS(my_phone_number, self.__number,
            "Here is your spending limit(this is not a scam its me Wensday)", 
                self.get_info())

        
        my_messenger.send_sms(msg, one_time=True)

    

def main():
    # manager = Manager()
    text = texter("test")
    text.email_alert()

if __name__ == "__main__":
    main()