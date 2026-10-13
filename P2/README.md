<div align="center">

<table width="100%">
  <tr align="center">
    <td width="20%">
      <img src="https://www.ipndeportes.com/natacion/images/logo-ipn-guinda.png" alt="Logo IPN" width="90"/>
    </td>
    <td width="60%">
      <h2><strong>INSTITUTO POLITÉCNICO NACIONAL</strong></h2>
      <h3><strong>ESCUELA SUPERIOR DE CÓMPUTO</strong></h3>
    </td>
    <td width="20%">
      <img src="https://www.escom.ipn.mx/images/conocenos/escudoESCOM.png" alt=Logo ESCOM" width="120"/>
    </td>
  </tr>
</table>

<h2><strong>INTELIGENCIA ARTIFICIAL</strong></h2>

<br><br><br>

<h1 style="font-size: 3em;"><strong>PRACTICA 2</strong></h1>
<h2><strong>Análisis Exploratorio de Datos (EDA) y Preparación de Datasets</strong></h2>

<br><br><br><br>

<h3><strong>POR</strong></h3>
<h3><strong>ANGELES PARRA ARGELIA</h3>
<h3><strong>CONTRERAS MARTINEZ RAUL</strong></h3>
<h3><strong>REYNA MENDOZA IAN GAEL</strong></h3>
<h3><strong>GRUPO 6CV2</strong></h3>

<br><br><br><br>

<h3><strong>PROFESOR</strong></h3>
<h3><strong>ANDRES GARCIA FLORIANO</strong></h3>

</div>

## ¿De qué trata esta práctica?

El objetivo principal de esta práctica es aprender a **auditar, limpiar y preparar datos reales antes de meterlos a un modelo de Machine Learning**. 

Muchas veces pensamos que la inteligencia artificial es solo entrenar modelos, pero en la realidad, si alimentas a un clasificador con datos sucios, incompletos o desbalanceados, los resultados van a ser engañosos (el famoso *"garbage in, garbage out"*). Por eso, en esta práctica tomamos **dos datasets de clasificación del mundo real**, diagnosticamos sus problemas y justificamos paso a paso cada decisión de preprocesamiento:

1. **Titanic (Supervivencia):** El clásico problema de predecir si un pasajero sobrevivió o no. Es ideal para aprender a manejar datos faltantes (en edad y cabina), variables mixtas (números, texto, categorías) y sesgos históricos.
2. **Telco Customer Churn (Abandono de Clientes):** Un problema clásico de negocios donde queremos predecir si un cliente va a cancelar su servicio de telefonía/internet. Tiene variables numéricas, categorías y un desbalance de clases marcado.

---

## 📁 ¿Cómo está organizada esta carpeta?

Diseñamos una estructura limpia y ordenada para que cualquiera pueda revisar el código y reproducir los resultados sin complicaciones:

```text
P2/
├── data/
│   ├── raw/                           <- Datasets originales (sin modificar)
│   │   ├── titanic.csv
│   │   └── Telco-Customer-Churn.csv
│   └── processed/                     <- Aquí se guardan los datos limpios y listos
├── docs/                              <- Reportes, fichas técnicas y diapositivas
├── env/                               <- Entorno virtual de Python con las librerías
├── notebooks/
│   └── EDA_Limpieza.ipynb             <- Nuestro cuaderno principal con todo el análisis y código
├── requirements.txt                   <- Requerimientos mínimos para ejecutarla
├── ai_log.md                          <- Bitacora de uso de IA
└── README.md                          <- Esta guía que estás leyendo
```

---

## 💻 ¿Cómo correr el proyecto?

1. **Clonar o descargar el repositorio** y abrir una terminal en la carpeta del proyecto.
2. **Activar el entorno virtual:**
   ```bash
   # En Windows:
   .\env\Scripts\Activate.ps1
   # En Mac/Linux:
   source env/bin/activate
   ```
3. **Abrir el cuaderno:**
   ```bash
   jupyter notebook notebooks/EDA_Limpieza.ipynb
   ```
4. Ejecutar las celdas en orden de arriba a abajo. Todas las rutas de los archivos están configuradas de forma relativa para que corran a la primera sin errores.
