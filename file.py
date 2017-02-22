
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8:

'''
Aplicacion para obtener el libro gratuito dirario
@author albertosanmartinmartinez@gmail.com
'''

import urllib2
from bs4 import BeautifulSoup

class Book():
    '''clase principal  para el libro'''

    def __init__(self, url):
        '''constructor de la clase cliente'''
        print "constructor llamado"
        self.url = url
        self.html_web = self.getWeb(self.url)
        self.title = self.getTitle(self.html_web)

    def getWeb(self, url):
        '''metodo que descarga la web'''
        print "obtenemos la web"
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def showBook(self):
        '''metodo que muestra el titulo del libro'''
        print self.url
        print self.web
        print self.title

    def getTitle(self, web):
        '''metodo que devuelve el titulo dle libro'''
        print "obtenemos el titulo"
        pass

if __name__ == "__main__":

    url = "https://www.packtpub.com/packt/offers/free-learning/"
    book = Book(url)
    book.showBook()
