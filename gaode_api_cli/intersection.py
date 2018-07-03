#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire
import re
import json
import urllib3
import csv
http = urllib3.PoolManager()

class GaodeIntersection:
  def __init__(self):
    self.gaode_key = '8b910cbfe87407ec3365253c81e43966'
    self.default_fields = {
      'key': '8b910cbfe87407ec3365253c81e43966',
    }
    pass

  def searchOne(self, keywords, city='杭州'):
    fields = self.default_fields.copy()
    fields['city'] = city
    fields['keywords'] = keywords

    result = None
    try:
      req = http.request('GET', 'http://restapi.amap.com/v3/place/text',fields=fields)
      result = json.loads(req.data.decode('utf-8'))
    except Exception as e:
      print('got exception: ', e)

    return result
  
  def searchByFile(self, input_file_name, output_file_name='output.csv'):
    delimiter = r'[;,\s]'
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
      writer = csv.writer(csv_file, delimiter=',')
      writer.writerow(keys)
      i = 0
      with open(input_file_name, 'rt', encoding='utf-8') as f:
        for line in f:
          print('i >> ', str(i))
          result = self.searchOne(re.split(delimiter, line.strip())[0] + '路口')
          print('line ==>', re.split(delimiter, line.strip())[0] + '路口')
          # result = self.searchIntersection(line.strip())
          row = [
            str(i),
            re.split(delimiter, line.strip())[0]
          ]
          if not result or 'pois' not in result or len(result['pois']) < 1:
            print('result error.', result)
            for k in keys[2:]:
              row.append('NULL')
          else:
            meta = result['pois'][0]
            for k in keys[2:]:
              row.append(meta[k])
          i += 1
          # print(
          #   json.dumps(
          #     result,
          #     sort_keys=True,
          #     indent=2, 
          #     separators=(',', ': '),
          #     ensure_ascii=False
          #   )
          # )
          
          writer.writerow(row)
          pass
        pass
      pass
    pass

if __name__ == '__main__':
  fire.Fire(GaodeIntersection)

