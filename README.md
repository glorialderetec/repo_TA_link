NO OLVIDAR DE ENVIAR LA API KEY POR SEPARADO EN LA NETREGA DEL TRABAJO Y DAR LAS INSTRUCCIONES (Pegar la APIKEY en el archivo recomendaciones\_api.py donde lo pide)



# Sistema de Análisis y Perfilado de Clientes



#### Descripción



Este proyecto permite analizar el comportamiento de compra de clientes a partir de un dataset. El sistema ofrece estadísticas generales, clasificación de perfiles de clientes, comparación de segmentos, visualización de gráficos y generación de recomendaciones de marketing.



#### Requisitos



Instalar las dependencias del proyecto:





pip install -r requirements.txt



En la línea 16 del archivo datos.py se encuentra la ubicación del archivo csv, si el programa se corre desde Windows se debe corroborar que esta escrita con \\\\, en cambio, en Mac debería tener /





#### Dependencias



El archivo *requirements.txt* contiene las siguientes librerías:



pandas

matplotlib

google-genai

rich



#### Configuración inicial

##### Configurar la API Key



En el archivo correspondiente a las recomendaciones mediante IA, reemplazar:





API\_KEY = "PEGAR\_ACA\_LA\_API\_KEY"

