# Bitácora de Uso de IA (ai_log.md)

## Registro 01: Asistencia en depuración y APIs periféricas
* **Fecha y herramienta:** 24 de agosto de 2026, Gemini.
* **Prompt exacto enviado:** "Me sale un error de NameError en el mapa:"
* **Resumen del output recibido:** La IA identificó que faltaba definir las variables `latitud` y `longitud` en la memoria del kernel tras reiniciar el entorno, y sugirió cambiar el proveedor de teselas en `folium` a un servidor compatible para evitar el bloqueo 403.
* **Qué parte del output se incorporó, modificó o descartó, y por qué:** Se incorporó la lógica para extraer las coordenadas directamente del grafo y el cambio de proveedor cartográfico, ya que las políticas de uso de OpenStreetMap denegaban las peticiones repetidas del script.
* **¿El output fue técnicamente correcto? Si no, qué error tenía y cómo se detectó?** Sí, fue técnicamente correcto; permitió solucionar el conflicto de alcance de variables del *kernel* y restableció la generación visual de los mapas, ya que no se lograban apreciar de una buena manera y en el mapa aparecian las rutas pero no el mapa en limpio.