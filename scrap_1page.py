#import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#function to login using given credentials and search the required keyword
def login_and_search():
    
    #initializing chromedriver
    driver = webdriver.Chrome()

    #opening the link
    driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

    driver.maximize_window()

    #logging in using username and password
    email = driver.find_element_by_xpath('//*[@id="username"]')
    email.send_keys('/* username of linkedin */')

    time.sleep(2)

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('/* password of linkedin */')

    time.sleep(2)

    #clicking login button
    login = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
    login.click()

    time.sleep(2)

    #search the keyword
    search = driver.find_element_by_xpath('//input[@aria-label="Search"]')
    search.send_keys('python programmer')

    time.sleep(2)

    search.send_keys(Keys.ENTER)

    time.sleep(2)

    people = driver.find_element_by_xpath('//button[@aria-label="View only People results"]')
    people.click()

    time.sleep(5)

    #returning the current state to next function
    return driver

#function to scrap the data results of searched keyword
def get_detail_link(driver):

    #get the url of the current page
    new_url=driver.current_url

    #loop to scrap 5 pages of search result
    for i in range(5):
        i=i+1

        #appending the pages nos to the link
        url2=new_url+"&page="+str(i)
        driver.get(url2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
    
        containers=soup.findAll("li",{"class":"search-result search-result__occluded-item ember-view"})

        container=containers[0]

        #loop to print the results of 1 page
        for container in containers:
            try:
                name_con=container.findAll("span",{"class":"name actor-name"})
                name=name_con[0].text.strip()
            except IndexError:
                name=""
            
            summ_con=container.findAll("p",{"class":"subline-level-1 t-14 t-black t-normal search-result__truncate"})
            summ=summ_con[0].text.strip()

            loc_con=container.findAll("p",{"class":"subline-level-2 t-12 t-black--light t-normal search-result__truncate"})
            loc=loc_con[0].text.strip()
            
            print(name+","+summ+","+loc+"\n")
        time.sleep(5)
       
    time.sleep(10)
       
    driver.quit()

#calling the functions
get_detail_link(login_and_search())
