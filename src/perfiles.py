
class Cliente:
    '''
    Objeto que representa un cliente de la empresa.
    '''
    def __init__(self, identificator, age, income, purchase_frequency, purchase_amount, satisfaction_score):
        '''

        Parametros
        ----------
        identificator : int
            El ID del cliente.
        age : int
            La edad del cliente.
        income : int
            El ingreso del cliente.
        purchase_frequency : int
            La frecuencia de compra del cliente.
        purchase_amount : int
            La cantidad de compra del cliente.
        satisfaction_score : int
            La satisfacción del cliente.

        Raises
        ------
        ValueError: si la edad, el ingreso y la cantidad de compra es negativa, 
                    si la satisfacción no esta entre 0-10, o si la frecuencia no es valida.

        Returns
        -------
        None.

        '''
        if age < 0:
            raise ValueError("Error: La edad no puede ser negativa")
        if income < 0:
            raise ValueError("Error: Los ingresos no pueden ser negativos")
        if purchase_amount < 0:
            raise ValueError("Error: El monto de compra no puede ser negativo")
        if satisfaction_score < 0 or satisfaction_score > 10:
            raise ValueError("Error: La satisfaccion debe estar entre 0 y 10")
        if purchase_frequency not in ["frequent", "occasional", "rare"]:
            raise ValueError("Error: La frecuencia debe ser 'frequent', 'occasional' o 'rare'")
        
        self.id = identificator
        self.age = age
        self.income = income
        self.purchase_frequency = purchase_frequency
        self.purchase_amount = purchase_amount
        self.satisfaction_score = satisfaction_score

 # Puntajes mínimos necesarios para cada categoría.
    # Si el score es >= 85 → Premium
    # Si el score es >= 55 → Frecuente
    # Si el score es < 55 → Ocasional        
        self.limite_premium = 85
        self.limite_frecuente = 55

    def obtener_score(self, cliente):
        '''
        Calcula el score del cliente a partir de su frecuencia de compra,monto gastado y nivel de satisfacción

        Returns
        -------
        score : int
            Puntaje total obtenido por el cliente.

        '''
        score = 0
        if cliente.purchase_frequency == "frequent":
            score += 50
        elif cliente.purchase_frequency == "occasional":
            score += 30
        else:  # rare
            score += 10

        if cliente.purchase_amount >= 15000:
            score += 30
        elif cliente.purchase_amount >= 8000:
            score += 20
        else:
            score += 10

        score += cliente.satisfaction_score * 2

        return score

#Clasifica al cliente segun su score 
    def clasificar(self, cliente):
        '''
        Determina la categoría del cliente según su score.

        Returns
        -------
        str
            La categoria asiganada al cliente. 
            Puede ser: "Premium", "Frecuente" o "Ocasional".

        '''

        score = self.obtener_score(cliente)

        if score >= self.limite_premium:
            return "Premium"

        elif score >= self.limite_frecuente:
            return "Frecuente"

        else:
            return "Ocasional"

    def generar_recomendacion(self, cliente):
        '''
        Genera una recomendación comercial basada en la categoría del cliente.


        Returns
        -------
        str
            Recomendación correspondiente al perfil del cliente.
        '''

        categoria = self.clasificar(cliente)

        if categoria == "Premium":
            return "Ofrecer beneficios VIP y descuentos exclusivos"

        elif categoria == "Frecuente":
            return "Enviar promociones personalizadas"

        else:
            return "Aplicar campaña de fidelización"
