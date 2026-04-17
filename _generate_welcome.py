"""Generate Welcome.ipynb — the landing notebook for the HF Space.

Emits a chapter-navigation TOC (bilingual, grouped by part) that opens each
chapter's primary notebook via a relative JupyterLab tree URL. Invoked at
Docker build time by the Dockerfile so the Space lands on a rendered
welcome page regardless of JupyterLab's workspace state.
"""

import json
import pathlib

APP_DIR = pathlib.Path(__file__).resolve().parent

# (chapter_dir, primary_notebook, english_title, chinese_title)
PARTS: list[tuple[str, list[tuple[str, str, str, str]]]] = [
    (
        "Part 0 · Foundations / 基础",
        [
            (
                "Ch00_preface_fundamentals",
                "Ch00_preface_fundamentals.ipynb",
                "Preface: finance literacy for absolute beginners",
                "序言：给完全零基础的你",
            ),
        ],
    ),
    (
        "Part 1 · Trading mechanics / 交易机制",
        [
            (
                "Ch01_market_overview",
                "Ch01_market_overview.ipynb",
                "Financial-market overview · spot vs derivatives · leverage",
                "金融市场总览",
            ),
            (
                "Ch02_margin_liquidation",
                "Ch02_margin_liquidation.ipynb",
                "Margin, liquidation, commission, dividends, overnight swap",
                "保证金与爆仓",
            ),
            (
                "Ch03_trading_costs",
                "Ch03_trading_costs.ipynb",
                "Spread · commission · swap",
                "交易成本",
            ),
        ],
    ),
    (
        "Part 2 · Pricing / 定价核心",
        [
            (
                "Ch04_forwards_futures",
                "Ch04_forwards_futures.ipynb",
                "Forward & futures pricing · no-arbitrage · basis",
                "远期与期货",
            ),
            (
                "Ch05_options_basics",
                "Ch05_options_basics.ipynb",
                "Calls, puts, long / short, payoff diagrams",
                "期权基础",
            ),
            (
                "Ch06_black_scholes",
                "Ch06_black_scholes.ipynb",
                "Black-Scholes formula + 3D price surface",
                "Black-Scholes 定价",
            ),
            (
                "Ch07_greeks",
                "Ch07_greeks.ipynb",
                "Delta / Gamma / Theta / Vega risk dashboard",
                "希腊字母",
            ),
            (
                "Ch08_volatility_surface",
                "Ch08_volatility_surface.ipynb",
                "Implied vol · smile · skew · 3D surface",
                "波动率曲面",
            ),
            (
                "Ch09_option_strategies",
                "Ch09_option_strategies.ipynb",
                "Bull / bear spreads, straddle, strangle, butterfly",
                "期权策略",
            ),
            (
                "Ch10_interest_rate_swap",
                "Ch10_interest_rate_swap.ipynb",
                "Fixed vs floating cash-flow visualization",
                "利率互换",
            ),
        ],
    ),
    (
        "Part 3 · Crypto derivatives / 加密衍生品",
        [
            (
                "Ch11_perpetual_swap",
                "Ch11_perpetual_swap.ipynb",
                "Perpetuals · funding-rate mechanism",
                "永续合约",
            ),
            (
                "Ch12_usdt_vs_coin_margined",
                "Ch12_usdt_vs_coin_margined.ipynb",
                "Linear vs convex P&L · double whammy",
                "U 本位 vs 币本位",
            ),
            (
                "Ch13_crash_simulation",
                "Ch13_crash_simulation.ipynb",
                "BTC crash at different leverage levels",
                "极端行情模拟",
            ),
        ],
    ),
    (
        "Part 4 · Capstone / 综合",
        [
            (
                "Ch14_trading_desk",
                "Ch14_trading_desk.ipynb",
                "All-asset interactive trading dashboard",
                "模拟交易台",
            ),
        ],
    ),
]

INTRO = """# Re:0 — 从零开始的衍生品 / Starting Derivatives From Zero

👋 欢迎。这是一门 14 章双语教程，把期货 / 期权 / 互换从直觉讲到公式。
Welcome to a 14-chapter bilingual tour of futures, options and swaps —
built from intuition up to the pricing equations.

点击下方任何链接打开对应章节（在新 tab 中）。左侧文件浏览器也能看到全部文件。
Click any link below to open that chapter in a new tab. The file browser
on the left shows the full project tree.

## 🎯 Reader paths / 读者地图

| 背景 / Background | 建议路径 / Suggested path |
|---|---|
| 零基础 · Zero finance | Ch00 → Ch01 → … 顺序 / in order |
| 已交易股票 · Stocks already | skim Ch00–Ch03，从 Ch04 精读 |
| 只想学期权 · Options only | Ch05 → Ch06 → Ch07 → Ch08 → Ch09 |
| 只想学加密永续 · Crypto perps | Ch01 → Ch02 → Ch11 → Ch12 → Ch13 |

---
"""

OUTRO = """
---

## 🚀 Run elsewhere / 本地运行

本地 / Local:

```bash
git clone https://github.com/ShepherdLoveYou/re0-futures-options-and-derivatives
cd re0-futures-options-and-derivatives
pip install -r requirements.txt
jupyter lab
```

源码 & 反馈 / Source & feedback: <https://github.com/ShepherdLoveYou/re0-futures-options-and-derivatives>
"""


def render_markdown() -> str:
    lines: list[str] = [INTRO.strip(), ""]
    for part_title, chapters in PARTS:
        lines.append(f"## {part_title}\n")
        lines.append("| # | Chapter / 章节 | 中文标题 |")
        lines.append("|---|---|---|")
        for folder, notebook, en_title, zh_title in chapters:
            ch_num = folder.split("_", 1)[0].removeprefix("Ch")
            href = f"./{folder}/{notebook}"
            lines.append(f"| {ch_num} | [{en_title}]({href}) | {zh_title} |")
        lines.append("")
    lines.append(OUTRO.strip())
    return "\n".join(lines)


def build_notebook(body: str) -> dict:
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": body,
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    body = render_markdown()
    nb = build_notebook(body)
    (APP_DIR / "Welcome.ipynb").write_text(
        json.dumps(nb, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
