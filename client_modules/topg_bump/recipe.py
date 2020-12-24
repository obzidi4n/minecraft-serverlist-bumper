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

    api.set_input_value('//input[@placeholder="Username"]', cfg['username'])
    api.set_input_value('//input[contains(@type,"password")]', cfg['password'])
    api.click('//button[contains(.,"Login")]')

    # bump (login needed)
    api.get_url(cfg['url_bump'])

    # fill text box manually with update info
    time.sleep(300)