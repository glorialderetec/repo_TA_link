def generar_recomendacion_api(cliente):
  prompt= (f"Cliente ID: {cliente.id},Edad: {cliente.age}, Ingresos: {cliente.income}, Frecuencia de compra: {cliente.purchase_frequency}, Monto de compra: {cliente.purchase_amount}, Satisfacción: {cliente.satisfaction_score}, Score: {cliente.obtener_score()}, Perfil: {cliente.clasificar_perfil()}, Recomendación base: {cliente.generar_recomendacion()}. Generá una recomendación de marketing clara y breve para este cliente. ")
  #aca llamar a la api y pasarle el prompt
