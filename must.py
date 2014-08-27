# coding: utf-8

import sys
import requests

from pyquery import PyQuery as pq


def query(work_title, work_ip='', work_title_exact='N', work_ip_exact='N'):
    url = 'http://www.must.org.tw/left_fun/search-list.asp?cpage='

    params = {
        'work_title': work_title, 
        'work_ip': work_ip,
        'work_title_exact': work_title_exact,
        'work_ip_exact': work_ip_exact,
    }

    r = requests.post(url, params)

    if not r.ok:
        sys.exit('request error')

    d = pq(r.content)
    tables = d('table:gt(1)')


    datas = []
    for idx, item in enumerate(tables):
        table = pq(item)
        full_title = table('tr:eq(1) td:eq(1)').text()
        language = table('tr:eq(1) td:eq(3)').text()
        lyricists = table('tr:eq(3) td:eq(1)').text()
        composers = table('tr:eq(4) td:eq(1)').text()
        rights_lyricists = table('tr:eq(6) td:eq(1)').text()
        rights_composers = table('tr:eq(7) td:eq(1)').text()

        if full_title == u'輸入曲目名稱有錯誤，請重新輸入正確曲目名稱再查詢。':
            return {}

        title, title_spell = full_title.split(' ', 1)[1].split('/', 1)

        data = {
            'title': title,
            'title_spell': title_spell,
            'langauge': language,
            'lyricists': lyricists,
            'composers': composers,
            'rights_lyricists': rights_lyricists,
            'rights_composers': rights_composers,
        }

        datas.append(data)

    return datas
