
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8:

'''
Aplicacion para obtener el libro gratuito dirario
@author albertosanmartinmartinez@gmail.com
'''

import urllib2
from bs4 import BeautifulSoup

global url = "https://www.packtpub.com/packt/offers/free-learning/"

class Client(object):
    '''clase principal para el cliente'''

    def getWeb(self, page):
        '''metodo que descarga la web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def showBook(self, title):
        '''metodo que muestra el titulo del libro'''
        print title

    def main(self):
        '''constructor de la clase cliente'''
        web = self.getWeb(url)

if __name__ == "__main__":
    client = Client()
    client.main()
