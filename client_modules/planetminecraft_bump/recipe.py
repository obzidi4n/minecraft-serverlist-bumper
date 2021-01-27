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

    # login
    api.get_url(cfg['url_login'])
    api.set_input_value('//input[@id="email"]', cfg['username'])
    api.set_input_value('//input[@id="password"]', cfg['password'])
    api.click('//input[@name="login"]')
    time.sleep(5)

    # bump (login needed)
    api.get_url(cfg['url_bump'])
    time.sleep(5)

    api.get_screenshot('bump_page')

    api.click('//a[contains(@title,"Bump Submission")]')
    print(cfg['site'] + ' bumped')