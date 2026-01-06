# Alpha优化指南

## 核心指标公式

| 指标 | 公式 | 说明 |
|------|------|------|
| **Sharpe (IR)** | `Return / std_dev(Return)` | 风险调整后收益 |
| **Fitness** | `Sharpe * sqrt(abs(Returns) / max(Turnover, 0.125))` | 综合评分 |
| **Turnover** | `Dollar_trading_volume / Booksize` | 换手率，建议<40% |

---

## 1. 如何提高Sharpe

### 核心思路
- **提高收益**: 更好的预测 = 更多信息
- **降低波动**: 中性化消除市场/行业暴露

### 具体方法
1. **中性化设置**: Market → Subindustry
2. **分组算子**: `group_neutralize`, `group_rank`, `group_zscore`
3. **回归中性化**: `regression_neut`, `vector_neut`
4. **Slow/Fast factors**: 尝试不同的中性化因子

### 注意事项
- 不要为了提高Sharpe而盲目调参，表达式需有经济逻辑
- 达到最低Sharpe阈值后，应更关注Returns

---

## 2. 如何提高Returns

### 具体方法
1. **提高Turnover**: 更多交易 = 潜在更高收益
2. **降低Decay**: 使用更低的decay值
3. **更小Universe**: 流动性更好的小宇宙（如TOP500）
4. **提高波动率**: 在保持drawdown不变的情况下
5. **使用高频数据**: News、Analyst数据集可能产生高收益Alpha

---

## 3. 如何优化Turnover

### 降低Turnover（建议<40%，必须<70%）
1. **Decay设置**: N天decay会平均N天的Alpha值
2. **Rank函数**: 对Alpha使用`rank()`
3. **trade_when**: 条件交易，减少不必要交易
4. **hump算子**: 设置阈值，只在变化超过阈值时交易

### 提高Turnover
1. 降低Decay值
2. 使用更小Universe
3. 使用更短时间窗口（如20天代替200天）
4. 使用高频更新数据（News、Sentiment）

---

## 4. 如何降低Correlation

### 方法
1. **换字段**: 用`high/low/open`替代`close`
2. **换算子**: `median`替代`mean`，`zscore`替代`rank`
3. **换分组**: 不同的neutralization和grouping
4. **创新思维**: 跳出框架，真正的研究

---

## 5. 如何平滑PnL曲线

### 波动原因及解决
| 原因 | 解决方案 |
|------|----------|
| NaN频繁切换 | `ts_backfill()`, `group_backfill()` |
| Alpha值剧烈变化 | `decay`设置，或在公式中取平均 |
| 单股权重过高 | 设置Truncation（建议<0.1） |
| 特定年份表现差 | 中性化消除行业风险 |

### 年度表现下滑原因
- 随机噪声或过拟合
- Alpha被过度使用
- 重大事件（如COVID-19）

---

## 6. 如何提高Fitness

### 公式分解
```
Fitness = Sharpe * sqrt(abs(Returns) / max(Turnover, 0.125))
```

### 优化方向
- **提高Sharpe**: 见第1节
- **提高Returns**: 见第2节
- **降低Turnover**: 见第3节

---

## 7. trade_when用法

### 语法
```
trade_when(Event_condition, Alpha_expression, hold_value)
```
- `hold_value = -1`: 保持上一个Alpha值
- `hold_value = 0`: 不交易

### 优点
- 良好的Alpha覆盖率
- 灵活定义事件
- 低换手率、低成本

### 缺点
- 不易获得高Sharpe
- 不易获得高Return

### 事件定义
- 收益率突变
- 数据值异常
- 技术指标信号

---

## 8. 提高Alpha容量

### 三大要素
1. **高流动性**
2. **低相关性**
3. **低换手率**（最重要）

### hump操作
- 设置阈值，只在Alpha变化超过阈值时交易
- 阈值可根据市场条件动态调整
- 可按行业/市值/波动率分组设置不同阈值

### 进阶思路
- 监控短期波动率
- 波动率突破阈值时才交易
- 其他时间保持持仓或使用更严格的hump阈值

---

## 9. Decay设置

### 原理
Decay是N天的线性衰减函数：
```
day_t_value = weighted_average(day_t to day_t-n)
```

### 效果
- 平滑Alpha值
- 降低Turnover
- 可能改变整体表现

### 默认值
- 默认decay=4

---

## 10. 优化决策树

```
Alpha表现评估
│
├─ Sharpe < 1.5 → 重新设计表达式
│
├─ Sharpe 1.5-2.5 →
│   ├─ 尝试中性化（sector/industry/subindustry）
│   ├─ 调整时间窗口参数
│   └─ 组合波动率/流动性因子
│
├─ Sharpe > 2.5 但 Turnover > 40% →
│   ├─ 增加Decay
│   ├─ 使用trade_when
│   └─ 使用hump算子
│
├─ Sharpe > 2.5 但 Returns低 →
│   ├─ 降低Decay
│   ├─ 使用更小Universe
│   └─ 尝试News/Analyst数据
│
└─ Sharpe > 2.5, Turnover < 40%, Returns好 →
    └─ 检查Correlation，尝试变体
```
