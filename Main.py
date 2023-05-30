# Automated-Amazon Price Tracker
from http import server
from smtplib import SMTP

import requests
from bs4 import BeautifulSoup
import smtplib

# Establish a connection with the email servers
server: SMTP = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
# Establish a secure connection
server.starttls()
server.ehlo()

# Login to the email account
server.login(' ', 'password')


# URL of the product
URL = 'https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i9/dp/B081JWZQJB/ref=sr_1_1_sspa?crid=2ZQZQZQZQZQZQ&dchild=1&keywords=macbook+pro+16+inch&qid=1596158453&sprefix=macbook+pro+16%2Caps%2C-1&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExM0dZM0dZV0dZQ0dSJmVuY3J5cHRlZElkPUEwNjY5NjQ5Mk5ZM0dZM0dZV0dZQ0dRJmVuY3J5cHRlZEFkSWQ9QTA0NjQ0NzYxM1dZM0dZM0dZV0dZQ0dRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

# User-Agent
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.116 Chrome/83.0.4103.116 Safari/537.36'}


# Function to check the price of the product
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Title of the product
    title = soup.find(id="productTitle").get_text()

    # Price of the product
    price = soup.find(id="price block_ourprice").get_text()
    converted_price = float(price[2:8].replace(',', ''))

    # If the price is less than 2,00,000, send an email
    if converted_price < 200000:
        send_mail()

    print(title.strip())
    print(converted_price)


# Function to send an email
def send_mail():
    servers = smtplib.SMTP('smtp.gmail.com', 587)
    servers.ehlo()
    # Establish a secure connection
    servers.starttls()
    servers.ehlo()

    # Login to the email account
    servers.login(' ', 'password')


# Subject of the email
subject = 'Price fell down!'
# Body of the email

body = 'Check the Amazon link: https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i9/dp/B081JWZQJB/ref=sr_1_1_sspa?crid=2ZQZQZQZQZQZQ&dchild=1&keywords=macbook+pro+16+inch&qid=1596158453&sprefix=macbook+pro+16%2Caps%2C-1&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExM0dZM0dZV0dZQ0dSJmVuY3J5cHRlZElkPUEwNjY5NjQ5Mk5ZM0dZM0dZV0dZQ0dRJmVuY3J5cHRlZEFkSWQ9QTA0NjQ0NzYxM1dZM0dZM0dZV0dZQ0dRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

msg = f"Subject: {subject}\n\n{body}"

# Send the email
server.sendmail(
    ' ',  # From
    ' ',  # To
    msg
)

print('Email has been sent!')

# Close the connection
server.quit()
