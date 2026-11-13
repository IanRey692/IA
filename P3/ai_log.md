## Registro 01: Selección y justificación del dataset Benchmark
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "Oye mano, me piden tener en el dataset 4 rasgos y 3 clases, cual cumpliria con esos y porque?"
- **Resumen del output recibido:** La IA sugirió usar el clásico dataset de Iris que ya viene en la librería `sklearn`, explicando que encaja perfecto porque tiene exactamente 4 características numéricas (medidas de los pétalos y sépalos) y 3 clases (los tipos de flor). Además, mencionó que es el estándar de la industria para usarlo como línea base (benchmark).
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó el uso de la función `load_iris()` directo en la celda de preparación. Fue mucho más rápido llamarlo desde la librería que andar buscando y descargando un archivo CSV suelto, garantizando de paso que cumpliera exactito con lo que pedía el profe en la rúbrica.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, estuvo perfecto. Los datos cargaron limpios y jalaron a la primera, lo que sirvió súper bien como entorno controlado para comprobar que la matemática de mis algoritmos desde cero sí estaba clasificando correctamente.

## Registro 02: Funcionamiento y cálculo de la distancia euclidiana
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "como funciona exactamente la euclidiana en el algoritmo de distancia mínima y cómo se saca o queso?"
- **Resumen del output recibido:** La IA me explicó que la distancia euclidiana es literal como tirar una línea recta entre dos puntos para ver qué tan lejos están. Me detalló que matemáticamente se saca restando el valor de nuestro dato nuevo menos el valor del centroide, elevando eso al cuadrado para quitar signos negativos, sumando todo y al final sacándole la raíz cuadrada. El algoritmo usa ese número final para ver a qué centroide pegarse.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Con esta explicación dejé tal cual mi función `distancia_euclidiana` con el ciclo `for` que armé, porque ya me quedó clarísimo qué hace cada línea de código (la resta, el `** 2` y el `** 0.5` de la raíz) y ya sé cómo defenderlo si me preguntan en la revisión.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, estuvo al cien. Me ayudó a entender la lógica que hay detrás de las matemáticas del código, comprobando que el modelo clasifica bien basándose simplemente en buscar el número más chiquito de esa fórmula.

## Registro 03: Optimización del cálculo de centroides en Distancia Mínima
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "para sacar el centro en el de distancia mínima, a fuerzas tengo que armar un ciclo for para sumar todo a mano o hay alguna funcion que me lo de directo?"
- **Resumen del output recibido:** La IA explicó que no era necesario hacer iteraciones manuales y sugirió utilizar la función `np.mean(puntos, axis=0)` para obtener el promedio de las características de la clase directamente por columnas.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó el uso de `np.mean` reemplazando los ciclos `for` que tenía planeados inicialmente, ya que hace el código mucho más limpio y eficiente, respetando la regla de hacerlo desde cero sin usar clasificadores preconstruidos.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, fue correcto. Facilitó el cálculo matricial sin alterar la lógica matemática del modelo, agilizando la predicción.

## Registro 04: Implementación de la Distancia Euclidiana desde cero
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "Oye mano, para la distancia euclidiana en el algoritmo, ¿puedo jalar una función de sklearn o a fuerzas tengo que aventarme la fórmula matemática a pie con un for para que el profe me lo cuente como 'desde cero'?"
- **Resumen del output recibido:** La IA me explicó que usar una función prefabricada de machine learning para el cálculo principal rompe el requisito de la práctica. Me recomendó irme a la segura y armar la fórmula manualmente: hacer la resta de los puntos, elevar al cuadrado, sumar y sacar la raíz.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Descarté buscar atajos en librerías y mejor armé mi propia función `distancia_euclidiana` usando un ciclo `for` básico. Lo hice así porque es el núcleo de mis dos algoritmos (Distancia Mínima y 1-NN) y con eso demuestro que la matemática principal la programé yo.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, quedó al cien. La función calcula las distancias perfecto y ambos modelos logran clasificar bien los datos sin depender de nada externo.

## Registro 05: Optimización para unir arreglos en el K-Fold
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "Oye mano, en el K-fold ya logré separar mis datos para el test, phice un for para sacar el dato anterior y pasarlo al nuevo. se puede hacer más rapido?"
- **Resumen del output recibido:** La IA me explicó que usar un ciclo `for` para mover los datos uno por uno hace que el proceso sea muy lento y poco eficiente. Me sugirió usar la función `np.concatenate` de NumPy para juntar los dos bloques del arreglo de un solo jalón aprovechando los índices.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Descarté mi ciclo iterativo por completo y metí la línea `np.concatenate((X_revuelto[:inicio], X_revuelto[fin:]))` que me recomendó la IA. Lo cambié porque el código queda mucho más corto, hace exactamente lo mismo y no rompe la regla de hacerlo desde cero porque solo es manejo de matrices.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, funcionó a la perfección. Logró unir las matrices al instante sin desacomodar nada, y el accuracy en mis pruebas del K-Fold salió igual de bien que con mi `for`, pero el código se ve más limpio.

## Registro 06: Diferencia conceptual entre 1-NN y Distancia Mínimo
- **Fecha y herramienta:** 12 de noviembre de 2026, Gemini.
- **Prompt exacto enviado:** "no entendi, en el 1-NN también le tengo que sacar el centroide como al otro o aquí cómo calculo para ver el vecino?"
- **Resumen del output recibido:** La IA aclaró que en 1-NN no se calculan promedios ni centroides. Se debe calcular la distancia del dato nuevo de prueba contra todos y cada uno de los puntos originales del entrenamiento, quedándose con la etiqueta del que dé la distancia más pequeña.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se estructuró el código de 1-NN con un ciclo anidado que evalúa el punto de prueba contra el tamaño total de `X_train` (`len(X_train)`), garantizando que busca al vecino más cercano real y no un promedio.
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, corrigió una confusión conceptual importante antes de implementar el algoritmo.

