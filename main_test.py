# Copyright 2016 Google Inc. Todos los derechos reservados.
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

importar  webtest

importar  principal


def  test_get ():
    app  =  webtest . TestApp ( principal . App )

    respuesta  =  aplicación . obtener ( '/' )

    afirmar la  respuesta . status_int  ==  200
    afirmar la  respuesta . body  ==  '¡Hola, mundo!'
