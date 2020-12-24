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

    # vote (no login needed)
    api.get_url(cfg['url_vote'])
    api.set_input_value('//input[@name="mc_user"]', cfg['vote_name'])
    api.click('//label[contains(@for,"rate-10")]')

    # solve captcha manually