Markdown# 🛢️ Plataforma de Analítica para Oil & Gas

## 📖 Descripción General
Esta aplicación web interactiva está diseñada para ejecutar cálculos críticos de ingeniería petrolera de forma ágil y visual. Desarrollada como parte del **Bootcamp Data Analytics for Oil & Gas**, la plataforma ofrece una interfaz profesional inspirada en sistemas de control operativo (Dark Theme / SCADA) para facilitar la toma de decisiones basada en datos.

## ⚙️ Módulos Principales
La aplicación se divide en tres áreas técnicas fundamentales, organizadas mediante un menú de navegación intuitivo:

1. **📈 Producción (Análisis IPR):** Calcula y grafica el desempeño de afluencia (IPR) para yacimientos subsaturados. El motor matemático identifica automáticamente si el flujo es lineal o se rige por el modelo no lineal de Vogel (cuando la presión cae por debajo del punto de burbuja).
2. **🎯 Perforación (Presión Hidrostática):** Genera un perfil vertical de presiones y evalúa la condición operativa del pozo en tiempo real. Mediante alertas visuales de colores, indica si la operación se encuentra en Sobrebalance, Balance aproximado o Bajo balance (riesgo de *Kick*).
3. **🛢️ Reservorios (Estimación Volumétrica):** Calcula el Petróleo Original en Sitio (POES) y las reservas recuperables utilizando el método volumétrico. Presenta comparativas visuales dinámicas de alto contraste en unidades operativas (STB y MMSTB).

## 🏗️ Arquitectura Modular del Proyecto
El código está estructurado bajo principios de ingeniería de software (separación de responsabilidades), garantizando un mantenimiento sencillo y un ciclo de ejecución eficiente en Streamlit:

* `app.py`: Archivo principal y orquestador de la aplicación. Enlaza todos los submódulos.
* `interfaz.py`: Capa de presentación (Frontend). Encapsula todo el diseño HTML, reglas CSS, animaciones interactivas en JavaScript y los gráficos dinámicos construidos con Plotly.
* `calculos.py`: Motor matemático de ingeniería. 
* `validaciones.py`: Reglas de negocio que evitan cálculos físicamente inconsistentes (ej. profundidades negativas o divisiones por cero).
* `modelos.py`: Clases de datos (`dataclasses`) para organizar y transferir la información de manera limpia entre la interfaz y el motor de cálculo.
* `datos.py`: Módulo preparado para la lectura y preparación de datos crudos.
* `__init__.py`: Inicializador del paquete.

⚠️ Consideraciones Importantes de Uso

Unidades de Medida: Presta atención a las unidades indicadas entre corchetes [...] en cada caja de texto (ej. Presión en psi, Caudal en STB/d).Fracciones vs Porcentajes: En el módulo de Reservorios, las propiedades petrofísicas como la Porosidad, Saturación Inicial de Agua ($Swi$), relación Net-to-Gross ($NTG$) y el Factor de Recobro ($FR$) deben ingresarse obligatoriamente como fracciones (valores entre 0 y 1), no como porcentajes enteros.

Interactividad Visual: Los gráficos son dinámicos. Pasa el cursor (hover) sobre las curvas, puntos operativos y barras para inspeccionar las métricas exactas calculadas.

Desarrollador: JOSE GONZALO OCHOA PAZ
Programa: Bootcamp Data Analytics for Oil & Gas - SPE Ecuador Section
