#!/usr/bin/python3

## Made by SirManishKumar ##

from selenium import webdriver
import time
import sys
import os

###########################

os.system("clear")

###########################
print (g +" ██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗") 
print ("███║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
print ("███║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝")
print ("███║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝ ")
print ("█╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║     ")
print ("█ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ")
print ()
print ("██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗")
print ("██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗")
print ("██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝")
print ("██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗")
print ("██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║")
print ("╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝"+ r)
print ()
print (f"              Coded By ={r}Sir{k}Man{r}ish{k}Kum{r}ar") 
print () 
print (f"              Twitter ={k} SirManishKumar")       
print ()
print (f"              {r}Github ={k} https://github.com/SirManishKumar/WhatsAppBom")
print ()
time.sleep(2)

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

name = input("\n Enter Target Name: ")

time.sleep(1)

msg = input("\n Enter Your Message: ")

time.sleep(1)

count = int(input("\n Enter Number of Messages: "))

time.sleep(1)

os.system("clear")

input(" Press Enter To Continue")

time.sleep(1)

os.system("clear")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name("_3u328")

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()
