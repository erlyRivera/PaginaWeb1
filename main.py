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

importar  webapp2


clase  MainPage ( webapp2 . RequestHandler ):
    def  get ( self ):
        yo . respuesta . encabezados [ 'Content-Type' ] =  'text / plain'
        yo . respuesta . escribir ( '¡Hola, mundo!' )


aplicación  =  webapp2 . Aplicación WSGIA ([
    ( '/' , Página principal ),
], debug = True )
