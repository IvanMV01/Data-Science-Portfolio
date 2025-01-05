# Tp-1 ALC 2024 2C

# Funcionamiento entrega

La entrega tiene 3 archivos funcionales junto con una carpeta de proyecto de spyder. Esta el archivo con el nombre del grupo y dos archivos auxiliares que contienen funciones. El código del archivo principal esta separado en bloques con la intención de ser ejecutados en orden sucesivo. 

La entrega tiene un archivo de funciones junto a un Jupyter Notebook y la información utilizada para el análisis inter regional en formato `csv`. El código del archivo principal, el Jupyter Notebook, esta separado en bloques con la intención de ser ejecutados en orden sucesivo. 

El env utilizado deberá contener las bibliotecas especificadas en la sección de bibliotecas y se deberá de usar el env especificado, o cualquier otro que cumpla con los requisitos de manera idéntica o similar.

## Bibliotecas

Las siguientes bibliotecas son necesarias para la ejecución:
* numpy 1.25.2
* pandas 1.5.3
* matplotlib 3.7.1
* seaborn 0.12.2

Dejamos un comando para poder generar un `conda env` para correr la entrega.
```
conda create --name correccion_alc_tp1 python=3.11 seaborn=0.12.2 scikit-learn=1.2.2 matplotlib=3.7.1 numpy=1.25.2 pandas=1.5.3
conda activate correccion_alc_tp1
pip install spyder-kernels==2.5.0
```

Asimismo, también el comando para su remoción.
```
conda deactivate correccion_alc_tp1
conda remove --name correccion_alc_tp1 --all
```
