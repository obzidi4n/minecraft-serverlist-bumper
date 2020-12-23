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

    # bump (login needed)
    api.get_url(cfg['url_bump'])
    time.sleep(5)
    
    api.click('//a[contains(text(),"Bump Submission")]')

    print(cfg['site'] + ' bumped')