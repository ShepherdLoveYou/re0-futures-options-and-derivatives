"""Generate Welcome.ipynb — the HF Space landing notebook.

Takes the repo's README.md and splices in a clickable chapter-navigation
TOC (each English title links straight to the chapter's primary notebook),
so visitors land on the full bilingual tutorial overview with one-click
chapter access. Invoked by the Dockerfile at image build time, before the
lockdown.
"""

import json
import pathlib
import re

APP_DIR = pathlib.Path(__file__).resolve().parent

# (chapter_dir, primary_notebook, english_title, chinese_title)
PARTS: list[tuple[str, list[tuple[str, str, str, str]]]] = [
    (
        "Part 0 — Starter / 起点",
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
        "Part 1 — FX Fundamentals / 外汇基础（必修）",
        [
            (
                "Ch01_market_overview",
                "Ch01_market_overview.ipynb",
                "Financial-market overview · spot vs. derivatives · leverage",
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
        "Part 2 — Traditional Derivatives / 传统衍生品",
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
                "Fixed vs. floating cash-flow visualization",
                "利率互换",
            ),
        ],
    ),
    (
        "Part 3 — Crypto Derivatives / 加密衍生品",
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
                "Linear vs. convex P&L · double whammy",
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
        "Part 4 — Integrated Practice / 综合实战",
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

SPACE_NOTE = """\
> 👋 你正在 Hugging Face Space 的 JupyterLab 里浏览本教程。点击下方任何章节标题即可在新 tab 中打开。Shift+Enter 执行 cell。
> You're viewing this tutorial in the Hugging Face Space's JupyterLab. Click any chapter title below to open it in a new tab, and run cells with Shift+Enter.
"""


def strip_frontmatter(src: str) -> str:
    """Drop the leading '---\\n...\\n---\\n' YAML block."""
    if src.startswith("---"):
        end = src.find("\n---", 3)
        if end != -1:
            return src[end + 4 :].lstrip()
    return src


def strip_badges(body: str) -> str:
    """Remove shield/badge lines — irrelevant inside a running Space."""
    return re.sub(r"^\[!\[.+?\)\]\(.+?\)\n", "", body, flags=re.MULTILINE)


def replace_online_callout(body: str) -> str:
    """Swap the README's 'deployed to HF Space' callout for a note that
    makes sense when the reader is already inside the Space."""
    pattern = re.compile(
        r"^> 🚀 \*\*在线运行.*?zero local setup\.\n",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub(SPACE_NOTE, body, count=1)


def build_clickable_tables() -> str:
    """Emit the five Part tables with each English title linked straight
    to its chapter notebook via a relative JupyterLab tree path."""
    lines: list[str] = [
        "点击任一英文标题，在新 tab 中打开对应章节 notebook。",
        "Click any English title to open that chapter's notebook in a new tab.",
        "",
    ]
    for part_title, chapters in PARTS:
        lines.append(f"### {part_title}")
        lines.append("| # | Chapter / 章节 | 中文标题 |")
        lines.append("|---|---|---|")
        for folder, notebook, en_title, zh_title in chapters:
            ch_num = folder.split("_", 1)[0].removeprefix("Ch")
            href = f"./{folder}/{notebook}"
            lines.append(f"| {ch_num} | [{en_title}]({href}) | {zh_title} |")
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_part_tables(body: str, new_tables: str) -> str:
    """Replace the five '### Part N — ...' README tables with the
    clickable version. Leaves '## Chapter index' header and '### Bonus'
    subsection intact."""
    pattern = re.compile(r"### Part 0 —.*?(?=\n### Bonus)", re.DOTALL)
    new_body, n = pattern.subn(new_tables + "\n", body)
    return new_body if n else body


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
    readme = (APP_DIR / "README.md").read_text(encoding="utf-8")
    body = strip_frontmatter(readme)
    body = strip_badges(body)
    body = replace_online_callout(body)
    body = replace_part_tables(body, build_clickable_tables())

    nb = build_notebook(body)
    (APP_DIR / "Welcome.ipynb").write_text(
        json.dumps(nb, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
