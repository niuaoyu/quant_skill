# User阶段禁止使用项

> 当用户说"度过user阶段"后，此文件可清空

## 禁止字段

### 基本面字段
- net_income
- market_cap
- free_cash_flow
- gross_profit
- operating_cash_flow
- current_assets
- current_liabilities
- book_value
- roe

### 交易相关
- short_interest
- shares_outstanding

### 分析师字段 (anl4_*)
- anl4_sell
- anl4_rev_down
- anl4_rev_up
- anl4_eps_mean
- anl4_capex_median
- anl4_ffo_value
- anl4_epsr_median
- anl4_ebitda_median
- anl4_afv4_eps_median
- anl4_basicconqfv110_value
- anl4_adxqfv110_value
- anl4_ady_value
- anl4_epsa_mean
- anl4_netdebt_value
- anl4_rd_exp_value
- anl4_tbvps_value
- anl4_fcfps_value
- anl4_totgw_value
- anl4_afv4_sales_mean

### 预估字段
- est_net_income
- est_target_price

### 基本面数据 (fnd6_*)
- fnd6_newa1v1300_txt
- fnd6_newa2v1300_gdwl
- fnd6_newa2v1300_intan
- fnd6_newa2v1300_gp
- fnd6_newa2v1300_emp
- fnd6_newa2v1300_dv
- fnd6_newa2v1300_dltt
- fnd6_newa2v1300_lct
- fnd6_newa1v1300_sale
- fnd6_newa1v1300_ni

### 新闻/情绪字段
- news_sentiment
- nws12_prez_sentiment

---

## 禁止操作符

### 时序操作符
- ts_max
- ts_min
- ts_decay_exp_window
- ts_skewness
- ts_stddev
- ts_argmax
- ts_argmin
- ts_ir
- ts_kurtosis
- ts_partial_corr
- ts_triple_corr
- ts_moment
- ts_prod

### 向量操作符
- vec_min
- vec_max
- vec_mean
- vec_count

### 其他操作符
- sigmoid
- negate
- regression_neut

---

## 数据限制

### 不存在的数据格式
- 不支持 `1e-6` 等科学计数法
- 不支持 `nan` 作为值

### 字段名称注意
- 相关性用 `ts_corr`（不是correlation）

### historical_volatility 只有以下窗口
- historical_volatility_10
- historical_volatility_20
- historical_volatility_30
- historical_volatility_60
- historical_volatility_90
- historical_volatility_120
- historical_volatility_150
- historical_volatility_180
- **禁止**: historical_volatility_210 及以上

### adv 只有
- adv20
- **禁止**: adv5, adv10, adv40 等
