# encoding: utf-8

import argparse
from datetime import datetime
import importlib
import os
from notifiers import get_notifier
import shutil
import traceback
import uuid

def exception(client_module, xslack, error):

  message = ':poop: _*' + client_module + '*_ produced an error at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n' + str(error.args) + '\n\nTraceback:\n```' + traceback.format_exc() + '```'
  print(message)
  
#   if not xslack:
#     slack = get_notifier('slack')
#     webhook_url = 'https://hooks.slack.com/services/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'
#     slack.notify(message=message, webhook_url=webhook_url)

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
  parser.add_argument("-xf", "--xftp", help="disable ftp", action="store_true")
  parser.add_argument("-xs", "--xslack", help="disable slack alerts ", action="store_true")
  args = parser.parse_args()

  try:

    # check for test mode
    if args.test:
      print('starting', args.client_module, 'in test mode')
      args.xftp = True
      args.xslack = True
    else:
      print('starting', args.client_module)

    # import client modules
    client_recipe = importlib.import_module('client_modules.' + args.client_module + '.recipe')
    # client_etl = importlib.import_module('client_modules.' + args.client_module + '.etl')
    # client_ftp = importlib.import_module('ftp')

    # create tmp folders
    tmp_folder = os.getcwd() + '/tmp/{}'.format(uuid.uuid4())
    make_tmp_folders(tmp_folder)
    print('created tmp folder:', tmp_folder)

    # run api recipe
    print('starting recipe')
    recipe = client_recipe.Recipe('client_modules/' + args.client_module, tmp_folder, args.browser)
    print('recipe complete')

#     # run etl
#     etl = client_etl.Etl('client_modules/' + args.client_module, tmp_folder)
#     print('etl complete')

#     # run ftp
#     if args.xftp:
#       print('ftp skipped')
#     else:
#       ftp = client_ftp.Ftp('client_modules/' + args.client_module, tmp_folder)
#       print('ftp complete')

    # close session
    if args.test:
      print('session close skipped')
    else:
      shutil.rmtree(tmp_folder, ignore_errors=True)
      print('closed session')

  except Exception as error:
    exception(args.client_module, args.xslack, error)

if __name__== "__main__":
  main()
