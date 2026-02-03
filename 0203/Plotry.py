#plotry 범례 지정하기
"""
import plotly.express as px
#express는 범럐가 자동으로 생성된다.
df = px.data.tips()


print(df.head())"""

"""
import plotly.express as px

df = px.data.tips()


fig = px.scatter(df,x =  )"""


"""
import plotly.io as pio

print(pio.templates)
"""

"""
import pandas as pd
import numpy as np

pd.options.plotting.backend
"""
import plotly.express as px

df = px.data.gapminder()
df_2007=df.query("year = 2007")

for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig = px.scatter(df_2007, x ="gdpPercap", y="lifeExp", size="pop", color="continent",
        log_x=True, size_max=60,
        template=template, title="Gapminder 2007: '%s' theme" % template)
    fig. show()