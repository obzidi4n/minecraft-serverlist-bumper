#!/usr/bin/env python
# encoding: utf-8

import argparse
from datetime import datetime
import importlib
import os
import discord_notify as dn
import shutil
import traceback
import uuid

def exception(client_module, xnotify, error):

  message = ':poop: _*' + client_module + '*_ produced an error at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n' + str(error.args) + '\n\nTraceback:\n```' + traceback.format_exc() + '```'

  print(message)
  
  if not xnotify:
    webhook_url = 'https://discord.com/api/webhooks/785293168044015617/B4BZpyx3xFsjiTE0kwQPywGsAjQINOWQ-zMyKqOphZ89nPFdf-sV0BzuYaeqDLuF_MIl'
    notifier = dn.Notifier(webhook_url)
    notifier.send(message, print_message=False)
    

def make_tmp_folders(tmp_folder):

  folders = ['/user-data','/data-path','/cache-dir','/downloads','/out','/screenshots']

  if not os.path.exists(tmp_folder):
      os.makedirs(tmp_folder)

  for f in folders:
    if not os.path.exists(tmp_folder + f):
      os.makedirs(tmp_folder + f)

def main():

  # get client module from command line
  parser = argparse.ArgumentParser(description='Specify the client_module to run.')
  parser.add_argument('client_module', help='name of the client module')
  parser.add_argument("-t", "--test", help="run in test mode: disable ftp and slack alerts, preserve tmp folder", action="store_true")
  parser.add_argument("-b", "--browser", help="run selenium with browser", action="store_true")
  parser.add_argument("-xd", "--xnotify", help="disable alerts ", action="store_true")
  args = parser.parse_args()

  try:

    print('starting', args.client_module, 'test:', args.test, 'browser:', args.browser, 'no notify:', args.xnotify)
    
    # test mode?
    if args.test:
      args.xnotify = True
    
    # import client modules
    client_recipe = importlib.import_module('client_modules.' + args.client_module + '.recipe')

    # create tmp folders
    tmp_folder = os.getcwd() + '/tmp/{}'.format(uuid.uuid4())
    make_tmp_folders(tmp_folder)
    print('created tmp folder:', tmp_folder)

    # run api recipe
    print('starting recipe')
    recipe = client_recipe.Recipe('client_modules/' + args.client_module, tmp_folder, args.browser)
    print('completed recipe')
    
    # close session
    if args.test:
      print('tmp folders retained')
    else:
      shutil.rmtree(tmp_folder, ignore_errors=True)
      print('tmp folders removed')
        
    # notify
    
    if not args.xnotify:
        message = (':right_facing_fist: ' + args.client_module + ' completed!')
        webhook_url = 'https://discord.com/api/webhooks/785293168044015617/B4BZpyx3xFsjiTE0kwQPywGsAjQINOWQ-zMyKqOphZ89nPFdf-sV0BzuYaeqDLuF_MIl'
        notifier = dn.Notifier(webhook_url)
        notifier.send(message, print_message=False)

  except Exception as error:
    exception(args.client_module, args.xnotify, error)

if __name__== "__main__":
  main()
