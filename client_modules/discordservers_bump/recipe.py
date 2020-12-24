from api_classes.selenium import Selenium
import os
import re
import time
import yaml

class Recipe():
  def __init__(self, client_module, tmp_folder, browser):
    
    # get configs
    with open(client_module + '/config.yml', 'r') as config:
      cfg = yaml.full_load(config)
    
    # open session
    api = Selenium(tmp_folder, browser)
    print('opened browser')

    # login
    api.get_url(cfg['url_login'])
    time.sleep(3)

    api.click('//img[@alt="Menu Image"]')
    api.click('//span[contains(.,"Log In")]')
    time.sleep(3)

    api.set_input_value('//input[@name="email"]', cfg['username'])
    api.set_input_value('//input[@name="password"]', cfg['password'])
    api.click('//button[@type="submit"]')
    print('logged in')
    time.sleep(3)

    # bump
    api.get_url(cfg['url_bump'])
    time.sleep(5)
    
    api.click('//button[contains(@class,"Button_btn__2GreU Button_large__1DH7q Button_cta__3kIzZ")]')
    print(cfg['site'] + ' bumped')


