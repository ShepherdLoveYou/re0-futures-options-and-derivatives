---
title: Re0 Futures Options And Derivatives
emoji: 💻🐳
colorFrom: gray
colorTo: green
sdk: docker
pinned: false
tags:
- jupyterlab
license: mit
short_description: "Re:0 — Starting Derivatives From Zero."
---

# Re:0 — 从零开始的衍生品 / Starting Derivatives From Zero

_Re:0 &middot; Futures, Interest & Options — the finance class you thought was philosophy_

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-interactive-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Chapters](https://img.shields.io/badge/chapters-14-blueviolet)](#chapter-index--章节索引)
[![Bilingual](https://img.shields.io/badge/docs-中文%20%2B%20English-red)](#)
[![Open in HF Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Open%20in%20Space-yellow)](https://huggingface.co/spaces/jingjiang233/re0-futures-options-and-derivatives)
[![test-notebooks](https://github.com/ShepherdLoveYou/re0-futures-options-and-derivatives/actions/workflows/test-notebooks.yml/badge.svg)](https://github.com/ShepherdLoveYou/re0-futures-options-and-derivatives/actions/workflows/test-notebooks.yml)

> 🚀 **在线运行 / Run online**：本项目已部署到 [Hugging Face Space](https://huggingface.co/spaces/jingjiang233/re0-futures-options-and-derivatives)，可直接在浏览器里打开 JupyterLab 运行所有章节，无需本地环境。
> This project is deployed as a Hugging Face Space — open JupyterLab in your browser and run all chapters with zero local setup.

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

## How to use this tutorial / 怎么用这份教程

- **Never touched finance?** Start from `Ch00_preface_fundamentals/` and go in order. Don't skip.
  **金融零基础**：从 `Ch00_preface_fundamentals/` 开始顺序阅读，不要跳章。
- **Already trade stocks / FX?** You can skim Ch00–Ch03 and start serious reading at `Ch04_forwards_futures/`.
  **已经交易股票 / 外汇**：可以略读 Ch00–Ch03，从 `Ch04_forwards_futures/` 开始精读。
- **Here for options only?** Ch05 → Ch06 → Ch07 → Ch08 → Ch09 is a self-contained options mini-course.
  **只想学期权**：Ch05 → Ch06 → Ch07 → Ch08 → Ch09 是自洽的期权小课。
- **Here for crypto perpetuals?** Ch01 → Ch02 → Ch11 → Ch12 → Ch13 is the shortest crypto path.
  **只想学加密永续**：Ch01 → Ch02 → Ch11 → Ch12 → Ch13 是最短的加密路径。
- **Every chapter is one `.ipynb` file.** Open, click into the first cell, press `Shift+Enter`, repeat. Drag sliders freely once the interactive cell has run.
  **每章就是一个 `.ipynb`**：打开、光标点到第一个 cell、按 `Shift+Enter`、往下走。互动 cell 跑完后就可以随便拖滑块。

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
PASS: 17  FAIL: 0  TIMEOUT: 0  TOTAL: 17
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

## Where this project lives / 项目托管在哪

| Role / 角色 | Location / 位置 | What it's for / 作用 |
|---|---|---|
| Source of truth / 源码源头 | [GitHub `ShepherdLoveYou/re0-futures-options-and-derivatives`](https://github.com/ShepherdLoveYou/re0-futures-options-and-derivatives) | 所有 PR、issue、release 都走 GitHub |
| Live interactive deploy / 在线部署 | [HF Space `jingjiang233/re0-futures-options-and-derivatives`](https://huggingface.co/spaces/jingjiang233/re0-futures-options-and-derivatives) | Public JupyterLab 环境，浏览器即开即用 |

You only need to push to **GitHub** — the HF Space mirrors itself from GitHub main automatically.
你**只需要 push 到 GitHub**，HF Space 会从 `main` 自动镜像过去。

### Pipeline / CI 与部署流水线

Every push to `main` on GitHub triggers two workflows in parallel:
每次向 GitHub `main` 推送都会并行触发两个 workflow：

1. [`test-notebooks.yml`](.github/workflows/test-notebooks.yml) — executes every chapter notebook via `nbconvert` (180 s timeout each). Fails loudly if any notebook errors or times out. PRs run the same check before merge.
   用 `nbconvert` 执行每个章节 notebook（每个 180 s 超时），有任何报错/超时就整体 fail。PR 合并前也会跑。
2. [`sync-to-hf.yml`](.github/workflows/sync-to-hf.yml) — mirrors `main` onto the HF Space git remote. HF then rebuilds the Docker image (~2 min on the slim Python base) and restarts the JupyterLab app — the new content is live ~3 minutes after the GitHub push.
   把 `main` 镜像推到 HF Space 的 git remote，HF 随后 rebuild Docker 镜像（slim 基础镜像下大概 2 分钟）并重启 JupyterLab，整条链路约 3 分钟内生效。

Auth for the sync workflow is a fine-grained HF write token stored as the `HF_TOKEN` repository secret on GitHub, scoped to this single Space.
同步 workflow 的鉴权是 GitHub secret `HF_TOKEN`，是一个仅授权给这一个 Space 的 HF 细粒度写 token。

### Space container / Space 容器

The Space serves JupyterLab from a [`python:3.11-slim`-based image](Dockerfile) on HF's free CPU tier. The image is hardened so visitors can execute any notebook cell but cannot persist modifications to the tutorial files:
Space 基于 [`python:3.11-slim` 镜像](Dockerfile) 跑 JupyterLab，使用 HF 免费 CPU。镜像做了安全加固 —— 访客可以跑任意 cell，但无法永久修改教程文件：

- `/home/user/app` — root-owned, read-only at the OS level (save / delete / create all fail with `PermissionError`).
  `/home/user/app` 归 root，OS 层只读，保存 / 删除 / 新建都会 `PermissionError`。
- No `sudo` grant — visitors run as the `user` account with no escalation path.
  没有 `sudo` 授权，访客以 `user` 身份运行，无提权路径。
- Python runtime (`/usr/local/lib/pythonX.Y/site-packages`) is also root-owned, so no visitor can `pip install` a malicious shim that poisons other sessions.
  Python 运行时同样 root 所有，访客无法通过 `pip install` 注入恶意包。
- `/home/user/.jupyter` is the only writable path, reserved for JupyterLab runtime state.
  `/home/user/.jupyter` 是仅有的可写目录，专供 JupyterLab 运行时使用。

---

## Authors / 作者

- **Mac Jing / 麦克·京** — author & maintainer / 作者与维护者
  - GitHub: [ShepherdLoveYou](https://github.com/ShepherdLoveYou)
  - Hugging Face: [jingjiang233](https://huggingface.co/jingjiang233)

Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).
欢迎贡献 —— 见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## License

MIT — see [`LICENSE`](LICENSE).

> 免责声明 / Disclaimer —— 本仓库纯粹是教育内容，不构成任何投资建议。任何真实交易的盈亏与作者无关。
> This repository is educational content only and does not constitute investment advice. The authors are not responsible for any P&L on real trades.

---

_"So the course wasn't actually about life philosophy. Turns out, life is."_
_"所以那门课终究不是哲学课。 —— 不过生活是。"_
