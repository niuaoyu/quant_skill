# BRAIN算子分类

## 时序操作符 `<ts_op/>`
| 算子 | 用途 | 示例 |
|------|------|------|
| `ts_mean` | 移动平均 | `ts_mean(close, 22)` |
| `ts_rank` | 时序排名(0-1) | `ts_rank(volume, 66)` |
| `ts_delta` | 差分 | `ts_delta(close, 5)` |
| `ts_std_dev` | 移动标准差 | `ts_std_dev(returns, 22)` |
| `ts_ir` | 信息比率 | `ts_ir(returns, 126)` |
| `ts_zscore` | 时序Z-score | `ts_zscore(eps, 252)` |
| `ts_corr` | 滚动相关性 | `ts_corr(returns, volume, 66)` |
| `ts_regression` | 滚动回归 | `ts_regression(y, x, 252)` |
| `ts_decay_linear` | 线性衰减 | `ts_decay_linear(signal, 10)` |
| `ts_decay_exp_window` | 指数衰减 | `ts_decay_exp_window(x, 22, 0.9)` |
| `ts_backfill` | 数据回填 | `ts_backfill(eps, 120)` |
| `ts_sum` | 滚动求和 | `ts_sum(volume, 22)` |
| `ts_delay` | 延迟 | `ts_delay(close, 1)` |

## 分组操作符 `<group_op/>`
| 算子 | 用途 | 示例 |
|------|------|------|
| `group_rank` | 分组排名 | `group_rank(roe, industry)` |
| `group_neutralize` | 分组中性化 | `group_neutralize(alpha, sector)` |
| `group_zscore` | 分组Z-score | `group_zscore(eps, industry)` |
| `group_mean` | 分组均值 | `group_mean(returns, 1, market)` |

## 向量操作符 `<vec_op/>`
| 算子 | 用途 | 示例 |
|------|------|------|
| `vec_avg` | 向量平均 | `vec_avg(anl4_eps_mean)` |
| `vec_sum` | 向量求和 | `vec_sum(analyst_estimate)` |
| `vec_max` | 向量最大 | `vec_max(anl4_eps_high)` |
| `vec_stddev` | 向量标准差 | `vec_stddev(sentiment_vec)` |

## 信号处理
| 算子 | 用途 |
|------|------|
| `winsorize` | 极端值截断 |
| `sigmoid` | Sigmoid归一化 |
| `signed_power` | 带符号幂变换 |
| `rank` | 截面排名 |
| `zscore` | 截面Z-score |

## 条件操作
| 算子 | 用途 |
|------|------|
| `if_else` | 条件判断 |
| `trade_when` | 条件交易 |
| `regression_neut` | 回归中性化 |
