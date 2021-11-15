# Copyright 2016 Google Inc.
#
# Con licencia de Apache License, Versión 2.0 (la "Licencia");
# no puede utilizar este archivo excepto de conformidad con la Licencia.
# Puede obtener una copia de la licencia en
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# A menos que lo exija la ley aplicable o se acuerde por escrito, el software
# distribuido bajo la Licencia se distribuye "TAL CUAL",
# SIN GARANTÍAS O CONDICIONES DE NINGÚN TIPO, ya sea expresa o implícita.
# Consulte la Licencia para conocer el idioma específico que rige los permisos y
# limitaciones de la licencia.

#import webapp2


#class MainPage(webapp2.RequestHandler):
 #   def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello, World!')


#app = webapp2.WSGIApplication([
#    ('/', MainPage),], debug=True)

from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello():
    """Return a friendly HTTP greeting."""
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

