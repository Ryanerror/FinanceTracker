from pushnotifier import PushNotifier as pn


class texter:

    __slots__ = ["__info", "__domain", ]

    def __init__(self, info):
        self.__info = info
        self.__domain = "@vtext.com"
        

    def set_info(self, new_info):
        self.__info = new_info
    
    def get_info(self):
        return self.__info

    def email_alert(self):
       notifer = pn.PushNotifier('ryangarvin19', 'Spongebob,101', 'com.ryangfinancetracker.app', 'B5YA6V2VBDE7DBV46V75B63CVB5YA68B2DBYFFBTTB')
       notifer.send_text(self.get_info(), None, True)


def main():
    # manager = Manager()
    text = texter("test")
    text.email_alert()

if __name__ == "__main__":
    main()