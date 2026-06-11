# Modelo Epidemiológico SIR — Simulación en Python
 
Proyecto final de la asignatura **Programación 1** (IMAT 1º curso).  
Implementación del modelo matemático SIR para simular la propagación de enfermedades infecciosas en una población, con y sin dinámica vital (natalidad, mortalidad y vacunación).
 
---
 
## Descripción
 
El modelo SIR divide la población en tres compartimentos:
 
- **S** — Susceptibles: personas que pueden infectarse
- **I** — Infectados: personas con la enfermedad activa
- **R** — Recuperados: personas inmunes tras superar la infección
El programa resuelve numéricamente las ecuaciones diferenciales del modelo y genera gráficas de evolución temporal de los tres grupos. Se implementan dos variantes: una sin dinámica vital y otra que incorpora tasas de natalidad, mortalidad y vacunación.
 
---
 
## Estructura del proyecto
 
```
epidemia-SIR/
├── funciones_epidemia.py   # Modelos SIR: ecuaciones y resolución numérica
├── main_no_tasa.py         # Simulación sin dinámica vital
├── main_tasa_vital.py      # Simulación con dinámica vital
└── README.md
```
 
| Archivo | Descripción |
|---|---|
| `funciones_epidemia.py` | Define las EDOs del modelo SIR y las resuelve con `odeint` |
| `main_no_tasa.py` | Ejecuta el modelo básico y muestra la gráfica |
| `main_tasa_vital.py` | Ejecuta el modelo extendido con natalidad, mortalidad y vacunación |
 
---
 
## Cómo ejecutar
 
**Requisitos:** Python 3.x
 
```bash
pip install numpy scipy matplotlib
```
 
**Modelo sin dinámica vital:**
```bash
python main_no_tasa.py
```
 
**Modelo con dinámica vital:**
```bash
python main_tasa_vital.py
```
 
---
 
## Parámetros del modelo
 
### Modelo básico (`main_no_tasa.py`)
 
| Parámetro | Valor ejemplo | Descripción |
|---|---|---|
| `S0` | 0.99 | Fracción inicial de susceptibles |
| `I0` | 0.01 | Fracción inicial de infectados |
| `R0` | 0.00 | Fracción inicial de recuperados |
| `trasm` | 0.08 | Tasa de transmisión |
| `recup` | 0.025 | Tasa de recuperación |
| `T` | 300 | Días de simulación |
 
### Modelo con dinámica vital (`main_tasa_vital.py`)
 
Incluye los parámetros anteriores más:
 
| Parámetro | Valor ejemplo | Descripción |
|---|---|---|
| `nym` | 0.006 | Tasa de natalidad/mortalidad |
| `vac` | 0.010 | Tasa de vacunación |
 
---
 
## Ecuaciones del modelo
 
**Modelo básico:**
 
```
dS/dt = -β·S·I  
dI/dt =  β·S·I - γ·I  
dR/dt =  γ·I
```
 
**Modelo con dinámica vital:**
 
```
dS/dt = -β·S·I - (v + μ)·S  
dI/dt =  β·S·I - γ·I - μ·I  
dR/dt =  γ·I - μ·R + v·S
```
 
Donde `β` es la tasa de transmisión, `γ` la de recuperación, `μ` la de natalidad/mortalidad y `v` la de vacunación.
 
---
 
## Resultados
 
**Sin dinámica vital:** toda la población acaba recuperándose. Se observa un pico de infecciones claro antes de que la curva de infectados descienda a cero.
 
**Con dinámica vital:** al incorporar mortalidad, las posibilidades de recuperación disminuyen con el tiempo. La población susceptible no se agota completamente ya que la natalidad introduce nuevos individuos susceptibles de forma continua.
 
---
 
## Tecnologías
 
- Python 3
- `numpy` — discretización temporal
- `scipy.integrate.odeint` — resolución numérica de EDOs
- `matplotlib` — visualización de resultados
---
 
## Autores
 
- **Guzmán Pérez**
- **Jaime Pedrosa**
Proyecto entregado en el 1er curso del Grado en Ingeniería Matemática e Inteligencia Artificial (IMAT) — Comillas ICAI.
