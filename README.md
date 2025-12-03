# Panel-Regression-Models
This code performs panel regression analysis on Indian stocks to study whether past returns predict future returns. It downloads data, computes returns, runs individual AR(1) regressions, pooled OLS, and fixed-effects models, then visualizes differences in intercepts and return dynamics across stocks using scatter plots and regression lines.
AR(1), Pooled OLS, and Fixed-Effects Analysis

This project performs a comprehensive panel regression study on major Indian stocks to examine whether lagged returns predict future returns. Using AR(1) models, pooled OLS, and fixed-effects regression, the analysis highlights differences in stock-specific return dynamics.

🚀 Features
1. Data Collection

Downloads historical price data for:
HDFCBANK, INFY, TCS, RELIANCE, ITC

Computes daily returns and lagged returns.

2. Individual AR(1) Models

Runs separate regressions for each stock:

𝑟
𝑖
,
𝑡
+
1
=
𝛼
𝑖
+
𝛽
𝑖
𝑟
𝑖
,
𝑡
r
i,t+1
	​

=α
i
	​

+β
i
	​

r
i,t
	​


Provides stock-level insight into momentum or mean reversion.

3. Pooled OLS Regression

Assumes a common intercept and slope for all stocks to test uniform behavior.

4. Fixed Effects Model

Allows different intercepts (αᵢ) across stocks while keeping a common β:

𝑟
𝑖
,
𝑡
+
1
=
𝛿
𝑖
+
𝛽
𝑟
𝑖
,
𝑡
r
i,t+1
	​

=δ
i
	​

+βr
i,t
	​

5. Visualizations

Scatter plots of lagged vs future returns

Regression lines showing differences across stocks
