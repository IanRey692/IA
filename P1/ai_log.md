# Bitácora de Uso de IA (ai_log.md)

## Registro 01: Asistencia en depuración y APIs periféricas
* **Fecha y herramienta:** 24 de septiembre de 2026, Gemini.
* **Prompt exacto enviado:** "Me sale un error de NameError en el mapa:"
* **Resumen del output recibido:** La IA identificó que faltaba definir las variables `latitud` y `longitud` en la memoria del kernel tras reiniciar el entorno, y sugirió cambiar el proveedor de teselas en `folium` a un servidor compatible para evitar el bloqueo 403.
* **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó la lógica para extraer las coordenadas directamente del grafo y el cambio de proveedor cartográfico, ya que las políticas de uso de OpenStreetMap denegaban las peticiones repetidas del script.
* **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, fue técnicamente correcto; permitió solucionar el conflicto de alcance de variables del *kernel* y restableció la generación visual de los mapas, ya que no se lograban apreciar de una buena manera y en el mapa aparecian las rutas pero no el mapa en limpio.

## Registro 02: Asistencia para Error de Sintaxis 
* **Fecha y herramienta:** 23 de septiembre de 2026, Gemini.
* **Prompt exacto enviado:** "Me arrojó un SyntaxError en test_rutas.py al intentar asignar el atributo en G.add_edge(1, 2, 0={'length': 10.0}). ¿Cómo lo soluciono?"
* **Resumen del output recibido:** La IA identificó que en Python no se pueden usar números enteros directamente como nombres de parámetros clave. Sugirió cambiar el tipo de grafo base a nx.MultiDiGraph() y asignar los atributos usando la sintaxis key=0, length=10.0 para replicar el formato exacto de OSMnx.
* **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se hizo una reestructuración completa del MultiDiGraph y la nueva sintaxis de asignación de atributos, ya que era estrictamente necesario para que el grafo ficticio de pruebas fuera compatible con el código original de las Fases 1 y 2.
* **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, eliminó el error de sintaxis y permitió que la estructura de datos del grafo de prueba imitara a la perfección los mapas de la ciudad.

## Registro 03: Asistencia para configuración de PYTHONPATH para pruebas
* **Fecha y herramienta:** 23 de septiembre de 2026, Gemini.
* **Prompt exacto enviado:** "Al ejecutar pytest en la terminal, me aparece el error ModuleNotFoundError: No module named 'src'. ¿A qué se debe y cómo lo arreglo?"
* **Resumen del output recibido:** La IA explicó que el entorno de ejecución de la terminal no estaba reconociendo la subcarpeta src/ como un paquete válido de Python. Sugirió dos opciones: ejecutar pytest a través del módulo de Python usando la bandera -m (python -m pytest) o crear un archivo __init__.py
* **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se optó por ejecutar python -m pytest tests/test_rutas.py -v por ser la opción más rápida, para no realizar la creación de archivos adicionales.
* **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, al forzar la inclusión de la ruta actual en las variables de entorno, la terminal logró descubrir los módulos y ejecutar los tests.
