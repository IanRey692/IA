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

## Registro 07: Advertencias de convergencia (ConvergenceWarning) en el MLP
- **Fecha y herramienta:** 15 de noviembre de 2026, Claude.
- **Prompt exacto enviado:** "de esta forma tiene que correr?" (con texto pegado de la celda de evaluación de SVM y MLP).
- **Resumen del output recibido:** La IA indicó que los resultados de SVM y MLP eran razonables (Iris arriba de 0.95 y el sintético cerca de 0.75). Explicó que los `ConvergenceWarning` son avisos y no errores: con las 200 iteraciones por defecto el MLP no siempre converge, y se pueden quitar subiendo `max_iter` en el ajuste de parámetros.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó la explicación y se silenció el aviso con `warnings.filterwarnings("ignore")` en la tabla comparativa. En la sección de ajuste de parámetros se usó `max_iter=2000`. 
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí. La explicación coincide con el mensaje de scikit-learn ("Maximum iterations (200) reached and the optimization hasn't converged yet"). Silenciar el aviso no cambia los resultados.

## Registro 08: Resultados de la conclusión que no coincidían con la tabla final
- **Fecha y herramienta:** 15 de noviembre de 2026, Claude.
- **Prompt exacto enviado:** "Analiza los resultados y determina si estos son correctos para lo determinado" (con texto pegado de la tabla final de los seis modelos) y después "Podrias definir que debemos ajustar".
- **Resumen del output recibido:** La IA confirmó que la tabla era correcta (misma partición y mismos folds para todos), pero señaló que la Conclusión del notebook usaba números de corridas anteriores sin semilla fija (74.33%, 59.33%) y afirmaba que K-NN era "el más robusto" en el sintético, cuando SVM (0.75) y MLP (0.7533) lo igualaban o superaban (0.7233). Propuso reescribirla con los valores de la tabla final y tratar a K-NN, SVM y MLP como un empate práctico, dado que la diferencia es de 2 a 3 puntos con 300 datos.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se propuso la reescritura de la Conclusión con los números de la tabla final y la idea del empate.  
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí en los números, que se verificaron contra la tabla. Una imprecisión: en una versión inicial la Conclusión decía "más de 0.92 en K-Fold" en Iris, pero Distancia Mínima tiene justo 0.92; se detectó al revisar el notebook completo y se cambió a "0.92 o más".

## Registro 09: El ajuste de parámetros no mejoró los resultados
- **Fecha y herramienta:** 15 de noviembre de 2026, Claude.
- **Prompt exacto enviado:** "el ajuste de estos parametros coinciden con los resultados que se tendrian que obtener?"
- **Resumen del output recibido:** La IA aclaró que el código no falló: los "Test default" coincidían con la tabla anterior. Lo inesperado era que el ajuste no mejoró en el sintético (SVM 0.7444 a 0.7333) y que el MLP empeoró de 0.7444 a 0.6000. Propuso como explicaciones posibles que Iris ya estaba cerca del máximo, que con etiquetas ruidosas los puntajes de las combinaciones quedan muy pegados y la mejor se elige en parte por suerte, que el MLP por defecto se detenía a las 200 iteraciones y con `max_iter=2000` se ajusta más al ruido, y que solo hay 90 datos de prueba. También sugirió una validación cruzada anidada para comparar de forma más robusta.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó la interpretación para responder "¿Mejoraron los resultados?" en el reporte, redactada con "creemos" porque son hipótesis. 
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Parcialmente. El diagnóstico de que no era un error de código es correcto, pero las causas del 0.6000 del MLP son hipótesis que no se comprobaron con otra corrida. Además, la IA dictó que el 15% de las etiquetas se cambiaba al azar, y eso es impreciso: `flip_y=0.15` asigna una clase al azar al 15% de los datos y algunas coinciden con la original, así que se cambian un poco menos. Se detectó al revisar la documentación de `make_classification`.


## Registro 10: Error NameError: accuracy_score is not defined
- **Fecha y herramienta:** 14 de noviembre de 2026, Claude.
- **Prompt exacto enviado:** "¿Por qué salió NameError: accuracy_score is not defined?"
- **Resumen del output recibido:** La IA aclaró que se había reiniciado el kernel y las celdas de arriba no estaban cargadas. Se resolvió con Run All.
- **Qué parte del output se incorporó, modificó o descartó, y por qué:** Ninguno, solo se corrio de nuevo el notebook. 
- **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, corrigió un error de flujo. 