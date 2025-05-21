#!/usr/bin/env python
# coding: utf-8

# In[184]:


import pandas as pd

df = pd.read_json('departamentos.json')

df.to_csv('departamentos.csv', index=False)


# In[185]:


df.info() # Visualize metadata from the df


# In[186]:


# Delete duplicated data
df = df.drop_duplicates()
df.info()


# In[187]:


# Extract the numeric portion from the 'terreno' column and store it in the new 'dimensiones' column
# (e.g. converts '625 mt^2' to '625')
df['dimensiones'] = df['terreno'].str.split().str[0]

# Delete the 'terreno' column as its useful information has already been transferred to 'dimensiones'
df = df.drop(columns=['terreno'])


# In[188]:


# Display the first rows of the df to check that the 'dimensiones' column was correctly created
df.head()


# In[189]:


# Rename the 'price' column to 'precio'
df = df.rename(columns={'price': 'precio'})


# In[190]:


# Clean the 'precio' column

# Identify rows where 'price' starts with 'MN ' or 'USD ' (valid price formats)
valid_prices = df['precio'].str.startswith('MN')

# Keep only the rows with valid price formats to ensure data consistency
df = df[valid_prices].copy()

# Remove extra information that appears after the '\n'
# as some price entries contain maintenance details
df['precio'] = df['precio'].str.split('\n').str[0]

# In this dataframe all prices are in mexican pesos, so we can skip the usd conversion
# Keep only the numeric value (price)
df['precio'] = df['precio'].str.split().str[1]


# In[191]:


df.info()
df.head()


# In[192]:


# Extract the 'alcaldia' value from the 'col' column and store it on its own column
# The final str.strip() removes any leading or trailing whitespace characters from the extracted value
df['alcaldia'] = df['col'].str.split(',').str[-1].str.strip()

# Keep only the neighborhood name in the 'col' column, since the 'alcaldía' value has been transferred
# The final str.strip() removes any leading or trailing whitespace characters from the extracted value
df['col'] = df['col'].str.split(',').str[0].str.strip()


# In[193]:


df.head(10) # Verify the process worked


# In[194]:


# Define misspelled 'alcaldia' names and their corrected versions 
# This accounts for common formatting issues such as missing accents or punctuation
# (e.g. 'Gustavo A Madero' -> 'Gustavo A. Madero')
alcaldia_corrections = {
    'Alvaro Obregon': 'Álvaro Obregón',
    'Alvaro Obregón': 'Álvaro Obregón',
    'Coyoacan': 'Coyoacán',
    'Tlahuac': 'Tláhuac',
    'Magdalena Contreras': 'La Magdalena Contreras',
    'Azcapotzalco': 'Azcapotzalco',
    'Gustavo A Madero': 'Gustavo A. Madero',
    'Cuauhtemoc': 'Cuauhtémoc'
}

# Apply the correction
df['alcaldia'] = df['alcaldia'].replace(alcaldia_corrections)


# In[195]:


# List of valid 'alcaldia' values
valid_alcaldias = [
    'Álvaro Obregón', 'Azcapotzalco', 'Benito Juárez', 'Coyoacán', 'Cuajimalpa de Morelos',
    'Cuauhtémoc', 'Gustavo A. Madero', 'Iztacalco', 'Iztapalapa', 'La Magdalena Contreras',
    'Miguel Hidalgo', 'Milpa Alta', 'Tláhuac', 'Tlalpan', 'Venustiano Carranza', 'Xochimilco'
]

# Check which entries in the alcaldia column aren't in this list
invalid_alcaldias = df[~df['alcaldia'].isin(valid_alcaldias)]

# See invalid 'alcaldia' values just one time no matter how many times they repeat
df.loc[~df['alcaldia'].isin(valid_alcaldias), 'alcaldia'].unique()


# In[196]:


# Keep only the rows with valid 'alcaldia' values
df = df[df['alcaldia'].isin(valid_alcaldias)].copy()


# In[197]:


df.info()


# In[198]:


# Display the median apartment prices for each 'alcaldia'

# Turn the 'precio' column to float
df['precio'] = df['precio'].str.replace(',', '').str.strip() # Remove commas before conversion, as pd.to_numeric cannot process them
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')  # 'coerce' turns invalid values into NaN, if any

# Group by 'alcaldia' and get the the median price
median_prices = df.groupby('alcaldia')['precio'].median()

# Display the median house prices for all 'alcaldias' from the most expensive to the least
print(f'Median price of apartments by {median_prices.sort_values(ascending=False)}')


# In[199]:


# Verify the conversion worked
df['precio'].head(20)


# In[200]:


# Clean the 'recamaras', 'banos', and 'estacionamientos' columns by keeping just the numeric values
# (e.g. converts '4 baños' to '4', '3 rec.' to '3' and 'No disponible' to 'No' and then Nan)

import numpy as np

def clean_numeric(col):
    cleaned = col.str.strip().str.split().str[0].str.replace('.', '', regex=False)

    # Replace 'No' with np.nan
    cleaned = cleaned.replace('No', np.nan)
    return cleaned

df['recamaras'] = clean_numeric(df['recamaras'])
df['banos'] = clean_numeric(df['banos'])
df['estacionamientos'] = clean_numeric(df['estacionamientos'])


# In[201]:


# Convert to numeric (handle NaN values)
df[['recamaras', 'banos', 'estacionamientos']] = df[['recamaras', 'banos', 'estacionamientos']].apply(pd.to_numeric)

# Calculate medians
medians = df[['recamaras', 'banos', 'estacionamientos']].median()

# Replace NaN with medians
df.fillna(medians, inplace=True)

# Convert to integer type
df[['recamaras', 'banos', 'estacionamientos']] = df[['recamaras', 'banos', 'estacionamientos']].astype('Int64')


# In[202]:


# Show all the different values for each of the columns to verify the process worked
print(df['recamaras'].unique())
print(df['banos'].unique())
print(df['estacionamientos'].unique())


# In[203]:


# We can see the 'dimensiones' column is currently stored as an object type
# We need to convert it to integers for numerical operations
df.info()


# In[204]:


# Converts the column to numeric values, replacing non numeric values, if any, with nan
df['dimensiones'] = pd.to_numeric(df['dimensiones'], errors='coerce').astype('Int64')


# In[205]:


df.info() # Verify the conversion worked properly


# In[206]:


# Create column price per square meter
df['precio_por_mt2'] = df['precio'] / df['dimensiones']

# Groups by 'alcaldia' and calculates the median price per square meter for each
median_sqm_price_per_alcaldia = df.groupby('alcaldia')['precio_por_mt2'].median()

# Merge the median values back into the original DataFrame
df = df.merge(median_sqm_price_per_alcaldia.rename('precio_promedio_por_mt2_por_alcaldia'), on='alcaldia', how='left')


# In[207]:


# Verify the new columns were created successfully
df.head(10)


# In[208]:


# Let's create some additional features that might help the model
df['banos_por_habitacion'] = df['banos'] / df['recamaras']

df['habitaciones_totales'] = df['banos'] + df['recamaras']


# In[209]:


# Separar las características de la etiqueta
# Características (X), etiqueta (y)
# We'll remove the 'dir' and 'descripcion', 'col' columns as they contain unstructured text
df = df.drop(['dir', 'descripcion', 'col'], axis=1)

df = pd.get_dummies(df, columns=['alcaldia'])


X = df.drop(["precio"], axis=1)
y = df["precio"]


# In[210]:


df.info()


# In[211]:


# First, let's look at the distribution of prices
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['precio'], bins=30)
plt.title('Price Distribution - Before Transformation')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# In[212]:


# Apply log transformation to price
# A log transformation compresses large values and spreads out smaller ones, 
# creating a more symmetrically distributed dataset that aligns better with linear regression assumptions

# If the dataset contains values across different scales (e.g. price vs. square meters), logs help normalize these differences,
# making model coefficients more stable and reducing the impact of outliers
df['log_precio'] = np.log1p(df['precio'])

plt.figure(figsize=(10, 6))
plt.hist(df['log_precio'], bins=30)
plt.title('Log Price Distribution')
plt.xlabel('Log Price')
plt.ylabel('Frequency')
plt.show()


# In[213]:


# Identificar todas las columnas dummy de alcaldías
alcaldia_columns = [col for col in df.columns if col.startswith('alcaldia_')]

X = df[['recamaras', 'banos', 'estacionamientos', 'dimensiones'] + alcaldia_columns]
y = df['log_precio']


# In[220]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)


# In[221]:


X_train.shape


# In[222]:


y_train.shape


# In[223]:


X_test.shape


# In[224]:


y_test.shape


# In[225]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)


# In[227]:


print(model.score(X_train, y_train))
print(model.score(X_test, y_test))


# In[ ]:


# Estos son los datos de la casa que quieres predecir
datos_departamento = {
    'recamaras': 3,
    'banos': 2,
    'estacionamientos': 1,
    'dimensiones': 70
}

alcaldias = [
    'alcaldia_Azcapotzalco',
    'alcaldia_Benito Juárez',
    'alcaldia_Coyoacán',
    'alcaldia_Cuajimalpa de Morelos',
    'alcaldia_Cuauhtémoc',
    'alcaldia_Gustavo A. Madero',
    'alcaldia_Iztacalco',
    'alcaldia_Iztapalapa',
    'alcaldia_La Magdalena Contreras',
    'alcaldia_Miguel Hidalgo',
    'alcaldia_Tlalpan',
    'alcaldia_Tláhuac',
    'alcaldia_Venustiano Carranza',
    'alcaldia_Xochimilco',
    'alcaldia_Álvaro Obregón'
]

# Ahora creas un diccionario con las columnas dummy de alcaldía en 0
for alcaldia in alcaldias:
    datos_departamento[alcaldia] = 0

# Y activas la alcaldía correcta
datos_departamento['alcaldia_Tlalpan'] = 1

# Conviertes a DataFrame
df_departamento = pd.DataFrame([datos_departamento])

# Aseguras que el orden de columnas es el mismo que X
df_departamento = df_departamento[X.columns]

# Ahora predices
prediccion_log_precio = model.predict(df_departamento)

# Si quieres obtener el precio en lugar del logaritmo
precio_estimado = np.exp(prediccion_log_precio)[0]

print(f'${precio_estimado:,.0f}')

