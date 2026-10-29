# Big Data - Análisis y Streaming de Pruebas Saber 11 (ICFES)

Repositorio oficial para el desarrollo del proyecto del curso de Big Data, enfocado en el procesamiento masivo y análisis de datos de las Pruebas Saber 11 en Colombia utilizando PySpark y Apache Kafka.

## 📁 Estructura del Proyecto
* **`batch_icfes.py`**: Script principal de PySpark para el procesamiento por lotes del archivo `saber_11.csv`, el cual realiza:
  1. Análisis de desempeño global por periodo.
  2. Estudio de brecha socioeconómica según el estrato de vivienda (`fami_estratovivienda`).
  3. Evaluación de rendimiento institucional cruzando el puntaje global y de matemáticas según el carácter del colegio.

## 🎥 Video de Sustentación y Demostración
Puedes ver la explicación y demostración completa del funcionamiento del proyecto en el siguiente enlace de YouTube:
👉 [https://youtu.be/QmzRcjKCPPc](https://youtu.be/QmzRcjKCPPc)

## 🛠️ Entorno de Ejecución
* **Entorno:** Máquina Virtual Ubuntu (VirtualBox)
* **Tecnologías:** Apache Spark (PySpark), Apache Kafka, Python.
