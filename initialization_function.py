
import func


def init():

    txt = """ 
    Hi! Welcome in this foreign exchange analysis program, if you are a trader or an investor it 
    will be very evaluated to you, so try it. Remember to follow my github profile if you like my projects.  
    This forex analysis program has a large variety of functionalities, the next paragraph will
    guide you to understand how it works. Start print 'help'.  
    """

    print(txt)


    help_input = input()

    if help_input == "help":
        help_txt = """  
        This is the list of the program's functionalities:
        1. Show today exchange rate - It shows the exchange rate of the current day
        """
        print(help_txt)


    cmd = input("Enter a query: ")

    if cmd == "Show today exchange rate":
        s = input("Insert source currency: ")
        c = input("Insert interested currencies (separated with a comma): ")
        func.showTodayExRate(s, c)