
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8:

'''
Aplicacion para obtener el libro gratuito dirario
@author albertosanmartinmartinez@gmail.com
'''

import urllib2
import requests
from bs4 import BeautifulSoup

class Book():
    '''clase principal  para el libro'''

    def __init__(self, url):
        '''constructor de la clase cliente'''
        self.url = url
        self.web_code = self.getCode(url)
        self.html_web = self.getWeb(url, self.web_code)
        self.title = self.getTitle(self.html_web)

    def getCode(self,url):
        '''metodo que obtiene el codigo de la web'''
        req = requests.get(url)
        code = req.status_code
        return code

    def getWeb(self, url, code):
        '''metodo que descarga la web'''
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def showBook(self):
        '''metodo que muestra el titulo del libro'''
        print "la url es: " + self.url
        print "el codigo de la web es: ", self.web_code
        print "el titulo del libro es: " + self.title

    def getTitle(self, html_web):
        '''metodo que devuelve el titulo dle libro'''
        soup = BeautifulSoup(html_web, 'html.parser')
        elements = soup.find_all("div")
        #print elements
        result = []
        for aux in elements:
            name = aux.find("dotd-title")
            result.append(name)
        print result
        return result

if __name__ == "__main__":

    url = "https://www.packtpub.com/packt/offers/free-learning/"
    book = Book(url)
    book.showBook()
