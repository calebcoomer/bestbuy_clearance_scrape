## import libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

########################################################################################################

## defining function that will open links
def openlink(target_link):
    ##with open(filename, 'r') as file:
    #link_list = []
    #l = open(filename, 'r')
    #for link in l:
    #    link_list.append(link.strip())
        
    ## provide url and wait after opening
    driver.get(target_link)

    sleep(3)

########################################################################################################

## defining function that will scrape information
def scrape(target_link):
## open file by filename as read to get link to best buy page
    openlink(target_link)
    
########################################################################################################

## GET MODEL INFO
#  use driver to find model and sku values by class name
    drive1 = driver.find_elements(By.CLASS_NAME, 'sku-value')
#  collect models and skus
    disc_text1 = []
    for discovery in drive1:
        disc_text1.append(discovery.text)
#  declare empty lists for data to be divided
    model_list = []
    sku_list = []
#  enumerate through discovery text list 1 to split data into appropriate lists
    for index, info in enumerate(disc_text1):
        if ((index + 2) % 2 == 0):
            model_list.append(info)
        else:
            sku_list.append(info)

########################################################################################################

## GET PRICE INFO
#  use driver to find prices on the page by class name
    drive2 = driver.find_elements(By.CLASS_NAME, 'priceView-hero-price')
#  collect product price
    disc_text2 = []
    price_list = []
#   enumerate through discovery text list 2 to split each entry and store price (0 element)
    for index, entry in enumerate(drive2):
        price_list.append(drive2[index].text.split('\n')[0])
#  use driver to find original prices on the page by class name
    drive2 = driver.find_elements(By.CLASS_NAME, 'pricing-price__regular-price')
#  collect product original price
    disc_text2 = []
    original_price_list = []
#  enumerate through discovery text list 2 to split each entry and store price (-1 element)
    for index, entry in enumerate(drive2):
        original_price_list.append(drive2[index].text.split(' ')[-1])
    original_price_list = original_price_list[::2]

########################################################################################################

## GET PRODUCT NAME
#  find product nanmes on the page using class names
    drive3 = driver.find_elements(By.CLASS_NAME, 'sku-title')
#  collect prices
    disc_text3 = []
    name_list = []
    for name in drive3:
        disc_text3.append(name.text)
    for entry in disc_text3:
        name_list.append(entry.split())

########################################################################################################

## PRINT PRODUCT INFO
#  iterate through length of the list to print models and sku
    for i in range(len(model_list)):
        f.write(f'{model_list[i] : <29} | {sku_list[i] : <7} | {name_list[i][0] : <15} | {price_list[i] : >9} | {original_price_list[i] : >9} | {' '.join(name_list[i][2:-3])}\n')
        f.write(f'{"-" * 225}\n')
        
########################################################################################################

## defining main function
def main(link_list):
    f.write(f'         Model  Name          | SKU     | Brand           |   Sale    |  Original | Product Info \n{"-" * 225}\n')
    target_list = ['laptop_clearance_link1.txt','laptop_clearance_link2.txt','laptop_clearance_link3.txt','laptop_clearance_link4.txt']
    for target_link in link_list:
        scrape(target_link)

########################################################################################################
        
## open the driver outside of main to the first page in case of error loading (seems to happen frequently)
driver = webdriver.Edge()
f = open('output.txt', 'a')
l = open('laptop_clearance_links.txt', 'r')
link_list = []
for link in l:
    link_list.append(link.strip())
driver.get(link_list[0])
main(link_list)
## close edge driver
driver.quit()
