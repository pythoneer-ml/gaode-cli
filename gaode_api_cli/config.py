#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire
import json
import os
config_file_path = os.path.join(os.path.split(__file__)[0], 'config.json')

class GaodeConfig:
  def __init__(self):
    pass

  def setKey(self, key):
    config_meta = {}
    with open(config_file_path, 'r') as f:
      try:
        config_meta = json.loads(f.read())
      except Exception as e:
        print('exception', e)
    config_meta['key'] = key

    with open(config_file_path, 'w+') as f:
      f.write(json.dumps(
        config_meta,
        indent=2,
        separators=(',', ': '),
        ensure_ascii=False
      ))
    pass
  
  def getKey(self):
    with open(config_file_path, 'r') as f:
      config_meta = {}
      try:
        config_meta = json.loads(f.read())
      except Exception as e:
        print('exception', e)
      if 'key' in config_meta:
        print('key: ', config_meta['key'])
      else:
        print('key not found, please set key.')
    pass

if __name__ == '__main__':
  fire.Fire(GaodeConfig)
