# 模板去重规则

## 核心原则
**同一模板结构 + 不同字段 = 重复**

## 模板抽象规则

### 单算子模板
| 具体表达式 | 抽象模板 |
|-----------|---------|
| `rank(assets)` | `rank(<f/>)` |
| `rank(close)` | `rank(<f/>)` |
| `ts_rank(volume, 22)` | `ts_rank(<f/>, d)` |
| `ts_delta(close, 5)` | `ts_delta(<f/>, d)` |

### 嵌套模板
| 具体表达式 | 抽象模板 |
|-----------|---------|
| `group_rank(ts_rank(eps, 252), industry)` | `group_rank(ts_rank(<f/>, d), <g/>)` |
| `group_rank(ts_rank(sales, 126), sector)` | `group_rank(ts_rank(<f/>, d), <g/>)` |

### 组合模板
| 具体表达式 | 抽象模板 |
|-----------|---------|
| `rank(a) * rank(b)` | `rank(<f1/>) * rank(<f2/>)` |
| `ts_rank(x, d1) - ts_rank(x, d2)` | `ts_rank(<f/>, d1) - ts_rank(<f/>, d2)` |

## 允许的变化
1. **改变算子**: `rank()` → `group_rank()` ✓
2. **增加嵌套**: `rank(x)` → `rank(ts_zscore(x, d))` ✓
3. **组合思想**: A思想 + B思想 = 新结构 ✓
4. **改变逻辑**: 加入条件 `trade_when()` ✓

## 禁止的变化
1. **换字段**: `rank(assets)` → `rank(price)` ✗
2. **换参数**: `ts_rank(x, 22)` → `ts_rank(x, 66)` ✗（同模板）
3. **换分组**: `group_rank(x, industry)` → `group_rank(x, sector)` ✗

---

## 禁止使用的模板结构

### 1. 比率回填+中性化
```
group_neutralize(rank(ts_backfill(X,d)/ts_backfill(Y,d)), group)
```

### 2. rank比率+ts_rank+中性化
```
group_neutralize(ts_rank(rank(X)/rank(Y),d), group)
```

### 3. 负相关性排名
```
-rank(ts_corr(X, Y, d))
```

### 4. 回填比率+ts_rank
```
ts_rank(ts_backfill(X,d)/Y, d)
```

### 5. ts_delta+group_rank
```
group_rank(ts_delta(X, d), group)
```
