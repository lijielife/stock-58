#!/usr/bin/env python2
#coding: utf-8

import urllib
import urllib2
import cookielib

class download:
    '''first_url: the referer in headers
       proxy: the proxy format with ip:port
       is_cookie: whether download with cookie
    '''
    def __init__(self, first_url='', proxy=None, is_cookie=False):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0'
        self.headers = {'User-Agent': self.user_agent, 'Accept-encoding':'gzip, deflate', 'Referer': first_url}
        if is_cookie:
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.MozillaCookieJar()))
        else:
            self.opener = urllib2.build_opener()
        self.proxy = proxy

    def add_proxy(self, url, proxy):
        if proxy:
            if url.startswith('https'):
                self.opener.add_handler(urllib2.ProxyHandler({'https': proxy}))
            else:
                self.opener.add_handler(urllib2.ProxyHandler({'http': proxy}))

    def get(self, url):
        self.add_proxy(url, self.proxy)
        request = urllib2.Request(url)
        print 'Downloading %s' % url
        response = self.opener.open(request)
        html = response.read()
        return html

    def post(self, url, data):
        self.add_proxy(url, self.proxy)
        if isinstance(data, dict):
            data = urllib.urlencode(data)
        request = urllib2.Request(url, data, self.headers)
        response = self.opener.open(request)
        print 'Downloading %s' % url
        html = response.read()
        return html

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print download(is_cookie=True).get(url)
