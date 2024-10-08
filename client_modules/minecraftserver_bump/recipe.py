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

    api.set_input_value('//input[@class="form-control"][contains(@id,"username")]', cfg['username'])
    api.set_input_value('//input[@class="form-control"][contains(@id,"password")]', cfg['password'])
    api.click('//button[contains(.,"Log In")]')
    print('logged in')
    time.sleep(3)

    # bump (login needed)
    api.scroll_window(0,2000)
    api.click('//input[contains(@value,"Bump Server to Top")]')
    print(cfg['site'] + ' bumped')