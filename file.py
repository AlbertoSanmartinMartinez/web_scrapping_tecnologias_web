
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
        #creamos las variables necesarias
        self.url = url
        self.web_code = self.getCode(url)
        self.html_web = self.getWeb(url, self.web_code)
        self.title = self.getTitle(self.html_web)

    def getCode(self,url):
        '''metodo que obtiene el codigo de la web, no lo usaremos, esta explicado en el reame.md'''
        req = requests.get(url)
        code = req.status_code #obtenemos el codigo que devuelve la web(explicado en el README.md
        return code

    def getWeb(self, url, code):
        '''metodo que descarga la web'''
        f = urllib2.urlopen(url)
        html = f.read() #obtenemos el html de la web
        f.close()
        return html

    def showBook(self):
        '''metodo que muestra la informacion del libro'''
        print "la url es: " + self.url
        print "el codigo de la web es: ", self.web_code
        print "el titulo del libro es: " + self.title.title()

    def getTitle(self, html_web):
        '''metodo que devuelve el titulo dle libro'''
        soup = BeautifulSoup(html_web, 'html.parser')
        elements = soup.find_all('div', 'dotd-title') #buscamos las etiquetas html donde esta el titulo
        for element in elements:
            result = element.find('h2').text #extraemos el texto que contiene el titulo
        result = result.strip()
        return result

if __name__ == "__main__":
    '''programa principal'''

    url = "https://www.packtpub.com/packt/offers/free-learning/"
    book = Book(url)
    book.showBook()
