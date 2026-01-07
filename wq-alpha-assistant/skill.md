# WorldQuant Alpha表达式助手

## 触发条件
**关键词**: 表达式、alpha、α、worldquant、quant

当用户请求以下任务时触发：
- 生成Alpha表达式
- 学习成功表达式
- 查询可用字段
- 解释表达式逻辑
- **优化现有Alpha**（提高Sharpe/Returns/Fitness等）

---

## 核心规则（必须遵守）

### 规则1: 字段来源
- **默认只读取**: `references/fields_simple/TOP3000/` 下的精简版字段文件（仅字段名）
- 其他Universe（TOP1000/TOP500等）除非用户明确指定，否则不读取
- **字段描述查询**: 若字段名含义不明，用Grep在`references/data_fields_txt/TOP3000/`中搜索该字段名，获取完整描述（第2列）

### 规则2: 输出规范（强制）
- **分号结尾**: 每个表达式必须以`;`分号结尾
- **直接输出**: 表达式直接在终端输出，**不写入任何文件**
- **不查clean_alpha**: 生成时**不查询**`clean_alpha/`里的具体表达式

### 规则3: 模板去重（核心）
**查询文件**: `references/template_dedup_rules.md` 和 `references/template_patterns.md`
**禁止同一模板换字段！** 以下视为同一模板：
- `rank(assets)` 和 `rank(price)` → 同属 `rank(<field/>)` 模板
- `ts_rank(close, 22)` 和 `ts_rank(volume, 22)` → 同属 `ts_rank(<field/>, d)` 模板

**允许的做法**:
- 组合多个好表达式的思想
- 改变算子结构（如 `rank()` → `group_rank()` + `ts_zscore()`）
- 增加嵌套层级或条件逻辑

### 规则4: 学习思想而非模板
当用户提供成功表达式时：
1. 提取**经济逻辑思想**（如"动量+均值回归组合"）
2. 记录**结构模式**（标记为已使用，后续禁止同模板换字段）
3. 后续生成时：可组合多个思想，但禁止复制模板结构

### 规则5: 禁止项检查（User阶段）
**生成前必须检查** `references/forbidden_items.md`：
- 禁止字段（如net_income, market_cap等）
- 禁止操作符（如ts_max, ts_min, regression_neut等）
- 禁止模板结构（见`references/template_dedup_rules.md`）
- 数据限制（adv只有20，historical_volatility窗口限制等）

**用户反馈禁止项时**：立即追加到`forbidden_items.md`

### 规则6: 复杂度要求（强制）
**禁止生成过于简单的表达式**：
- ❌ 单个datafield: `close`, `volume`, `returns`
- ❌ 单层operator+单字段: `rank(close)`, `ts_rank(volume, 20)`, `group_rank(returns, industry)`
- ❌ 简单算术: `close/volume`, `high - low`

**最低复杂度标准**（至少满足一项）：
- ✅ 2层以上嵌套: `rank(ts_delta(close, 5))`, `group_rank(ts_zscore(volume, 20), industry)`
- ✅ 多字段组合运算: `ts_corr(close, volume, 20)`, `(close - open) / (high - low)`
- ✅ 条件逻辑: `trade_when(condition, signal, fallback)`, `if_else(cond, a, b)`
- ✅ 复合信号: `rank(field1) * rank(field2)`, `ts_rank(a, d) - ts_rank(b, d)`

**复杂度检测规则**：
```
简单模式（禁止）:
- ^[a-z_]+$                           # 单字段
- ^(rank|zscore)\([a-z_]+\)$          # rank/zscore单字段
- ^ts_\w+\([a-z_]+,\s*\d+\)$          # ts_op单字段
- ^group_\w+\([a-z_]+,\s*\w+\)$       # group_op单字段
```

---

## 工作流程

### 生成Alpha表达式
1. **读取字段**: 从 `references/fields_simple/TOP3000/` 获取可用字段
2. **禁止项检查**: 读取 `references/forbidden_items.md`，排除禁止字段/操作符
3. **模板去重**: 查询 `references/template_dedup_rules.md`，避免使用已有模板结构
4. **生成表达式**: 基于金融逻辑，确保不使用禁止项和重复模板
5. **直接输出**: 在终端输出，每行一个表达式，以`;`结尾

### 学习成功表达式
1. **解析结构**: 识别算子嵌套、字段、参数
2. **提取思想**: 记录经济逻辑（非模板本身）
3. **标记模板**: 将该模板结构标记为"已使用"，后续禁止同结构换字段
4. **更新知识库**: 追加到 `references/learned_patterns.md`
5. **确认学习**: 输出学习摘要

### 查询字段
1. 读取 `references/data_fields_txt/TOP3000/` 下的字段文件
2. 根据用户描述匹配字段
3. 返回字段列表及用途

### 优化现有Alpha
当用户提供Alpha及其指标（Sharpe/Returns/Fitness/Turnover等）时：
1. **读取优化指南**: `references/alpha_optimization_guide.md`
2. **分析表达式**: 解析结构、字段、参数
3. **诊断问题**: 根据指标判断优化方向
4. **给出建议**: 参考优化指南，提供具体改进方案

---

## 知识库路径
```
C:\Users\nay\.claude\skills\wq-alpha-assistant\references\
├── data_fields_txt/TOP3000/  # 默认字段来源（必读）
├── fields_simple/TOP3000/    # 精简版字段（仅字段名）
├── clean_alpha/              # 已使用表达式（去重检查+写入）
├── forbidden_items.md        # 禁止字段/操作符（User阶段）
├── template_dedup_rules.md   # 模板去重+禁止模板结构
├── alpha_optimization_guide.md # Alpha优化指南（Sharpe/Returns/Fitness等）
├── template_summary.txt      # 模板精华总结
├── learned_patterns.md       # 学习到的思想（非模板）
└── operators.md              # 算子分类
```

## 输出格式

### 生成表达式时（根据数量决定格式）

**重要**: 每个表达式必须以`;`分号结尾，直接输出到终端

**数量 > 30个**: 直接输出表达式列表，无需解释，无需汇总
```
expression1;
expression2;
expression3;
...
```

**数量 ≤ 30个**: 每个表达式带解释，最后附汇总便于复制
```
【表达式1】
<expression>;
【逻辑】<rationale>

【表达式2】
...

---
【汇总-方便复制】
expression1;
expression2;
expression3;
```

### 学习表达式时
```
【已学习】
表达式: <expression>
思想类型: <idea_type>（如：动量、反转、价值、情绪、复合）
核心逻辑: <logic>
模板结构: <template>（已标记为已使用，后续禁止同结构换字段）
```

---

## 注意事项
- 所有表达式必须符合BRAIN平台语法
- **每个表达式必须以`;`分号结尾**
- **直接输出到终端，不写入文件**
- **不查询clean_alpha，只查询template文件**
- **严格执行模板去重**：同结构换字段视为重复
- 优先组合多个成功思想，创造新结构
