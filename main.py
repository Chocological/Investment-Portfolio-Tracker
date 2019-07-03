from appJar import gui
import csv
app = gui("Investment Portfolio Tracker", "800x400")
app.setFont(18)
main = "Dashboard"
addCoin = "Add a coin"


def read_coin_info():
    coin_ticker_name = app.getEntry("e1")
    coin_price = app.getEntry("e2")
    coin_purchase_date = str(app.getEntry("e3"))
    formatted_date = coin_purchase_date[0:1] + '/' + coin_purchase_date[2:3] + '/' + coin_purchase_date[4:7]
    coin_info_list = [coin_ticker_name, coin_price, formatted_date]
    headers = ["Name", "Price", "Date"]
    with open('Investments.csv', 'a') as investcsv:
        filewriter = csv.writer(investcsv, delimiter=',', lineterminator='\n')
        filewriter.writerow(coin_info_list)
    investcsv.close()


def dashboard():
    return


def add_coin():
    app.addEntry("e1")
    app.addNumericEntry("e2")
    app.addNumericEntry("e3")
    app.setEntryDefault("e1", "Coin ticker name (e.g BTC/USD)")
    app.setEntryDefault("e2", "Entry price")
    app.setEntryDefault("e3", "Date of purchase (in DDMMYYYY format)")
    app.setEntryMaxLength("e3", 8)
    app.addButton("Submit", read_coin_info)


app.addToolbarButton(main, dashboard, findIcon=True)
app.addToolbarButton(addCoin, add_coin, findIcon=True)
app.go()
