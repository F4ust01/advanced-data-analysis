import csv
import MySQLdb
import sys
import pandas as pd
import matplotlib.pyplot as plt  # Importa pyplot correctamente

# Abre el archivo CSV en modo lectura
with open('companydata.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)  # Omitir la primera fila que contiene encabezados

    # La lectura del archivo CSV debe estar dentro de este bloque
    try:
        # Conectarse a la base de datos MySQL
        db = MySQLdb.connect("localhost", "root", "", "companydata")
        print("Conexión correcta.")
    except MySQLdb.Error as e:
        print("No se pudo conectar a la base de datos:", e)
        sys.exit(1)

    # Leer datos del CSV en un DataFrame de pandas
    data = pd.read_csv('companydata.csv')

# performance_score: datos
# media
print(data['performance_score'].mean())

# mediana
print(data['performance_score'].median())

# desviacion estandar
print(data['performance_score'].std())

# salary: datos
# media
print(data['salary'].mean())

# mediana
print(data['salary'].median())

# desviacion estandar
print(data['salary'].std())

# numero total de empleados por departamento
employees_per_department = data.groupby('department')['employee_id'].count()

print("Número total de empleados por departamento:")
print(employees_per_department)

# correlacion entre years_with_company y performance_score
correlation = data['years_with_company'].corr(data['performance_score'])
print(f"La correlación entre years_with_company y performance_score es: {correlation}")

# correlacion entre salary y performance_score
correlation2 = data['salary'].corr(data['performance_score'])
print(f"La correlación entre salary y performance_score es: {correlation2}")

# Crear histogramas del performance_score para cada departamento
departments = data['department'].unique()
for department in departments:
    plt.figure(figsize=(10, 6))
    subset = data[data['department'] == department]
    plt.hist(subset['performance_score'], bins=10, edgecolor='black')
    plt.title(f'Histograma del Performance Score para el departamento: {department}')
    plt.xlabel('Performance Score')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

# Crear un gráfico de dispersión de years_with_company vs. performance_score
plt.figure(figsize=(10, 6))
plt.scatter(data['years_with_company'], data['performance_score'], alpha=0.5)
plt.title('Gráfico de dispersión de Years with Company vs. Performance Score')
plt.xlabel('Years with Company')
plt.ylabel('Performance Score')
plt.grid(True)
plt.show()

# Crear un gráfico de dispersión de salary vs. performance_score
plt.figure(figsize=(10, 6))
plt.scatter(data['salary'], data['performance_score'], alpha=0.5)
plt.title('Gráfico de dispersión de Salary vs. Performance Score')
plt.xlabel('Salary')
plt.ylabel('Performance Score')
plt.grid(True)
plt.show()

# Cerrar la conexión a la base de datos
db.close()
