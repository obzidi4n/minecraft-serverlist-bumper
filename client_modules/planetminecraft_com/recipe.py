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

    api.get_url(cfg['site']['url'])
    time.sleep(5)
    
    api.click('//a[contains(text(),"Sign In")]')

    api.set_input_value('//input[@id="email"]', cfg['site']['username'])
    time.sleep(2)

    api.set_input_value('//input[@id="password"]', cfg['site']['password'])

    ## wait for manual auth and login
    time.sleep(60)

    api.get_url(cfg['site']['page'])
    time.sleep(5)
    
    # is this correct?
    api.click('//a[contains(text(),"Bump Submission")]')