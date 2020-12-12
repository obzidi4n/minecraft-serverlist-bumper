from api_classes.selenium import Selenium
import os
import re
import time
import yaml

class Recipe():
  def __init__(self, client_module, tmp_folder, browser):
    
    # get configs
    #with open(client_module + 'config.yml', 'r') as config:
    with open('config.yml', 'r') as config:
      cfg = yaml.full_load(config)
    
    # open session
    api = Selenium(tmp_folder, browser)

    # vote (no login needed)
    api.get_url(cfg['url_vote'])

    time.sleep(5)

    api.set_input_value('//input[@name="mcname"]', cfg['vote_name'])
    api.click('//input[@class="r3submit"]')