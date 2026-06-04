NO OLVIDAR DE ENVIAR LA API KEY POR SEPARADO EN LA NETREGA DEL TRABAJO Y DAR LAS INSTRUCCIONES (Pegar la APIKEY en el archivo recomendaciones\_api.py donde lo pide)



# Sistema de Análisis y Perfilado de Clientes



#### Descripción



Este proyecto permite analizar el comportamiento de compra de clientes a partir de un dataset. El sistema ofrece estadísticas generales, clasificación de perfiles de clientes, comparación de segmentos, visualización de gráficos y generación de recomendaciones de marketing.



#### Requisitos



Instalar las dependencias del proyecto:





pip install -r requirements.txt





#### Dependencias



El archivo *requirements.txt* contiene las siguientes librerías:


pandas

matplotlib

google-genai

rich



#### Configuración inicial



##### 1\. Configurar la ruta del proyecto



Antes de ejecutar el programa, modificar la variable 'ruta_proyecto' dentro de la función 'cargar_dataset()' ubicada en 'src/datos.py'.



Ejemplo:





ruta\_proyecto = "C:\\\\Users\\\\NombreUsuario\\\\Documents\\\\GitHub\\\\repo\_TA\\\\"





La ruta debe coincidir con la ubicación del repositorio en la computadora donde se ejecutará el programa.



##### 2\. Configurar la API Key



En el archivo correspondiente a las recomendaciones mediante IA, reemplazar:





API\_KEY = "PEGAR\_ACA\_LA\_API\_KEY"





#### Estructura del proyecto



repo\_TA/

│

├── main.py

├── requirements.txt

├── README.md

│

├── data/

│   └── customer\_data.csv

│

└── src/

	 ├── datos.py

	 ├── interfaz.py

	 ├── perfiles.py

	 ├── metricas.py

	 ├── comparaciones.py

	 ├── graficos.py

	 └── recomendaciones.py
