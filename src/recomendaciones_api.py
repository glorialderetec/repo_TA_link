from google import genai

API_KEY = "PEGAR_ACA_LA_API_KEY" #se la mandamos aparte en la entrega del trabajo

client = genai.Client(api_key=API_KEY)

def generar_recomendacion_api(cliente):
    prompt= (f"Cliente ID: {cliente.id},Edad: {cliente.age}, Ingresos: {cliente.income}, Frecuencia de compra: {cliente.purchase_frequency}, Monto de compra: {cliente.purchase_amount}, Satisfacción: {cliente.satisfaction_score}, Score: {cliente.obtener_score()}, Perfil: {cliente.clasificar_perfil()}, Recomendación base: {cliente.generar_recomendacion()}. Generá una recomendación de marketing clara y breve para este cliente. 1. Análisis del cliente. 2. Riesgos detectados. 3. Recomendaciones. 4. Prioridad. ")

    respuesta = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return respuesta.text  #SUPER A CHEQUEAR 



