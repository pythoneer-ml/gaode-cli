#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire
import os
import json
import re
import json
import urllib3
import csv
http = urllib3.PoolManager()
config_file_path = os.path.join(os.path.split(__file__)[0], 'config.json')
default_fields = {}

'''
相关高德poi类型:
822 190302  地名地址信息  交通地名  路口名
823 190303  地名地址信息  交通地名  环岛名
824 190304  地名地址信息  交通地名  高速路出口
825 190305  地名地址信息  交通地名  高速路入口
826 190306  地名地址信息  交通地名  立交桥
827 190307  地名地址信息  交通地名  桥
828 190308  地名地址信息  交通地名  城市快速路出口
829 190309  地名地址信息  交通地名  城市快速路入口
'''

class GaodeIntersection:
  def __init__(self):
    config_meta = {}
    with open(config_file_path, 'r') as f:
      config_meta = json.loads(f.read())
    self.__default_fields = {
      'key': config_meta['key'],
      'types': '190302|190303|190304|190305|190306|190308|190309' # 路口类型
    }
    pass

  def searchOne(self, keywords, city=u'杭州'):
    fields = self.__default_fields.copy()
    fields['city'] = city.encode('utf-8')
    fields['keywords'] = keywords.encode('utf-8')

    result = None
    try:
      req = http.request('GET', 'http://restapi.amap.com/v3/place/text',fields=fields,timeout=10)
      result = json.loads(req.data.decode('utf-8'))
    except Exception as e:
      print('got exception: ', e)

    return result
  
  def searchByFile(self, input_file_name, output_file_name='output.csv', has_header=False, delimiter='$'):
    rowDelimiter = r'[;,\s]'
    keys = [
      'id',
      'origin',
      'name',
      'adname',
      'cityname',
      'pname',
      'type',
      'location',
      'typecode'
    ]
    with open(output_file_name, 'w') as csv_file:
      writer = csv.writer(csv_file, delimiter=delimiter)
      writer.writerow(keys)
      with open(input_file_name, 'rt', encoding='utf-8') as f:
        i = 0
        startRow = 0
        if has_header:
          startRow = 1
        for line in f:
          i += 1
          if not (i > startRow):
            continue
          splits = re.split(rowDelimiter, line.strip())
          key = splits[0]
          if len(splits) > 1:
            searchValue = splits[1]
          else:
            searchValue = splits[0]
          result = self.searchOne(searchValue)
          print('lineNum => ', i)
          print('content => ', line.strip().encode('utf-8').decode('utf-8'))
          # result = self.searchIntersection(line.strip())
          row = [
            key,
            searchValue
          ]
          if not result or 'pois' not in result or len(result['pois']) < 1:
            print('result error.', result)
            for k in keys[2:]:
              row.append('NULL')
          else:
            meta = result['pois'][0]
            for k in keys[2:]:
              row.append(meta[k])
          
          writer.writerow(row)
          pass
        pass
      pass
    pass

if __name__ == '__main__':
  fire.Fire(GaodeIntersection)

