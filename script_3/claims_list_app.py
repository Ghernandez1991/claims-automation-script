
# IMPORT DEPENDENCIES
import pandas as pd
from bs4 import BeautifulSoup
import requests

from splinter import Browser
import time
import pyautogui

# create a list of claim numbers
claim_list = ['enter claim number here']
# loop down the list of claims
for claim in claim_list:

    # GRAB THE USER CLAIM NUMBER/ID/PASSWORD

    claim_number = claim
    user_name = 'enter arb forums username here'
    password = 'enter password here'

    # set the url to an object
    url = "https://www.arbfile.org/webapp/execute/memberHome"

    # create the browser object
    browser = Browser("chrome", executable_path="chromedriver")
    # tell the browser to go to the website.
    browser.visit(url)

    # tell the browser to look for form data and fill in with the information we provided earlier
    browser.fill('username', user_name)
    browser.fill('password', password)

    # find the button and click it to submit
    browser.find_by_tag('button').click()

    # find the navbar table where e-subro is housed. when we find it, click it
    nav_bar = browser.find_by_id('td4')
    drop_down = nav_bar.click()

    # search for text demand search and click it.

    browser.click_link_by_text('Demand Search')

    # fill in the form 'fileno' with the claim number from earlier
    browser.fill('fileNo', claim_number)
    # find the button element and submit
    browser.find_by_name('btnSearch').first.click()

    # note this only works for trs files- olf files use different html to navigate to- use try and except to catch index errors and spit to console
    try:
        browser.click_link_by_partial_text('click here')
    except:
        print(f"This docket cannot be found, {claim_number}")
        continue

    # other wise for olf, use this
    # used for olf cases ---browser.click_link_by_partial_text('Docket Records')
    # give the browser time to slow down to allow the javascript/html to load
    import time
    time.sleep(10)

    # when you get to the page, tell the browser to search by xpath , and then click it.
    docket = browser.find_by_xpath(
        '//*[@id="featureView"]/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/a')
    docket.click()
    # find the xpath for the pdf decision
    decision = browser.find_by_xpath(
        '//*[@id="fixed-content"]/div[7]/div/decision-display-by-components/div[4]/card[1]/div')
    # more time needed to load
    time.sleep(5)

    # click on case actions
    button = browser.find_by_xpath('//*[@id="decision-actions"]')
    button.click()
    # opens pdf
    pdf = browser.find_by_id('action_VIEW_DECISION_PDF')
    window_before = browser.windows[0]
    pdf.click()
    # more time for browser to load
    time.sleep(5)
    # get current screen size- users with differnt screen sizes will need to use differnt x and y corordinates below
    print(pyautogui.size())
    # find position of the mouse
    print(pyautogui.position())
    # click that position
    # we move to 810 first because the download button likes to disappear if idle for too long
    pyautogui.moveTo(810, 215)
    # move back to the download button which should now be there
    pyautogui.moveTo(819, 215)
    # wait to make sure the download button is there
    time.sleep(1)
    # click it a second time to ensure it downloads
    pyautogui.click(819, 215)
    # wait
    time.sleep(3)
    # insert the claim number into the file name -bar. hit enter to save to downloads path
    pyautogui.typewrite(f"{claim_number}")
    pyautogui.typewrite(["enter"])
