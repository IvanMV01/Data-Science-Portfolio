{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "5c0cbb93-2880-4750-975d-11cce9f6b12c",
   "metadata": {},
   "source": [
    "# Trabajo Práctico 1 - Matrices de Insumo Producto"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11f7face-a325-4e30-b13e-0c3d84280c5e",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "### Consigna 1 - Análisis del sistema según $(I-A)$ y $d$\n",
    "\n",
    "Empezamos por el caso en el que $(I-A)$ es inversible y asumimos que $d=0$ para poder diferenciarlo del siguiente caso de análisis. Cuando sucede esto, tenemos un sistema **compatible determinado** el cual tendrá solución única para un $d$ determinado no nulo.\n",
    "\n",
    "Por otro lado, si $(I-A)$ continua siendo inversible pero ahora asumimos que $d=0$, entonces tenemos un sistema homogéneo. A partir de que sabemos que la matriz de Leontief es inversible, por ende, tiene $dim(Ker(L)) = 0$. Por lo tanto, la única respuesta al sistema es $p=0$, la solución trivial. Esto también es más palpable al partir del sistema (1).\n",
    "\n",
    "$$p=A\\cdot p+d$$\n",
    "\n",
    "$$d=0\\Rightarrow p=A\\cdot p\\Longleftrightarrow (I-A)\\cdot p = 0$$\n",
    "\n",
    "$$\\Longleftrightarrow p=0$$\n",
    "\n",
    "Luego, tenemos el caso de un sistema en el que la matriz de Leontief no es inversible y, además, $d\\neq 0$. En esta situación, ni siquiera podríamos plantear la ecuación que veníamos viendo, llegaríamos a que $p\\cdot (I-A) = d$ y no podríamos invertir $L$ para conseguir $p$. Nos quedaríamos con que el sistema tiene dos posibles casos: **compatible indeterminado** e **indeterminado**. Ahora, si el vector $d$ llega a estar incluido en la imagen de la matriz de nuestro sistema, el sistema va a ser compatible indeterminado, habría infinitas soluciones. En el caso contrario ($d$ no pertenece a la imagen), el sistema no va a tener solución, deberíamos de llegar a un absurdo.\n",
    "\n",
    "Por último, el caso de $(I-A)$ no inversible y $d=0$, automáticamente pasamos a un sistema homogéneo en el que la matriz que tenemos tiene $dim(Ker(I-A))\\neq0$, es decir, tendríamos infinitas soluciones porque es un sistema **compatible no determinado**. Sería como resolver el núcleo de la matriz en cuanto a $p$.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ea60699-4c07-40fb-8f71-ec4cacf32708",
   "metadata": {},
   "source": [
    "### Consigna 2 - Descomposición $LU$ e inversa\n",
    "\n",
    "Ver en `funciones.py` la definición de cada función con su correspondiente desarrollo y *docstring*."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "260b913f-d6d3-47b8-9431-7a64d6d037a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from funciones import calcularLU, inversaLU"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6527567-ea14-4fb0-8cbb-3faa67fee8c1",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c69cb1df",
   "metadata": {},
   "source": [
    "### Consigna 3 - Caso de resolución especifico \n",
    "\n",
    "Hay que resolver el sistema usando la función `inversaLU` para los siguientes valores de $A$ y $d$. \n",
    "\n",
    "$$\n",
    "A =\n",
    "    \\begin{pmatrix}\n",
    "    0.3 & 0  & 0.1\\\\\n",
    "    0.05 & 1.0 & 0.2\\\\\n",
    "    0.1 & 0.15 & 0.1 \\\\\n",
    "    \\end{pmatrix}\n",
    "\n",
    "\\qquad\n",
    "\n",
    "d = \\begin{pmatrix}\n",
    "    100 \\\\\n",
    "    100 \\\\\n",
    "    300 \\\\\n",
    "    \\end{pmatrix}\n",
    "$$\n",
    "\n",
    "Vamos a usar las funciones y matrices para calcular el sistema. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "07f69bd8-9a22-4fa0-8e69-7e2580e80459",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vector solución:\n",
      "[[   68.96551724]\n",
      " [-5149.42528736]\n",
      " [ -517.24137931]]\n"
     ]
    }
   ],
   "source": [
    "# Declaro A y d\n",
    "A = np.array([\n",
    "    [.3, .0, .1],\n",
    "    [.05, 1.0, .2],\n",
    "    [.1, .15, .1]\n",
    "])\n",
    "d = np.array([[100], [100], [300]])\n",
    "\n",
    "# Consigo la matriz (I - A) (M) y la descompongo\n",
    "M = (np.eye(A.shape[0]) - A)\n",
    "L, U, P = calcularLU(M)\n",
    "\n",
    "# Invierto la matriz y resuelvo el sistema\n",
    "invLU = inversaLU(L, U, P)\n",
    "p = invLU @ d\n",
    "print(\"Vector solución:\\n\", p, sep=\"\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a42545f",
   "metadata": {},
   "source": [
    "Vemos que la solución al sistema parece ser bastante peculiar en el sentido de que la segunda y tercer posición del vector producción son negativas y, además, la segunda posición es mucho mayor en valor absoluto que el resto de componentes. No tiene sentido que un sistema nos informe que nuestro vector $p$ de total producido tiene componentes negativos e incluso de gran magnitud en relación al anterior $p$, es como decir que nos falta producir. Creemos que esto indica que el sistema consumé más de lo que produce y/o que la demanda es mucho más alta de lo que el sistema puede llegar a producir. \n",
    "\n",
    "Sospechamos que la característica de la matriz que hace que esto sea así es que $(A)_{2,2} = 1$. Esto sugiere que para llegar a la producción $p$ siguiente, necesitamos el 100% de ese sector dedicado a el mismo. Creemos fuertemente que la suma de cada fila no debería exceder 1 para tener un sistema sostenible. De todas formas, esto no involucra un cambio potencial para la demanda."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19403a3c-422b-4bdb-85b3-058b90560067",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5d4ff39",
   "metadata": {},
   "source": [
    "### Consigna 4 - Análisis de $\\Delta p$ según un $\\Delta d$ en Consigna 3\n",
    "\n",
    "(Ver que afecta a la tercer col de Leontief)\n",
    "\n",
    "Ahora deberíamos ver que sucede (analíticamente) si perturbamos el sistema con un $\\Delta d$, osea, ver que sucede cuando aumentamos la demanda con $\\Delta d = (0, 0, 1)^t$. Usar este vector sería como aumentar en la demanda en el tercer sector por una única unidad. Veamos como queda el sistema a partir de la introducción del *shock*, empezamos con el sistema de antes pero anticipamos que vamos a tener una $\\Delta p$ relativamente \"chica\" a la obtenida en la Consigna 3. \n",
    "\n",
    "$$p'=L\\cdot d' \\Longleftrightarrow p + \\Delta p = L \\cdot (d + \\Delta d)$$\n",
    "\n",
    "$$\\Rightarrow \\Delta p = L\\cdot d + L\\cdot\\Delta d - p$$\n",
    "\n",
    "Por definición, sabemos que $p = L\\cdot d$, entonces:\n",
    "\n",
    "$$\\Longrightarrow \\Delta p = L\\cdot\\Delta d$$\n",
    "\n",
    "Vemos que solo necesitamos procesar el shock por separado para entender como va a afectar a la producción total."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "10993b2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vector solución con shock:\n",
      "[[ 0.        ]\n",
      " [-6.66666667]\n",
      " [ 0.        ]]\n"
     ]
    }
   ],
   "source": [
    "# Declaro el shock\n",
    "delta_d = np.array([[0], [0], [1]])\n",
    "\n",
    "# Ya tenemos la matris de Leontief en memoria\n",
    "delta_p = invLU @ delta_d\n",
    "print(\"Vector solución con shock:\\n\", delta_p, sep=\"\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdd55814",
   "metadata": {},
   "source": [
    "Es bastante interesante que un aumento de demanda en el tercer sector genere que la producción total se vea afectado en el segundo sector, algo que no esperábamos. Sumado a esto, podemos ver que hay un leve aumento en módulo de parte del shock que se produjo. Aclaramos que el hecho de que la demanda sea $e_3$ implica que se utilice la tercera columna de la matriz de Leontief para determinar la producción.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff8b6c3d",
   "metadata": {},
   "source": [
    "### Consigna 5 - Coeficientes técnicos\n",
    "\n",
    "Vemos que, según lo que informan, tenemos que la matriz de coeficientes técnicos es $A = Z\\cdot P^{-1}$, sabemos que $Z$ representa la demanda interna y la $P$ es el total producido. Por ende:\n",
    "\n",
    "$$A = Z\\cdot P^{-1} =\n",
    "\\begin{pmatrix}\n",
    "    350 & 0 & 0 \\\\\n",
    "    50 & 250 & 150 \\\\\n",
    "    200 & 150 & 550 \\\\\n",
    "\\end{pmatrix}\n",
    "\\cdot\n",
    "\\begin{pmatrix}\n",
    "    \\frac{1}{1000} & 0 & 0 \\\\\n",
    "    0 & \\frac{1}{500} & 0 \\\\\n",
    "    0 & 0 & \\frac{1}{1000}\\\\\n",
    "\\end{pmatrix} =\n",
    "\\begin{pmatrix}\n",
    "    0.35 & 0 & 0 \\\\\n",
    "    0.05 & 0.5 & 0.15 \\\\\n",
    "    0.2 & 0.3 & 0.55 \\\\\n",
    "\\end{pmatrix}\n",
    "$$\n",
    "\n",
    "Ahora que sabemos la matriz $A$ podemos calcular tranquilamente su inversa con el código previamente establecido:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c3f846de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.53846154 0.         0.        ]\n",
      " [0.44871795 2.5        0.83333333]\n",
      " [0.98290598 1.66666667 2.77777778]]\n"
     ]
    }
   ],
   "source": [
    "# Defino A\n",
    "A = np.array([\n",
    "    [.35, 0, 0],\n",
    "    [.05, .5, .15],\n",
    "    [.2, .3, .55]\n",
    "])\n",
    "\n",
    "# Calculo la inversa via descomposición LU\n",
    "M = np.eye(3) - A\n",
    "L, U, P = calcularLU(M)\n",
    "leontief = inversaLU(L, U, P)\n",
    "\n",
    "print(leontief)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9ae0cd3",
   "metadata": {},
   "source": [
    "Esta sería la matriz de Leontief para la economía propuesta por la consigna. \n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Consigna 6 - Demostración de Ecuación de Modelo Inter Regional\n",
    "\n",
    "Partimos del hecho de que sabemos como se que un sistema inter regional y que, por imposición, tenemos que el *shock* de demanda de Nicaragua es nulo.\n",
    "\n",
    "$$\n",
    "\\left[\n",
    "\\begin{pmatrix}\n",
    "I_{n \\times n} & 0_{n \\times m} \\\\\n",
    "0_{m \\times n} & I_{m \\times m}\n",
    "\\end{pmatrix}\n",
    "-\n",
    "\\begin{pmatrix}\n",
    "A ^{rr} & A ^{rs} \\\\\n",
    "A ^{sr} & A ^{ss}\n",
    "\\end{pmatrix}\n",
    "\\right]\n",
    "\\cdot\n",
    "\\begin{pmatrix}\n",
    "\\Delta p^r \\\\\n",
    "\\Delta p^s\n",
    "\\end{pmatrix}\n",
    "=\n",
    "\\begin{pmatrix}\n",
    "\\Delta d ^ r\\\\\n",
    "0\n",
    "\\end{pmatrix}\n",
    "$$\n",
    "\n",
    "$$\n",
    "\\Rightarrow\n",
    "\\begin{pmatrix}\n",
    "I - A ^{rr} & -A ^{rs} \\\\\n",
    "-A ^{sr} & I - A ^{ss}\n",
    "\\end{pmatrix}\n",
    "\\cdot\n",
    "\\begin{pmatrix}\n",
    "\\Delta p^r \\\\\n",
    "\\Delta p^s\n",
    "\\end{pmatrix}\n",
    "=\n",
    "\\begin{pmatrix}\n",
    "\\Delta d ^ r\\\\\n",
    "0\n",
    "\\end{pmatrix}\n",
    "$$\n",
    "\n",
    "$$\n",
    "\\Rightarrow\n",
    "\\begin{cases}\n",
    "(I - A ^{rr}) \\cdot \\Delta p^r - A^{rs} \\cdot \\Delta p^s = \\Delta d ^ r \\quad (1) \\\\\n",
    "- A ^{sr} \\cdot \\Delta p^r + (I - A^{ss}) \\cdot \\Delta p^s = 0 \\quad (2)\n",
    "\\end{cases}\n",
    "$$\n",
    "\n",
    "De (2) vemos que podemos llegar a una igualdad para $\\Delta p^s$: \n",
    "\n",
    "$$ (I - A^{ss}) \\cdot \\Delta p^s =  A ^{sr} \\cdot \\Delta p^r $$\n",
    "\n",
    "$$\n",
    "\\Delta p^s = (I - A^{ss})^{-1} \\cdot A ^{sr} \\cdot \\Delta p^r\n",
    "$$\n",
    "\n",
    "Reemplazando en (1) tenemos que: \n",
    "\n",
    "$$ (I - A ^{rr}) \\cdot \\Delta p^r - A^{rs} \\cdot (I - A^{ss})^{-1} \\cdot A ^{sr} \\cdot \\Delta p^r = \\Delta d^r $$\n",
    "\n",
    "$$ \\Rightarrow  \\Delta p^r\\cdot((I - A ^{rr}) - A^{rs} \\cdot (I - A^{ss})^{-1} \\cdot A ^{sr}) = \\Delta d^r $$\n",
    "\n",
    "Queda demostrado lo propuesto por el ejercicio pero además observamos que, para obtener el $\\Delta p^r$ de un sistema inter regional, necesitamos primero calcular la demanda a partir de lo encontrado con esta matriz de Leontief y la producción total. Luego podríamos abordar los deltas ya que sabemos por la Consigna 4 que el calculo de $P$ y $\\Delta P$ se da por separado. \n",
    "\n",
    "$$\n",
    "\\begin{align}\n",
    "    d^r &= p^r \\cdot[I - A^{rr} - A^{rs} \\cdot (I - A^{ss})^{-1} \\cdot A^{sr}] \\\\\n",
    "    \\Delta p^r &= [I - A^{rr} - A^{rs} \\cdot (I - A^{ss})^{-1} \\cdot A^{sr}]^{-1} \\cdot \\Delta d^r\n",
    "\\end{align}\n",
    "$$\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81ad1ab8",
   "metadata": {},
   "source": [
    "### Consigna 7 - Sistema Insumo Producto entre países\n",
    "\n",
    "<u>Aclaración</u>: ¡GTM es el primer país!\n",
    "\n",
    "Tenemos el contexto de que hay que resolver un sistema que relaciona dos países. En el caso del grupo, los países son Guatemala (GTM y Nicaragua (NIC). Para ambos países tenemos 40 sectores, esto quiere decir que la matriz Insumo Producto de este sistema es de 80x80. Hay un pequeño detalle que puede afectar a como armar las matrices $A = Z\\cdot P^{-1}$, hay algunos sectores que parecen ser nulos en su producción, no es bueno porque implica que $P$ podría tener división por 0 en alguna/s de sus posiciones. Para evitar esto, reemplazamos todos los 0 por 1, esto no debería ser un cambio significativo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d151df2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conteo de producción nula en GTM: 7\n",
      "Conteo de producción nula en NIC: 7\n"
     ]
    }
   ],
   "source": [
    "# Cargo la data que esta en formato csv\n",
    "df = pd.read_csv(r\"data_paises.csv\")\n",
    "\n",
    "# Selecciono GTM y NIC, Guatemala y Nicaragua\n",
    "df_gtm = df[df[\"Country_iso3\"] == \"GTM\"]\n",
    "df_nic = df[df[\"Country_iso3\"] == \"NIC\"]\n",
    "\n",
    "# Consigo los P \n",
    "P_gtm = df_nic[\"Output\"]\n",
    "P_nic = df_nic[\"Output\"]\n",
    "\n",
    "# Veo los que tengan producción nula\n",
    "suma_nulos_P_gtm = sum([1 for i in P_gtm if i == 0])\n",
    "suma_nulos_P_nic = sum([1 for i in P_nic if i == 0])\n",
    "print(\"Conteo de producción nula en GTM:\", suma_nulos_P_gtm)\n",
    "print(\"Conteo de producción nula en NIC:\", suma_nulos_P_nic)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5633f82a",
   "metadata": {},
   "source": [
    "Vemos que para ambos países hay 7 sectores que tienen producción nula. En la siguiente celda ejecutamos un cambio de los ceros por unos para poder conseguir las matrices $A$ sin problema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "621ca30d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Cambio los 0s a 1s para poder conseguir las A\n",
    "P_nic = np.array(P_nic.replace({0:1}))\n",
    "P_gtm = np.array(P_gtm.replace({0:1}))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a69bfad5",
   "metadata": {},
   "source": [
    "Ahora si podemos calcular las matrices $A$ correspondientes a cada región y las inter regionales. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "efa82ed1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creo cuatro df que representan las matrices Z\n",
    "df_gtm_gtm = df_gtm[[col for col in df_gtm.columns if (col.startswith(\"GTM\"))]]\n",
    "df_gtm_nic = df_gtm[[col for col in df_gtm.columns if (col.startswith(\"NIC\"))]]\n",
    "df_nic_gtm = df_nic[[col for col in df_nic.columns if (col.startswith(\"GTM\"))]]\n",
    "df_nic_nic = df_nic[[col for col in df_nic.columns if (col.startswith(\"NIC\"))]]\n",
    "\n",
    "# Mando a matriz de coef. técnicos\n",
    "A_nic_nic = np.array(df_nic_nic) / P_nic\n",
    "A_nic_gtm = np.array(df_nic_gtm) / P_gtm\n",
    "A_gtm_nic = np.array(df_gtm_nic) / P_nic\n",
    "A_gtm_gtm = np.array(df_gtm_gtm) / P_gtm"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3adc1939",
   "metadata": {},
   "source": [
    "Bien, de momento tenemos las matrices que nos permiten calcular apropiadamente el sistema. Sólo falta resolver el sistemas con lo que sabemos de la Consigna 6. Sabemos que tenemos que resolver el sistema asumiendo que $r$ representa a Guatemala y $s$ a Nicaragua. Tenemos que:\n",
    "\n",
    "$$ d^r = (I- A^{rr} - A^{rs}\\cdot(I-A^{ss})^{-1}\\cdot A^{sr})\\cdot p^r$$\n",
    "\n",
    "$$\\Delta p^r = (I- A^{rr} - A^{rs}\\cdot(I-A^{ss})^{-1}\\cdot A^{sr})^{-1}\\cdot\\Delta d^r$$\n",
    "\n",
    "Necesitamos primero calcular $d^r$ para luego poder hacer el calculo apropiado del *shock* que queremos introducir en el sistema con $\\Delta d^{r}$ en Guatemala. Aclaramos que la matriz $(I-A^{ss})^{-1}$ va a figurar como $L^{ss}$ en el código y la vamos a procesar con las funciones previamente utilizadas para el calculo de inversa. La matriz de Leontief del sistema total va a ser $B$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a3edd6d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculo la demanda del primer país (GTM)\n",
    "M_nic_nic = np.eye(40) - A_nic_nic\n",
    "L, U, P = calcularLU(M_nic_nic)\n",
    "L_nic_nic = inversaLU(L, U, P)\n",
    "B = (np.eye(40) - A_gtm_gtm - A_gtm_nic @ L_nic_nic @ A_nic_gtm)  # Matriz resolución\n",
    "D_gtm = P_gtm @ B  # Demanda de guatemala modelo inter regional"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3ebd9da9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Invierto B \n",
    "L, U, P = calcularLU(B)\n",
    "invB = inversaLU(L, U, P)\n",
    "\n",
    "# Creo la delta según lo especificado\n",
    "delta_D_gtm = [0] * 40\n",
    "delta_D_gtm[4] = -D_gtm[4]*.1\n",
    "delta_D_gtm[5] = D_gtm[5]*.033\n",
    "delta_D_gtm[6] = D_gtm[6]*.033\n",
    "delta_D_gtm[7] = D_gtm[7]*.033\n",
    "\n",
    "delta_P_gtm = invB @ delta_D_gtm  # Dif de demanda de guatemala en modelo inter regional"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6cad4349",
   "metadata": {},
   "source": [
    "Bueno, tenemos nuestra diferencia de demanda con *shock* $\\Delta d$ correspondiente a Guatemala según el modelo complejo interregional con correlación a Nicaragua. Faltaría vincular los resultados de este modelo con el modelo simple, es decir, solo considerando la matriz $A^{rr}$ para armar un modelo Insumo Producto. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b4982ccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Consigo la matriz de Leontief del modelo simple\n",
    "L_inv = np.eye(40) - A_gtm_gtm\n",
    "L, U, P = calcularLU(L_inv)\n",
    "L = inversaLU(L, U, P)\n",
    "\n",
    "# Calculo la demanda según el modelo simple\n",
    "D_gtm_simple = L_inv @ P_gtm\n",
    "\n",
    "# Creo el shock\n",
    "delta_D_gtm_simple = [0] * 40\n",
    "delta_D_gtm_simple[4] = -D_gtm_simple[4]*.1\n",
    "delta_D_gtm_simple[5] = D_gtm_simple[5]*.033\n",
    "delta_D_gtm_simple[6] = D_gtm_simple[6]*.033\n",
    "delta_D_gtm_simple[7] = D_gtm_simple[7]*.033\n",
    "\n",
    "# Calculo el delta P\n",
    "delta_P_gtm_simple = L @ delta_D_gtm_simple  # Dif en produccióm modelo simple"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3dc179fb",
   "metadata": {},
   "source": [
    "Ahora tenemos todo lo necesario para poder llevar a cabo una comparación de modelos usando la producción de Guatemala como base.La comparativa ronda en ver como afecta el hecho de que haya información cruzada con Nicaragua en el sistema inter regional contra el sistema simple que solo tiene información de Guatemala. Sabemos que deberán de tener diferentes demandas, ya que las calculamos a través de diferentes matrices, eso si, se mantiene la producción.\n",
    "\n",
    "Para empezar veamos como son diferentes las demandas lado a lado según cada sector."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e16e8704",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Armo un df para comparar demandas y deltas\n",
    "df_analisis = pd.DataFrame({\n",
    "    \"Sectores\": 2*[\"s\" + str(i) for i in range(1, 40 + 1)],\n",
    "    \"Demanda\": np.concatenate([D_gtm, D_gtm_simple]),\n",
    "    \"Delta Demanda\": np.concatenate([delta_D_gtm, delta_D_gtm_simple]),\n",
    "    \"Delta Producción Total\": np.concatenate([delta_P_gtm, delta_P_gtm_simple]),\n",
    "    \"Modelo\": [\"Modelo Inter Regional\"]*40 + [\"Modelo Simple\"]*40\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bf8ad21e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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FZMmTRJ2dnZCV1dXWFlZiVGjRqlMlZeYmCh69uwp7OzshFwuF2ZmZsLLy0ua1YRIEzIhnvm/DRFRKaZPn44ZM2bg7t27L2TsKBERUU3EMdVERERERBpiUk1EREREpCEO/yAiIiIi0hB7qomIiIiINMSkmoiIiIhIQ0yqiYiIiIg0xJe/VBGlUombN2+iVq1aal8/S0RERERVSwiBf//9F9bW1tDSKrkvmkl1Fbl58yZsbGyquhlEREREVIqMjIxS31DKpLqKFL56NiMjA8bGxkX25+XlIS4uDh06dICurm65j69JfcZmbMZmbMZmbMZmbMYGsrKyYGNjI+VtJWFSXUUKh3wYGxsXm1QbGBjA2Ni4wjdIReszNmMzNmMzNmMzNmMz9v8ry1BdPqhIRERERKQhJtVERERERBpiUk1EREREpCEm1UREREREGmJSTURERESkISbVREREREQaYlJNRERERKQhJtVERERERBpiUk1EREREpCEm1UREREREGmJSTURERESkIZ2qbgARERER0Yvm/vkqtdv1tIHJniYaH5891UREREREGmJSTURERESkISbVREREREQa4pjqakDdGJ/KGt9DRERERC8ee6qJiIiIiDTEpJqIiIiISENMqomIiIiINMSkmoiIiIhIQ0yqiYiIiIg0xKSaiIiIiEhDnFKvmrs+zxPayhyVbbZTU6qoNURERESkDnuqiYiIiIg0xKSaiIiIiEhDTKqJiIiIiDTEpJqIiIiISENMqomIiIiINMTZP6ha4qwnNc+r+pm5f75K7XY9bWCyp8lLbg0REVVXTKqJiDTwqv4xQUT0ulH387z2uINlrs/hHxpaunQpHBwcoK+vD3d3d/z5559V3SQiIiIiesnYU62B9evXY9y4cVi6dCnatGmDZcuWoVOnTjh79ixsbW2runlERK8ldUN2CofrVOV/FvhfDaJXG5NqDSxatAjDhg3D8OHDAQARERHYuXMnIiMjMXfu3CpuHdVE/KVLVLOVlNAT0auNSXUF5ebmIjk5GZMnT1bZ3qFDBxw6dKhI+ZycHOTk/H+ylJWV9cLbCDBJq4iafM1qctuJiIhqMibVFXTv3j0UFBTAwsJCZbuFhQUyMzOLlJ87dy5mzJih9ljJCwYV2ZaXl4dt27ahwaRE6OrqFtuO0mYmqEj9svaqlBa7tASvpNianvfrGluTz7si7a6s2KV5kde8tLrqvj8Bzb5HK+uaa3LepanKa65p7Bf5M/VFxtZUVfaSv8h7rTqrrt/fjK2+bkV+npenE5RJtYZkMpnKuhCiyDYACA0NRUhIiLSelZUFGxsbjeOXdoMQ0avrRSdp1dXret5Us5R2n/L3d8WU9IdrVWNSXUHm5ubQ1tYu0it9586dIr3XACCXyyGXy19W86oF/uKrWWryL4Caeq/V1HYTUfWm6c8W/myqGCbVFaSnpwd3d3fs2rULPXv2lLbv2rUL3bt3r8KWEVC1PxD4w6hm4edFRNVRTf3ZVFPbXRmYVGsgJCQEfn5+8PDwgKenJ3744Qekp6dj5MiRVd00IqIX6nX9xfm6njcRlY5JtQb69euHv//+GzNnzsStW7fg4uKCbdu2wc7OrqqbRkREREQvEZNqDQUGBiIwMLCqm0Gvieo8rpmIiF6e6vzAXkle5d9jTKqJiOilqskPxRK9Cvg99mJoVXUDiIiIiIhqOibVREREREQaYlJNRERERKQhjqkmIiIiomqhJk9byZ5qIiIiIiINMakmIiIiItIQk2oiIiIiIg0xqSYiIiIi0hAfVKQqU1PfBkVERET0PPZUExERERFpiEk1EREREZGGOPyDKkzd8A2AQzhIPQ73ISKiVxmTaqKXjMklERHRq4dJNRHRC/S6/hH1up43Eb2+mFQTERERUY1X1a8454OKREREREQaYlJNRERERKQhJtVERERERBpiUk1EREREpCEm1UREREREGmJSTURERESkIU6pR0RERERlxnno1WNPNRERERGRhphUExERERFpiEk1EREREZGGmFQTEREREWmIDyrSa4kPWRAREVFlYk81EREREZGGmFQTEREREWmISTURERERkYY4ppqIqj11Y+CBso+D5xh6IiJ60dhTTURERESkISbVREREREQaeqWSant7e8hkMpVl8uTJKmXS09PRrVs3GBoawtzcHGPGjEFubq5KmZSUFHh5eUGhUKB+/fqYOXMmhBAqZeLj4+Hu7g59fX04OjoiKirqhZ8fEREREVVPr9yY6pkzZyIgIEBaNzIykr4uKChAly5dULduXSQkJODvv//G4MGDIYTAkiVLAABZWVnw8fGBt7c3jh07hgsXLsDf3x+GhoYYP348ACAtLQ2dO3dGQEAAVq9ejYMHDyIwMBB169ZF7969X+4J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28PT0xM9evTAzp07cfXqVRw6dAhffvklkpKSAADTpk3D2rVrMW3aNKSmpiIlJQXz58+XYtjb2+PAgQO4ceMG7t27BwAYP3489uzZg1mzZuHChQtYuXIlvvvuO0yYMKHE9k6aNAmJiYkYPXo0Tp48iYsXL+KPP/7AZ599BgDYsmULFi9ejJMnT+LatWtYtWoVlEolGjdu/IKuIBFROQgiInolZWdni8mTJ4sWLVoIExMTYWBgIBo3biy+/PJL8eTJEyGEEFlZWeKzzz4T1tbWQldXV9jY2IiBAweK9PR06TixsbHCzc1N6OnpCXNzc9GrVy9pX2JionB1dRVyuVw8+yvlf//7n3B2dha6urrC1tZWLFiwQKVtdnZ24ptvvinS5qNHjwofHx9hZGQkDA0NhaurqwgPDxdCCPHnn38KLy8vYWpqKhQKhXB1dRXr16+vzEtGRFRhnP2DiIiIiEhDHP5BRERERKQhJtVERERERBpiUk1EREREpCEm1UREREREGmJSTURERESkISbVREREREQaYlJNRERERKQhJtVERERERBpiUk1EREREpCEm1UREREREGmJSTURERESkISbVREREREQa+j8LedYEAYO7AAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 800x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Ploteo\n",
    "plt.figure(figsize=(8, 4))\n",
    "ax = sns.barplot(\n",
    "    data=df_analisis, x=\"Sectores\", y=\"Demanda\", hue=\"Modelo\"\n",
    "    )\n",
    "ax.set_title(\"Comparativa de demandas entre modelos\")\n",
    "ax.tick_params(axis=\"x\", rotation=90)\n",
    "ax.grid(axis=\"x\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62a4fce1",
   "metadata": {},
   "source": [
    "Vemos que la comparativa es bastante violenta por la diferencia que se genera entre ambas demandas. El modelo inter regional parece ser mucho menos demandante en el sentido de que la gran mayoría de sectores tienen gran diferencia pero en negativo, incluso hay sectores con demanda nula en el modelo simple que en el modelo inter regional pasan a ser grandes demandas negativas. Sumamos también el hecho de que los sectores 3 (minería para energía), 11 (textiles), 18 (productos químicos no fármacos) y 30 (vehículos) son aquellos que parecen englobar los valores más significativos. \n",
    "\n",
    "A partir de lo que vemos en la comparativa de demandas, sabemos que los *shocks* de demanda serán proporcionados a lo visto. Veamos ahora el $\\Delta p$ para poder apreciar como el shock cambio a ambos modelos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9639c038",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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/fXXUCgUJZFjgU2ePBnBwcEYNWoUGjRogDt37iAqKgpmZmZSn8WLF6NHjx7o06cPmjVrBmNjY+zZs0fpUnmbN29GnTp10K5dO7Rr1w6enp7YuHFjaWwSEREREZUyrc8wT5s2DWvWrMH8+fPRrFkzCCFw/PhxhISEIDMzE3Pnzi2JPFU6fPiw0nOZTIaQkBCEhISoHWNkZIRly5Zh2bJlavtUqFABmzZtKqYsiYiIiKg807pgXr9+PX766Sd069ZNaqtbty4qV66MUaNGvdWCmYiIiIiopGk9JePhw4f44IMP8rV/8MEHePjwYbEkRURERERUVmhdMNetWxfLly/P1758+XLUrVu3WJIiIiIiIiorCjwlo2rVqoiNjcWCBQvQuXNnHDx4ED4+PpDJZDhx4gRu3bqFffv2lWSuRERERERvXYHPMF+/fh25ubnw9fXFlStX0LNnTzx+/BgPHz6Ev78/EhMT0bx585LMlYiIiIjordP6S38A4ODgwC/3EREREdF7QauC+fLly0hNTdXYx9PTs0gJERERERGVJVoVzK1bt4YQQu1ymUyG3NzcIidFRERERFRWaFUwnz59GjY2NiWVCxERERFRmaNVwezs7AxbW9uSyoWIiIiIqMzR+jrMRERERETvkwIXzL6+vjAwMCjJXIiIiIiIypwCT8n4448/SjIPIiIiIqIyiVMyiIiIiIg0YMFMRERERKRBoe70R0REREQlw/vzDfnaDHSBqT4WpZANATzDTERERESkkdZnmHNzcxEeHo5Dhw4hLS0NCoVCafnvv/9ebMkREREREZU2rQvmcePGITw8HJ07d4aHhwdkMllJ5EVEREREVCZoXTBv27YNP//8Mzp16lQS+RARERERlSlaz2E2MDCAm5tbSeRCRERERFTmaF0wT5w4Ed9//z2EECWRDxERERFRmaL1lIxjx47hjz/+wP79+1G7dm3o6+srLY+IiCi25IiIiIiISpvWBbOlpSV69uxZErkQEREREZU5WhfM69atK4k8iIiIiIjKpELf6e/+/ftITEyETCZDjRo1YGNjU5x5ERERERGVCVp/6e/Zs2cYMmQIKlWqhBYtWqB58+ZwcHDAp59+iufPn5dEjkREREREpeaNBfOSJUtw6NAh6fmECRMQExODPXv24PHjx3j8+DF+/fVXxMTEYOLEiSWaLBERERHR2/bG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",
      "text/plain": [
       "<Figure size 800x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Ploteo\n",
    "plt.figure(figsize=(8, 4))\n",
    "ax = sns.barplot(\n",
    "    data=df_analisis, x=\"Sectores\", y=\"Delta Producción Total\", hue=\"Modelo\"\n",
    "    )\n",
    "ax.set_title(\"Comparativa de $\\t{Shock}$ de Producción entre modelos\")\n",
    "ax.tick_params(axis=\"x\", rotation=90)\n",
    "ax.grid(axis=\"x\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33d62ee6",
   "metadata": {},
   "source": [
    "Se observa que el $\\Delta P$ del modelo inter regional supone un aumento considerable en sectores. Vemos que los sectores más afectados son el 4, 21, 35 y 39, con un delta positivo. Un detalle no menor a destacar es que hay correspondencia en ambos modelos al signo de la producción pero no a la magnitud, aunque con excepciones como el sector 14 y el 40. Podemos concluir de cierto modo que ambos sistemas llevan tienen un comportamiento subyacente similar pero manejan magnitudes sumamente diferentes en cuanto a sus demandas y producciones, siendo la del modelo inter regional una mucho mayor. Esto se puede deber una posible similitud entre Guatemala y Nicaragua y que, además, estamos asumiendo que la demanda de Nicaragua es nula y consecuentemente se produzca una retroalimentación entre sectores de estos países que logren una demanda de tal magnitud en negativo. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
