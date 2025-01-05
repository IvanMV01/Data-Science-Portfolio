from sklearn.decomposition import PCA
from funciones import metodoPotencia
import numpy as np
import pandas as pd

def matriz_E_n(n):
    # Crear la matriz identidad I_n
    I_n = np.eye(n)
    
    # Crear el vector columna e
    e = np.ones((n, 1))

    # Calcular E_n
    E_n = I_n - (1/n) * (e @ e.T)

    return E_n

# Cargo la data que esta en formato csv
df = pd.read_csv(r"data_paises.csv")

# Selecciono GTM y NIC, Guatemala y Nicaragua
df_gtm = df[df["Country_iso3"] == "GTM"]
df_nic = df[df["Country_iso3"] == "NIC"]

# Consigo los P 
P_gtm = df_nic["Output"]
P_nic = df_nic["Output"]

# Cambio los 0s a 1s para poder conseguir las A
P_nic = np.array(P_nic.replace({0:1}))
P_gtm = np.array(P_gtm.replace({0:1}))

# Creo cuatro df que representan las matrices Z
df_gtm_gtm = df_gtm[[col for col in df_gtm.columns if (col.startswith("GTM"))]]
df_gtm_nic = df_gtm[[col for col in df_gtm.columns if (col.startswith("NIC"))]]
df_nic_gtm = df_nic[[col for col in df_nic.columns if (col.startswith("GTM"))]]
df_nic_nic = df_nic[[col for col in df_nic.columns if (col.startswith("NIC"))]]

# Mando a matriz de coef. técnicos
A_nic_nic = np.array(df_nic_nic) / P_nic
A_nic_gtm = np.array(df_nic_gtm) / P_gtm
A_gtm_nic = np.array(df_gtm_nic) / P_nic
A_gtm_gtm = np.array(df_gtm_gtm) / P_gtm

# Renombro
A1 = A_nic_nic

# Normalizamos la matriz de coeficientes para la economía interna de Nicaragua
n = 40
E_40 = matriz_E_n(n)
A1_norm = E_40 @ A1

# Aplico pca de sklearn
pca = PCA(n_components=1)
pca.fit(A1_norm)    

# Calculamos la matriz de covarianza
C1 = (A1_norm.T @ A1_norm) / (40-1)

# Primer autovector y autovalor
lambda_1, v1 = metodoPotencia(C1)

# Chequeo de convergencia via isclose con rtol de 17 decimales
print(
        "Correspondencia de métodos:", 
        np.isclose(lambda_1, pca.explained_variance_[0], rtol=1e-17)
    )
