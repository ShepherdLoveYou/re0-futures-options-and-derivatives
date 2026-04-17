# Re:0 — 从零开始的衍生品 / Starting Derivatives From Zero

_Re:0 &middot; Futures, Interest & Options — the finance class you thought was philosophy_

---

## 开场：一个美丽的误会 / A Beautiful Misunderstanding

> 记得以前在读研的时候，学校开了一门课，叫 **《Futures, Interest and Options》**。
> 我以为是《未来、兴趣与选择》，立刻兴冲冲地选了 —— 感觉很哲学，能指导自己未来的人生。
>
> 上了课才发现 …… 是《**期货、利息和期权**》。

> Back in grad school I once enrolled in a course called **"Futures, Interest and Options"** —
> convinced it was going to teach me life philosophy.
> It turned out to be about *futures, interest rates, and options*.

翻译的锅背得实在有点沉 —— 不过那门课真的在教"未来、利息与选择"，只是换成了 Black-Scholes 偏微分方程的语言：

- **Futures 期货** → 你敢不敢把未来锁在今天的价格上？
- **Interest 利息** → 时间确实有价值，你的耐心值多少钱？
- **Options 期权** → 花小钱买一个"可以反悔的权利"。

That course really does teach you about the future, interest, and choice — just phrased in the language of Black-Scholes PDEs:

- **Futures** → dare to lock tomorrow's future at today's price?
- **Interest** → time really does have a price; how much is your patience worth?
- **Options** → pay a small premium for the right to change your mind.

这个仓库，就是我为"当年那个以为选了哲学课的自己"写的教程。
This repo is the tutorial I wish that version of me had started with.

---

## What's inside / 教程内容

- **14 bilingual chapters** — markdown prose in Chinese + English, side by side.
  **14 章中英双语** —— 每段讲解中英并列。
- **Drag-a-slider interactive charts** in every chapter (via `ipywidgets`).
  **每章一组互动图表**，拖动滑块实时体验。
- **Real ground covered** — inflation, leverage, margin math, Black-Scholes, the Greeks, volatility smiles, option strategies, interest-rate swaps, BTC perpetual funding, USDT vs. coin-margined convexity, crash simulations.
  **覆盖范围** —— 从通胀 / 杠杆 / 保证金计算，到 Black-Scholes / 希腊字母 / 波动率微笑 / 期权策略 / 利率互换 / BTC 永续资金费率 / U 本位 vs 币本位凸性 / 暴跌模拟。
- **Code is 100 % English** (identifiers, strings, comments), so it runs cleanly in any locale.
  **代码 100 % 英文**（变量名、字符串、注释），跨环境零编码问题。
- **Zero prior finance knowledge assumed.** Chapter 0 starts with "what is inflation?".
  **零金融基础** —— 第 0 章从"什么是通胀"讲起。

---

## Chapter index / 章节索引

### Part 0 — Starter / 起点
| Folder | Chapter | 中文标题 |
|--------|---------|----------|
| [`Ch00_preface_fundamentals/`](Ch00_preface_fundamentals/) | Preface: finance literacy for absolute beginners | 序言：给完全零基础的你 |

### Part 1 — FX Fundamentals / 外汇基础（必修）
| Folder | Chapter | 中文标题 |
|--------|---------|----------|
| [`Ch01_market_overview/`](Ch01_market_overview/) | Financial-market overview · spot vs. derivatives · leverage | 金融市场总览 |
| [`Ch02_margin_liquidation/`](Ch02_margin_liquidation/) | Margin, liquidation, commission, dividends, overnight swap | 保证金与爆仓 |
| [`Ch03_trading_costs/`](Ch03_trading_costs/) | Spread · commission · swap | 交易成本 |

### Part 2 — Traditional Derivatives / 传统衍生品
| Folder | Chapter | 中文标题 |
|--------|---------|----------|
| [`Ch04_forwards_futures/`](Ch04_forwards_futures/) | Forward & futures pricing · no-arbitrage · basis | 远期与期货 |
| [`Ch05_options_basics/`](Ch05_options_basics/) | Calls, puts, long / short, payoff diagrams | 期权基础 |
| [`Ch06_black_scholes/`](Ch06_black_scholes/) | Black-Scholes formula + 3D price surface | Black-Scholes 定价 |
| [`Ch07_greeks/`](Ch07_greeks/) | Delta / Gamma / Theta / Vega risk dashboard | 希腊字母 |
| [`Ch08_volatility_surface/`](Ch08_volatility_surface/) | Implied vol · smile · skew · 3D surface | 波动率曲面 |
| [`Ch09_option_strategies/`](Ch09_option_strategies/) | Bull / bear spreads, straddle, strangle, butterfly | 期权策略 |
| [`Ch10_interest_rate_swap/`](Ch10_interest_rate_swap/) | Fixed vs. floating cash-flow visualization | 利率互换 |

### Part 3 — Crypto Derivatives / 加密衍生品
| Folder | Chapter | 中文标题 |
|--------|---------|----------|
| [`Ch11_perpetual_swap/`](Ch11_perpetual_swap/) | Perpetuals · funding-rate mechanism | 永续合约 |
| [`Ch12_usdt_vs_coin_margined/`](Ch12_usdt_vs_coin_margined/) | Linear vs. convex P&L · double whammy | U 本位 vs 币本位 |
| [`Ch13_crash_simulation/`](Ch13_crash_simulation/) | BTC crash at different leverage levels | 极端行情模拟 |

### Part 4 — Integrated Practice / 综合实战
| Folder | Chapter | 中文标题 |
|--------|---------|----------|
| [`Ch14_trading_desk/`](Ch14_trading_desk/) | All-asset interactive trading dashboard | 模拟交易台 |

### Bonus / 附加
- `Ch02_margin_liquidation/` 包含三份题目 txt（中英双语）和两份讲解 notebook：10 题保证金 & 爆仓走解、15 题手续费/股息/隔夜利息走解。
  `Ch02_margin_liquidation/` also ships three bilingual exercise `.txt` files and two walk-through notebooks: a 10-problem margin + liquidation tour and a 15-problem commission / dividend / swap tour.

---

## Install & run / 安装与运行

```bash
pip install -r requirements.txt
```

然后任选一种方式启动 / Then launch via any of:

- **VS Code** — open any `.ipynb`, pick a Python kernel in the top-right.
- **JupyterLab** — `jupyter lab`
- **Classic Notebook** — `jupyter notebook`

Inside a notebook, `Shift+Enter` runs cells one at a time. Always run the first setup cell before interacting with the sliders.
在 notebook 内按 `Shift+Enter` 逐 cell 运行。第一个 setup cell 必须先跑，才能拖滑块。

### Optional / 可选 — QuantLib

A few cells can use **QuantLib-Python** for professional-grade option pricing, and gracefully fall back to `scipy` if it's missing:
部分 cell 可调用 **QuantLib-Python** 做专业期权定价，未安装时自动降级到 `scipy`：

```bash
pip install QuantLib
```

### Execute-test every notebook / 批量执行测试

```bash
python _test_notebooks.py
```

Expected output / 预期输出：

```
PASS: 18  FAIL: 0  TIMEOUT: 0  TOTAL: 18
```

---

## Conventions / 代码与写作约定

- **Identifiers, string literals, and comments are English-only.** Avoids encoding issues across platforms.
  **变量名 / 字符串 / 注释一律英文。** 避免跨平台编码问题。
- **Markdown prose is bilingual Chinese + English**, so you can pick either language or read both.
  **Markdown 讲解是中英双语并列**，任选一种语言或对照阅读。
- Unified color palette / 统一颜色方案: `C_GREEN, C_RED, C_ORANGE, C_BLUE, C_PURPLE`.
- Every notebook starts with the same setup cell / 每个 notebook 的第一个 cell 是相同的 setup 块.

### Contributing a new chapter / 新增章节

1. Create `ChXX_topic/ChXX_topic.ipynb` with the same structure: intro markdown → setup code → explanatory markdown → interactive code → summary markdown.
2. Keep code fully English, markdown bilingual.
3. Run `python _test_notebooks.py` — make sure it stays green.

---

## Tech stack / 技术栈

- **Python 3.10+** (tested on 3.13)
- **matplotlib** — static plots
- **ipywidgets** — interactive sliders
- **numpy · pandas · scipy** — numerical core
- **QuantLib-Python** (optional) — professional option-pricing engine

---

## License

MIT — see [`LICENSE`](LICENSE).

> 免责声明 / Disclaimer —— 本仓库纯粹是教育内容，不构成任何投资建议。任何真实交易的盈亏与作者无关。
> This repository is educational content only and does not constitute investment advice. The authors are not responsible for any P&L on real trades.

---

_"So the course wasn't actually about life philosophy. Turns out, life is."_
_"所以那门课终究不是哲学课。 —— 不过生活是。"_
