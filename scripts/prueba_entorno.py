from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import cfd_aprendizaje

salida = Path("resultados")
salida.mkdir(exist_ok=True)

x = np.linspace(0, 2 * np.pi, 200)
plt.plot(x, np.sin(x))
plt.savefig(salida / "prueba.png")

print("numpy", np.__version__)
cfd_aprendizaje.main()
