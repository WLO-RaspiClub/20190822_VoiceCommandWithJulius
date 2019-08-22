#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import xml.etree.ElementTree as ET

def main():
  host = 'localhost'
  port = 10500
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))

  try:
    data = ''
    while 1:
      if '</RECOGOUT>\n.' in data:
        root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
        for wp in root.findall('./SHYPO/WHYPO'):
          command = wp.get('WORD')
          score = float(wp.get('CM'))
          if command == u'再生' and score >= 0.9:
            print u'play'
          elif command == u'プレイ' and score >= 0.996:
            print u'play'
          elif command == u'停止' and score >= 0.996:
            print u'stop'
          elif command == u'ストップ' and score >= 0.996:
            print u'stop'
          elif command == u'巻き戻し' and score >= 0.996:
            print u'rew'
          elif command == u'巻き戻り' and score >= 0.996:
            print u'rew'
        data = ''
      else:
        data = data + client.recv(1024)
  except KeyboardInterrupt:
    client.close()

if __name__ == "__main__":
  main()
