import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('Insert file name')
df.plot()

"""
ETS: (Error, Trend, Seasonality)
Grab all Day open prices and all Day close prices and break
them down ( decompose ) into five values of evaultion listed

The more valuable results are:
    1. Trend (Overall:: Up, Down or Consolidating)
    2. Seasonality (shorter time frames & *technical patterns)

We can also evaluate other values such as *seasonal_fundamentals, valuation ratios, etc.
and decompose them into this segmentation of the chart into different categories for
observation.
This can show possible repeating patterns which is the most important 
evaluation of ETS.
The trend is a secondary evaluation as long as there is a repeatable 
pattern in a strategy we can take trades on either an up trend, down trend, or sideways trend. 
"""

ets_open_result = seasonal_decompose(df['Open'], model='multiplicative')
ets_close_result = seasonal_decompose(df['Close'], model='multiplicative')

# Singular seasonal decompose value plots
result.seasonal.plot()
result.trend.plot()
result.observed.plot()
result.resid.plot()
result.nobs.plot()

# Plot All ETS values
ets_result.plot()

#  Calculate Count, Mean, Std, Min, 25%, 50%, 75%, Max
df.describe().transpose()
