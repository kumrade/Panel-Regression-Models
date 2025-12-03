# ===============================================================
# PANEL REGRESSION MODELS FOR INDIAN STOCKS
# ---------------------------------------------------------------
# Models implemented:
# 1. Individual AR(1) regressions (α_i, β_i for each stock)
# 2. Pooled OLS (Common α, β)
# 3. Fixed Effects Panel Regression (Different intercepts, common β)
# ===============================================================

from jugaad_data.nse import stock_df
from datetime import date
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# ----------------------------------------------
# 1. Download DATA from JUGAAD for Indian Stocks
# ----------------------------------------------
stocks = ["HDFCBANK", "INFY", "TCS", "RELIANCE", "ITC"]
start = date(2020, 1, 1)
end   = date(2023, 12, 31)

panel_data = []

for symbol in stocks:
    print("Downloading:", symbol)
    df = stock_df(symbol, from_date=start, to_date=end)
    df["Symbol"] = symbol
    df["Return"] = df["CLOSE"].pct_change()
    panel_data.append(df)

df = pd.concat(panel_data)
df = df.dropna().reset_index(drop=True)

# lag return → r_i,t
df["Return_lag"] = df.groupby("Symbol")["Return"].shift(1)
df = df.dropna()

# ------------------------------------------------------
# 2. INDIVIDUAL AR(1) REGRESSIONS: 
#    r_{i,t+1} = α_i + β_i * r_{i,t}
# ------------------------------------------------------
print("\n=================== INDIVIDUAL AR(1) RESULTS ===================")
individual_results = {}

for s in stocks:
    temp = df[df["Symbol"] == s]
    model = smf.ols("Return ~ Return_lag", data=temp).fit()
    individual_results[s] = model
    print(f"\n{s}")
    print(model.summary())

# ------------------------------------------------------
# 3. POOLED OLS REGRESSION:
#    r_{i,t+1} = α + β * r_{i,t}
# ------------------------------------------------------
print("\n=================== POOLED OLS (COMMON α, β) ===================")
pooled_model = smf.ols("Return ~ Return_lag", data=df).fit()
print(pooled_model.summary())

# ------------------------------------------------------
# 4. FIXED EFFECTS MODEL:
#    r_{i,t+1} = δ_i + β * r_{i,t}
# ------------------------------------------------------
print("\n=================== FIXED EFFECTS REGRESSION ===================")
# Equivalent to including Symbol dummy variables
fixed_effects_model = smf.ols("Return ~ Return_lag + C(Symbol)", data=df).fit()
print(fixed_effects_model.summary())

# ======================================================
# 5. PLOTS: VISUALIZING DIFFERENCES BETWEEN STOCKS
# ======================================================

plt.figure(figsize=(10, 6))
for symbol in stocks:
    temp = df[df["Symbol"] == symbol]
    plt.scatter(temp["Return_lag"], temp["Return"], alpha=0.3, label=symbol)

plt.title("AR(1) Return Relationship for Different Indian Stocks")
plt.xlabel("Lagged Return r(t)")
plt.ylabel("Next Return r(t+1)")
plt.legend()
plt.show()

# Plot individual regression lines to show different intercepts
plt.figure(figsize=(10, 6))

x_vals = np.linspace(df["Return_lag"].min(), df["Return_lag"].max(), 100)

for symbol in stocks:
    model = individual_results[symbol]
    α = model.params["Intercept"]
    β = model.params["Return_lag"]
    plt.plot(x_vals, α + β * x_vals, label=symbol)

plt.title("AR(1) Regression Lines: Different Intercepts (α_i)")
plt.xlabel("Lagged Return r(t)")
plt.ylabel("Predicted Return r(t+1)")
plt.legend()
plt.show()
