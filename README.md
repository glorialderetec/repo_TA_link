NO OLVIDAR DE ENVIAR LA API KEY POR SEPARADO EN LA ENTREGA DEL TRABAJO Y DAR LAS INSTRUCCIONES (Pegar la APIKEY en el archivo recomendaciones\_api.py donde lo pide)



# Sistema de Análisis y Perfilado de Clientes



#### Descripción



Este proyecto permite analizar el comportamiento de compra de clientes a partir de un dataset. El sistema ofrece estadísticas generales, clasificación de perfiles de clientes, comparación de segmentos, visualización de gráficos y generación de recomendaciones de marketing.



La función de heatmap devuelve un documento HTML que se almacena en la carpeta del repositorio. 



EL RESTO DEL DISEÑO DEL TRABAJO APLICADO SE ENCUENTRA EN EL DOCUMENTO "diseño" EN LA CARPETA "docs".



#### Requisitos



* Instalar las dependencias del proyecto:



pip install -r requirements.txt





* En la línea 16 del archivo datos.py se encuentra la ubicación del archivo csv, si el programa se corre desde Windows se debe corroborar que esta escrita con \\\\, en cambio, en Mac debería tener /





#### Dependencias



El archivo *requirements.txt* contiene las siguientes librerías:



pandas

matplotlib

seaborn

folium

google-genai

rich



#### Configuración inicial

##### Configurar la API Key



En el archivo "recomendaciones\_api.py", reemplazar:





API\_KEY = "PEGAR\_ACA\_LA\_API\_KEY"



por la api key que se les envía por mail

