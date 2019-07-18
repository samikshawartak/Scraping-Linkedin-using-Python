from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def login_and_search():	

    driver = webdriver.Chrome()

    driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

    driver.maximize_window()

    email = driver.find_element_by_xpath('//*[@id="username"]')
    email.send_keys('vikrantikawale1234@gmail.com')

    time.sleep(2)

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('qwerty@123')

    time.sleep(2)

    login = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
    login.click()

    time.sleep(2)

    #search
    search = driver.find_element_by_xpath('//input[@aria-label="Search"]')
    search.send_keys('python programmer')

    time.sleep(2)

    search.send_keys(Keys.ENTER)

    time.sleep(2)

    people = driver.find_element_by_xpath('//button[@aria-label="View only People results"]')
    people.click()

    time.sleep(3)

    #driver.quit()
    return driver


def get_detail_link(driver):
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    containers=soup.findAll("li",{"class":"search-result search-result__occluded-item ember-view"})
    #print(len(containers))
    
    #print(BeautifulSoup.prettify(containers[0]))

    container=containers[0]

    #print(container.img["alt"])
    '''try:
        name_con=container.findAll("span",{"class":"name actor-name"})
        name=name_con[0].text.strip()
    except IndexError:
        name=""
    
    summ_con=container.findAll("p",{"class":"subline-level-1 t-14 t-black t-normal search-result__truncate"})
    summ=summ_con[0].text.strip()

    loc_con=container.findAll("p",{"class":"subline-level-2 t-12 t-black--light t-normal search-result__truncate"})
    loc=loc_con[0].text.strip()
    
    print(name)
    print(summ)
    print(loc)'''
    
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
        
        print(name+","+summ+","+loc)
        
    time.sleep(20)
    
    driver.quit()


get_detail_link(login_and_search())
