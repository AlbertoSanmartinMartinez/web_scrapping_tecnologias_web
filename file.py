
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8:

'''
Aplicacion para obtener el libro gratuito dirario
@author albertosanmartinmartinez@gmail.com
'''

import urllib2
import requests
from bs4 import BeautifulSoup
import os


class Book():
    '''clase principal  para el libro'''

    def __init__(self, url):
        '''constructor de la clase cliente'''
        # creamos las variables necesarias
        self.url = url
        self.web_code = self.getCode(url)
        self.html_web = self.getWeb(url, self.web_code)
        self.title = self.getTitle(self.html_web)

    def getCode(self, url):
        '''metodo que obtiene el codigo de la web, explicado en el reame.md'''
        # obtenemos el codigo que devuelve la web(explicado en el README.md
        req = requests.get(url)
        code = req.status_code
        return code

    def getWeb(self, url, code):
        '''metodo que descarga la web'''
        f = urllib2.urlopen(url)
        html = f.read()  # obtenemos el html de la web
        f.close()
        return html

    def showBook(self):
        '''metodo que muestra la informacion del libro'''
        print "la url es: " + self.url
        print "el codigo de la web es: ", self.web_code
        print "el titulo del libro es: " + self.title.title()
        self.notify('Notification', 'subtitle', self.title.title())

    def getTitle(self, html_web):
        '''metodo que devuelve el titulo dle libro'''
        # buscamos las etiquetas html donde esta el titulo
        soup = BeautifulSoup(html_web, 'html.parser')
        elements = soup.find_all('div', 'dotd-title')
        # extraemos el texto que contiene el titulo
        for element in elements:
            result = element.find('h2').text
        result = result.strip()
        return result

    def notify(self, title, subtitle, message):
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


if __name__ == "__main__":
    '''programa principal'''

    url = "https://www.packtpub.com/packt/offers/free-learning/"
    book = Book(url)
    book.showBook()
