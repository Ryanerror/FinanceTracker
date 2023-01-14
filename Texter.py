from pushnotifier import PushNotifier as pn
import Manager

User_Name = 'ryangarvin19'
Password = 'Spongebob,101'
Application_Name = 'com.ryangfinancetracker.app'
API_Key = 'B5YA6V2VBDE7DBV46V75B63CVB5YA68B2DBYFFBTTB'

class texter:

    __slots__ = ["__info"]

    def __init__(self, info):
        self.__info = info
        

    def set_info(self, new_info):
        self.__info = new_info
    
    def get_info(self):
        return self.__info

    def notify(self):
       notifer = pn.PushNotifier(User_Name, Password, Application_Name, API_Key)
       notifer.send_text(self.get_info(), None, True)


def main():
    info = Manager.Manager()
    text = texter(info.print_table())
    text.notify()

if __name__ == "__main__":
    main()