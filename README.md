Módulo 2. Actividad didáctica 2

La actividad didáctica 2-M1 requiere aplicar el conocimiento de las distribuciones de probabilidad a la implementación de un modelo de Markov que se pueda ejecutar y obtener diferentes resultados de simulación.
Por ello, en esta actividad se implementa un modelo de Markov para simular cómo evolucionan las preferencias de las personas por tres tipos de gorras (Elegante, Casual y Deportiva) durante un periodo de 12 meses. Seleccionando el estado inicial de manera aleatoria según las probabilidades establecidas en una matriz de transición.

Para desarrollar la solución que simula las preferencias por gorras utilizando un modelo de Markov con la capacidad de iniciar desde cualquiera de los tres estados posibles ("Elegante", "Casual", "Deportiva"), se siguieron los siguientes pasos.

En primer lugar, se establecieron los estados que representan las preferencias por gorras: "Elegante", "Casual" y "Deportiva". Cada uno de estos estados refleja una elección específica que un usuario podría hacer en términos de estilo de gorra.

El siguiente paso fue definir la matriz de transición. Esta matriz especifica las probabilidades de cambiar de un estado a otro. Para este caso, se creó una matriz de transición 3x3 utilizando NumPy, donde cada fila representa las probabilidades de transición desde un estado inicial hacia los otros estados. Por ejemplo, si un usuario está en el estado "Elegante", la matriz de transición indica la probabilidad de permanecer en "Elegante", cambiar a "Casual" o cambiar a "Deportiva". 

Posteriormente y para asegurar que el modelo comience desde un estado inicial aleatorio entre los tres estados definidos, se implementó una función random_initial_state. Esta función utiliza np.random.choice para seleccionar de manera aleatoria uno de los índices correspondientes a los estados ("Elegante", "Casual", "Deportiva"). 

Una vez determinado el estado inicial, la simulación procede a lo largo de un número predeterminado de meses (en este caso, 12 meses). Durante cada mes, se utiliza la matriz de transición y el estado actual para determinar el siguiente estado. Esto se logra mediante la función next_state, que nuevamente utiliza np.random.choice para elegir el próximo estado basado en las probabilidades definidas en la matriz de transición desde el estado actual.

Durante la simulación, se registran las preferencias mensuales en una secuencia (preference_sequence) y se almacenan en una matriz (preference_matrix) que utiliza codificación one-hot para representar visualmente cómo cambian las preferencias mes a mes. 
Finalmente, se calcula y se imprimen los resultados que muestran cuántas veces se prefirió cada tipo de gorra durante los 12 meses simulados, junto con el porcentaje de tiempo que se mantuvo cada preferencia. 
