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

    # open browser
    api = Selenium(tmp_folder, browser)

    # cookie nottification
    api.get_url(cfg['url_login'])
    time.sleep(3)
    api.click('//a[@class="cc-btn cc-dismiss"]')
    
    # login
    api.get_url(cfg['url_login'])
    time.sleep(3)

    api.set_input_value('//input[contains(@name,"username")]', cfg['username'])
    api.set_input_value('//input[contains(@name,"password")]', cfg['password'])
    api.click('//button[@type="submit"][contains(.,"Login")]')
    print('logged in')

    # bump (login needed)
    api.get_url(cfg['url_bump'])
    time.sleep(3)

    print(cfg['site'] + ' bumped')