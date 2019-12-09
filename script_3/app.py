def arb_scrape():
    #IMPORT DEPENDENCIES 
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests

    from splinter import Browser
    import time

    #GRAB THE USER CLAIM NUMBER/ID/PASSWORD
    claim_number = input("What is the claim number?")
    user_name = input("What is your username")
    password = input("What is your password")

    #set the url to an object
    url = "https://www.arbfile.org/webapp/execute/memberHome"


    #create the browser object 
    browser = Browser("chrome", executable_path="chromedriver")

    ##tell the browser to go to the website. 
    browser.visit(url)

    #tell the browser to look for form data and fill in with the information we provided earlier
    browser.fill('username', user_name)
    browser.fill('password', password )

    #find the button and click it to submit
    browser.find_by_tag('button').click()

    #find the navbar table where e-subro is housed. when we find it, click it
    nav_bar = browser.find_by_id('td4')
    drop_down = nav_bar.click()


    #search for text demand search and click it. 

    browser.click_link_by_text('Demand Search')

    #fill in the form 'fileno' with the claim number from earlier
    browser.fill('fileNo', claim_number)
    #find the button element and submit 
    browser.find_by_name('btnSearch').first.click()

    #if it is a trs claim- use this
    browser.click_link_by_partial_text('click here')
    #other wise for olf, use this 
    #used for olf cases ---browser.click_link_by_partial_text('Docket Records')


    time.sleep(10)

    #when you get to the page, tell the browser to search by xpath , and then click it. 



    docket = browser.find_by_xpath('//*[@id="featureView"]/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/a')
    docket.click()

    decision = browser.find_by_xpath('//*[@id="fixed-content"]/div[7]/div/decision-display-by-components/div[4]/card[1]/div')

    time.sleep(5)

    #click on case actions 
    button = browser.find_by_xpath('//*[@id="decision-actions"]')
    button.click()

    pdf = browser.find_by_id('action_VIEW_DECISION_PDF')
    pdf.click()

 
    keep_open = input("putting input to keep the browser open")


   



arb_scrape()


