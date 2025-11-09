 import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# rutas de los archivos
ruta_entrada = r"C:\preprocesamiento-ciencia-datos\data\datasetoriginal\car_price_prediction_.csv"
ruta_salida = r"C:\preprocesamiento-ciencia-datos\data\procesado\cars_preprocessed.csv"

# asegurarse de que la carpeta de salida exista
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

# cargamos el dataset
df = pd.read_csv(ruta_entrada)
print("Primeras filas del dataset:")
print(df.head())  # mostrar las primeras filas del dataset

# análisis exploratorio de datos
print("\nInformación general del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

# imputamos los valores nulos
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].mean()) 
    else:
        df[col] = df[col].fillna(df[col].mode()[0]) 

# eliminamos los datos duplicados
df.drop_duplicates(inplace=True)

# codificamos las variables categóricas
categorical_cols = df.select_dtypes(include='object').columns

# usamos one-hot encoding para las variables categóricas
print("\nAplicando One-Hot Encoding...")
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# normalizado y escala
numeric_cols = ['Engine Size', 'Mileage']
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# imprimimos el dataset preprocesado
print("\nDataset preprocesado:")
print(df.head())

# guardamos el dataset preprocesado
df.to_csv(ruta_salida, index=False)
print(f"\nDataset preprocesado guardado en '{ruta_salida}'")
