# Alpha模板模式库

## 核心模式

### 1. 时序动量
```
ts_rank(<field/>, <d/>)
ts_mean(returns, <d_short/>) - ts_mean(returns, <d_long/>)
```
**逻辑**: 捕捉趋势延续

### 2. 均值回归
```
-ts_delta(close, <d/>)
-(close - ts_mean(close, <d/>))/ts_mean(close, <d/>)
```
**逻辑**: 价格偏离后回归

### 3. 基本面价值
```
group_rank(<book_value/>/<market_cap/>, <group/>)
ts_rank(net_income/assets, 252)
```
**逻辑**: 低估值股票溢价

### 4. 分析师预期
```
vec_avg(anl4_eps_mean) - ts_delay(vec_avg(anl4_eps_mean), 22)
group_zscore(actual - estimate, industry)
```
**逻辑**: 预期修正驱动

### 5. 情绪因子
```
-scl12_buzz  # 高关注度反转
ts_decay_exp_window(vec_avg(sentiment), 10, 0.9)
```
**逻辑**: 情绪极端后反转

## 标准处理流程
```
数据清洗: ts_backfill → winsorize
时序转换: ts_rank/ts_zscore/ts_delta
截面比较: group_rank/group_zscore
中性化: group_neutralize(alpha, industry)
换手控制: ts_decay_linear/hump
```

## 常用组合模板
```
# 三阶嵌套
group_rank(ts_rank(ts_zscore(<field/>, <d1/>), <d2/>), <group/>)

# 双重中性化
a1 = group_neutralize(alpha, industry);
group_neutralize(a1, bucket(rank(cap), range="0.1,1,0.1"))

# 条件交易
trade_when(volume > adv20, <alpha/>, -1)
```
