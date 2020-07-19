import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.com/PGACLS30/dp/B07NVWHBBH/ref=sr_1_7?crid=UPOWVQ32FZR&dchild=1&keywords=guitar&qid=1595153762&sprefix=gui%2Caps%2C396&sr=8-7'

headers={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

def check_price():

    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print("hello")
    print(converted_price)
    print(title.strip())

    if(converted_price < 1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.elho()
    server.starttls()
    server.elho()

    server.login('from@gmail.com', 'password')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/PGACLS30/dp/B07NVWHBBH/ref=sr_1_7?crid=UPOWVQ32FZR&dchild=1&keywords=guitar&qid=1595153762&sprefix=gui%2Caps%2C396&sr=8-7'

    msg = "Subject: {subject}\n\n{body}"

    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()