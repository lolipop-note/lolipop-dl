#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cookielib, urllib, urllib2, time

### Config
USER_URL = 'https://user.lolipop.jp/'
USER_LOGIN_URL = 'https://user.lolipop.jp/?mode=login&exec=1'
USER_LOGIN_REDIRECT_URL = 'https://user.lolipop.jp/?mode=menu'
ANALYZE_URL = 'https://user.lolipop.jp/?mode=analyze'
ANALYZE_SETTING_URL = 'https://user.lolipop.jp/?mode=analyze&exec=setting&id=%(id)s'
ANALYZE_DOWNLOAD_URL = 'https://user.lolipop.jp/?mode=analyze&exec=download'

### LolipopDL
class LolipopDL:
  def __init__(self, domain_plan, passwd, account=None, domain_id=None, domain_name_2=None, domain_name_3=None):
    if domain_plan == 0:
      self._login = ({
        'domain_plan': 0,
        'account': account,
        'domain_id': domain_id,
        'passwd': passwd})
    elif domain_plan == 1:
      self._login = ({
        'domain_plan': 1,
        'domain_name_2': domain_name_2,
        'domain_name_3': domain_name_3,
        'passwd': passwd})
    else:
      raise

    self._cj = cookielib.CookieJar()
    self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cj))
    self._opener.addheaders = [('User-agent', '')]

  def login(self):
    # Login
    self._opener.open(USER_URL)
    time.sleep(10)

    # Login (POST)
    r = self._opener.open(USER_LOGIN_URL, urllib.urlencode(self._login))
    time.sleep(10)

    # Check
    if r.geturl() != USER_LOGIN_REDIRECT_URL: raise

  def download(self, addressid, sltDate=[]):
    # Analyze
    self._opener.open(ANALYZE_URL)
    time.sleep(10)

    # Analyze Setting
    self._opener.open(ANALYZE_SETTING_URL % {'id': addressid})
    time.sleep(10)

    # Analyze Setting (POST)
    for i in sltDate:
      r = self._opener.open(ANALYZE_DOWNLOAD_URL, urllib.urlencode({'sltDate': i}))
      time.sleep(10)

      if r.info().has_key('Content-Disposition'):
        name = r.info()['Content-Disposition'].split('filename=')[1]
        if name[0] == '"' or name[0] == "'": name = name[1:-1]
        open(name, 'wb').write(r.read())
        print(name)
