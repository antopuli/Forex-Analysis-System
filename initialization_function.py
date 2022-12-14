
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
        1. Show today exchange rates - It shows the exchange rate of the current day
        """
        print(help_txt)


    cmd = input("Enter a query: ")

    if cmd == "Show today exchange rates":
        s = input("Insert source currency: ")
        c = input("Insert interested currencies (separated with a comma): ")
        func.showTodayExRate(s, c)

    if cmd == "Show exchange rates from a date to today":
        dy = input("Enter the year: ")
        dm = input("Enter the month: ")
        dd = input("Enter the day: ")
        dte = dy + "-" + dm + "-" + dd
        s = input("Insert source currency: ")
        c = input("Insert interested currencies (separated with a comma): ")
        func.showExRateFromASpecificDateToToday(dte, s, c)

    if cmd == "Convert amount from a currency to another one":
        ic = input("Insert initial currency: ")
        t = "Insert amount: {curr} "
        a = input(t.format(curr=ic))
        fc = input("Insert final currency: ")
        func.convertAmountFromDifferentCurrencies(ic, fc, a)