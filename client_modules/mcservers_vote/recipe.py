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
    api.get_url(cfg['url_vote'])
    time.sleep(3)
    api.click('//a[@class="cc-btn cc-dismiss"]')
    
    # vote (no login needed)
    api.set_input_value('//input[@id="username"]', cfg['vote_name'])

    # solve captcha manually
    time.sleep(90)