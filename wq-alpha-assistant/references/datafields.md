# BRAIN数据字段分类

## 量价类 `<pv_field/>`
```
close, open, high, low, vwap
returns, volume, adv20, sharesout, cap
```

## 基本面类 `<fundamental_field/>`
```
assets, sales, ebitda, net_income, eps
operating_income, debt, cash, equity
roe, roa, debt_to_equity
fnd6_*, fnd72_*, mdl175_*
```

## 分析师类 `<analyst_field/>` (VECTOR)
```
anl4_eps_mean, anl4_eps_low, anl4_eps_high
anl4_revenue_mean, anl4_fcf_value
anl14_mean_eps_*, anl15_*
```

## 情绪类 `<sentiment_field/>`
```
scl12_sentiment, scl12_buzz
nws18_relevance, nws18_ber
mws85_sentiment
```

## 期权类 `<option_field/>`
```
implied_volatility_call_*, implied_volatility_put_*
pcr_vol_*, pcr_oi_*
put_delta, call_delta, put_gamma, call_gamma
```

## 分组字段 `<group/>`
```
industry, sector, subindustry
market, country, exchange
```

## 标准时间窗口
| 代号 | 天数 | 含义 |
|------|------|------|
| 短期 | 3-22 | 反转因子 |
| 中期 | 22-66 | 动量因子 |
| 长期 | 126-252 | 趋势因子 |
| 超长 | 252-504 | 回归/波动 |
