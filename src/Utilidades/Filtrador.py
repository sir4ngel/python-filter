import pandas as pd
import re

class C_Filtrador:
    # Metodo filtrar en el que ingresamos la ruta del archivo y las palabras a filtrar en el mismo.
    def filtrar(archivo, palabras, ruta):
        # Usamos la libreria pandas con su metodo read_csv en el cual ingresaremos el archivo pasado en los parametros y una opcion extra de encoding
        # ... ya que la base de datos tiene datos con este tipo de encoding.
        df = pd.read_csv(archivo, encoding='ISO-8859-2')

        # Creamos una variable nueva a la que le asignaremos un nuevo DataFrame con la busqueda en la columna texto y las palabras pasadas en los
        # ... parametros
        columna_filtrada = df['Texto'].str.contains('|'.join(palabras), case=False, na=False, regex=True)
        archivo_filtrado = df[columna_filtrada]

        # Creamos un nuevo dataframe para poder convertirlo a csv
        dfFiltrado = pd.DataFrame(archivo_filtrado)

        # Finalmente guardamos la nueva base de datos filtrada en la carpeta del codigo.
        dfFiltrado.to_csv(ruta)