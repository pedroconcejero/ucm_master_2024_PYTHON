# master UCM visualizacion avanzada
# Tema 9 shiny - Ejemplo 1: Datos 4500 vehículos UK 2016
# ui
# Basado en parte en el ejemplo de Joe Cheng
# https://gist.github.com/jcheng5/3239667

import pandas as pd
from shiny import *
from plotnine import *
import sklearn
import skmisc

df = pd.read_csv("vehiculos_UK_2016.csv", sep = "|")
continuas = df.select_dtypes(include=['int', 'float']).columns.tolist()

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select('eje_x',
            'Elige variable para eje X', 
            continuas,
            selected = continuas[0]),
            ui.input_select('eje_y',
            'Elige variable para eje Y', 
            continuas,
            selected = continuas[1]),
        ),
        ui.card(
            ui.output_plot("plot"),
        ),
    ),
    )

def server(input, output, session):
    @output
    @render.plot(alt = "Gráfico Bivariante")
    def plot():
      p = ggplot(df, aes(x = str(input.eje_x()), 
                         y = str(input.eje_y()),
                         fill = "Tipo")) + geom_point() + geom_smooth(method = 'lowess') 
      return p

app = App(app_ui, server)

