from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa la sesión de Spark para el análisis Saber 11
spark = SparkSession.builder.appName('AnalisisSaber11').getOrCreate()

# Leer el archivo CSV de las Pruebas Saber 11
df_saber11 = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .csv("saber_11.csv")

# Normalizar nombres de columnas a minúsculas
df_saber11 = df_saber11.toDF(*(c.lower() for c in df_saber11.columns))

print("--- ARCHIVO LEÍDO CORRECTAMENTE EN MODO BATCH ---")

if "punt_global" in df_saber11.columns:
    df_cleaned = df_saber11.filter(col("punt_global").isNotNull())

    # 1. Desempeño por Periodo
    print("\n=== 1. DESEMPEÑO POR PERIODO ===")
    df_cleaned.groupBy("periodo") \
        .avg("punt_global") \
        .orderBy(col("avg(punt_global)").desc()) \
        .show(10, truncate=False)

    # 2. Brecha Socioeconómica
    print("\n=== 2. BRECHA SOCIOECONÓMICA (Impacto del Estrato) ===")
    df_cleaned.groupBy("fami_estratovivienda") \
        .avg("punt_global") \
        .orderBy("fami_estratovivienda") \
        .show(10, truncate=False)

    # 3. Rendimiento Institucional
    print("\n=== 3. RENDIMIENTO INSTITUCIONAL (Carácter del Colegio) ===")
    df_cleaned.groupBy("cole_caracter") \
        .agg({"punt_global": "avg", "punt_matematicas": "avg"}) \
        .show(10, truncate=False)
else:
    print("No se encontró la columna de puntaje global.")
