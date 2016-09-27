#!/usr/bin/env python
#coding: utf8



import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import urlparse
import time
import xlsxwriter
import sys

reload(sys)
sys.setdefaultencoding('utf8')

try:
    data = []
    url = 'http://1.163.com/list/0-0-1-2.html'
    response = urllib2.urlopen(url)
    if response.code != 200:
        print response.code
        exit(1)
    htmldoc = response.read()
    soup = BeautifulSoup(htmldoc, 'html.parser', from_encoding='utf8')

    u1 = 'http://1.163.com/'
    d = []
    for i in soup.find_all('p', class_='w-goods-title f-txtabb'):
        a = i.find('a')
        d.append(a['title'])

    m = []
    for i in d:
        i = i.replace('  ', ' ')
        m.append(i)

    for i in m:
        duobao = []
        driver = webdriver.PhantomJS(executable_path="phantomjs")
        driver.get(url)
        driver.find_element_by_link_text(i).click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(2)
        u = driver.current_url

        html_page = driver.page_source
        time.sleep(2)
        # d = m
        # for i in d:
        #     reson = urllib2.urlopen(i)
        #     if reson.code != 200:
        #         print reson.code
        #         continue
        #     html_page = reson.read()
        soup_page = BeautifulSoup(html_page, 'html.parser', from_encoding='utf8')

        for j in soup_page.find_all('div', class_='m-detail-main-title'):
            h1 = j.find('h1')
            name = h1['title']
        print name
        duobao.append(name)
        price = soup_page.find('div', class_='m-detail-main-one-price')
        t = price.get_text()
        money = t.split('次')[1]
        duobao.append(money)
        print money
        # driver = webdriver.PhantomJS(executable_path='phantomjs')
        print u  # url
        driver.get(i)
        driver.find_element_by_id("historyTab").click()
        time.sleep(3)
        html_js = driver.page_source
        soup_js = BeautifulSoup(html_js, 'html.parser', from_encoding='utf8')
        result = soup_js.find_all('div', class_="m-detail-tabHistory-result")

        # 获取第一个数据
        for i in result:
            if i.span != None:
                c = i.find_all('span')
                break

        list_time = []
        for i in c:
            for j in i.strings:
                list_time.append(j)

        num = list_time[1]
        jiexiao_time = list_time[2].split('：')[1]
        duobao_time = list_time[3].split('：')[1]

        duobao.append(num)
        duobao.append(jiexiao_time)
        duobao.append(duobao_time)
        print num
        print jiexiao_time
        print duobao_time

        dict_time = []
        for i in result:
            if i.span == None:
                continue
            dict_time.append(i.span.strong.string)

        count = len(dict_time)
        print count
        page = soup_js.find_all('button', class_='w-button w-button-aside')
        page_count = len(page)

        all_count = count + (page_count - 1) * 10
        print all_count
        duobao.append(all_count)

        page_end = page[page_count - 2]['id']
        print page_end
        driver.find_element_by_id(page_end).click()
        time.sleep(3)
        html_endpage = driver.page_source
        soup_end = BeautifulSoup(html_endpage, 'html.parser', from_encoding='utf8')
        result_end = soup_end.find_all('div', class_="m-detail-tabHistory-result")
        driver.close
        i = result_end[9]
        c = i.find_all('span')

        list_time = []
        for i in c:
            for j in i.strings:
                list_time.append(j)

        num_end = list_time[1]
        jiexiao_endtime = list_time[2].split('：')[1]
        duobao_endtime = list_time[3].split('：')[1]

        duobao.append(num_end)
        duobao.append(jiexiao_endtime)
        duobao.append(duobao_endtime)

        print num_end
        print jiexiao_endtime
        print duobao_endtime

        data.append(duobao)

except Exception, e:
    print "error"
    print e
finally:
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 8)
    worksheet.set_column('C:C', 12)
    worksheet.set_column('D:D', 24)
    worksheet.set_column('E:E', 24)
    worksheet.set_column('F:F', 5)
    worksheet.set_column('G:G', 12)
    worksheet.set_column('H:H', 24)
    worksheet.set_column('I:I', 24)
    worksheet.set_row(0, 30)
    top = workbook.add_format({'border': 6, 'align': 'center', 'bg_color': 'cccccc', 'font_size': 13, 'bold': True})
    title = ['商品名称', '总需人次', '幸运号1', '揭晓时间1', '夺宝时间1', '期数', '幸运号2', '揭晓时间2', '夺宝时间2']
    worksheet.write_row('A1', title, top)

    line = 1
    for i in data:
        line = line + 1
        a = 'A' + str(line)
        worksheet.write_row(a, i)

    # for i in range(2, len(data) + 2):
    #     a = 'A' + str(i)
    #     b = 'B' + str(i)
    #     c = 'C' + str(i)
    #     d = 'D' + str(i)
    #     e = 'E' + str(i)
    #     f = 'F' + str(i)
    #     g = 'G' + str(i)
    #     h = 'H' + str(i)
    #     k = 'I' + str(i)
    #
    #     j = i - 2
    #
    #     worksheet.write(p, d[j])
    #     worksheet.write(q, ldzwl[j])
    #     worksheet.write(m, cqbl[j])
    #     worksheet.write(n, tkzzl[j])

    workbook.close()
