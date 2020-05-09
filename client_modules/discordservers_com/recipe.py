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

    api.get_url(cfg['site']['url'])
    time.sleep(5)

    api.click('//a[@role="button"][@aria-label="menu"]')

    api.click('//div[@class="style_2Kds2_main style_1kVGk_menu-active"]//a[6]')

    api.set_input_value('//input[@class="inputDefault-_djjkz input-cIJ7To"][@type="email"]', cfg['site']['username'])
    time.sleep(2)

    api.set_input_value('//input[@class="inputDefault-_djjkz input-cIJ7To"][@type="password"]', cfg['site']['password'])
    time.sleep(2)

    api.click('//button[@type="submit"]')
    time.sleep(5)

    # optional validation
    if api.find_elements('//button[@class="button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl grow-q77ONN"]'):
        api.click('//button[@class="button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeMedium-1AC_Sl grow-q77ONN"]')
        time.sleep(10)

    api.get_url('https://discordservers.com/panel/210536719844376576/view')
    time.sleep(5)

    # yep twice .. might need to authenticate
    api.get_url('https://discordservers.com/panel/210536719844376576/view')
    time.sleep(5)

    api.click('//a[contains(text(),"Bump Server")]')
    time.sleep(2)
    
    api.click('//button[contains(text(),"Give Free Gems!")]')