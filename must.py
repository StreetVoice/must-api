# coding: utf-8

import sys
import requests

from pyquery import PyQuery as pq


def query(work_title, work_ip=None):
    url = 'http://www.must.org.tw/left_fun/search-list.asp?cpage='

    params = {
        'work_title': work_title, 
        'work_title_exact': 'Y',
        'work_ip_exact': 'N',
    }

    if work_ip:
        params['work_ip'] = work_ip

    r = requests.post(url, params)

    if not r.ok:
        sys.exit('request error')

    d = pq(r.content)
    table = d('table:eq(2)')

    name = table('tr:eq(1) td:eq(1)').text()
    language = table('tr:eq(1) td:eq(2)').text()
    lyricists = table('tr:eq(3) td:eq(1)').text()
    composers = table('tr:eq(4) td:eq(1)').text()
    rights_lyricists = table('tr:eq(6) td:eq(1)').text()
    rights_composers = table('tr:eq(7) td:eq(1)').text()

    if name == u'輸入曲目名稱有錯誤，請重新輸入正確曲目名稱再查詢。':
        return {}

    data = {
        'name': name,
        'langauge': language,
        'lyricists': lyricists,
        'composers': composers,
        'rights_lyricists': rights_lyricists,
        'rights_composers': rights_composers,
    }

    return data