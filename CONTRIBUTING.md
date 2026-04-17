# Contributing / 贡献指南

Thanks for wanting to make this tutorial better! This project is a bilingual (Chinese + English) interactive finance-derivatives course.
谢谢你愿意让这份教程变得更好！这是一个中英双语的互动金融衍生品课程。

---

## How to contribute / 如何贡献

### 1. Fix a typo, bug, or unclear explanation / 修 typo、bug 或讲不清楚的段落

1. Fork the repo and create a branch: `git checkout -b fix/your-topic`
   Fork 本仓库后创建分支：`git checkout -b fix/your-topic`
2. Make your edit in the relevant notebook or markdown file.
   在相关的 notebook 或 markdown 文件里改动。
3. Run the test suite locally: `python _test_notebooks.py` — it must stay green.
   本地跑测试：`python _test_notebooks.py`，需要保持全绿。
4. Commit with a short, descriptive message and open a PR.
   用简短清晰的 message 提交，然后发 PR。

### 2. Add a new chapter / 新增章节

1. Create `ChXX_topic/ChXX_topic.ipynb` (e.g. `Ch15_exotic_options/Ch15_exotic_options.ipynb`).
   创建 `ChXX_topic/ChXX_topic.ipynb`。
2. Follow the existing chapter structure:
   遵循现有章节结构：
   - Intro markdown (concepts, why it matters) / 介绍 markdown（概念 + 为什么重要）
   - Setup code cell (imports + color palette + `print('Setup done!')`) / setup 代码 cell
   - Explanatory markdown / 讲解 markdown
   - Interactive code cell (sliders via `ipywidgets.interact`) / 互动代码 cell
   - Summary markdown with "Next chapter →" pointer / 总结 markdown + "下一章" 指引
3. Update `README.md` chapter index and the badge `chapters-14`.
   同步更新 `README.md` 的章节目录和徽章数字。

---

## Style rules / 写作约定

### Code / 代码
- **Identifiers, string literals, and comments → English only.** Avoids cross-platform encoding issues.
  **变量名 / 字符串 / 注释：一律英文。** 避免跨平台编码问题。
- Use the shared color palette: `C_GREEN, C_RED, C_ORANGE, C_BLUE, C_PURPLE`.
  使用统一颜色方案。
- Interactive plots go through `ipywidgets.interact`. Avoid heavy state — re-render inside the function.
  互动图通过 `ipywidgets.interact`，避免外部状态，全部在函数内重绘。

### Markdown prose / 讲解文字
- **Every paragraph is bilingual**: Chinese first, English right below (or vice versa). Do not leave a concept in only one language.
  **每段都要双语**：中文在前，英文紧随其后（或反之）。不要只写一种语言。
- Tables: if columns are labels, make both languages appear (`Lots / 手数`).
  表格列名中英并列。
- Formulas use LaTeX, inside `$$...$$` blocks.
  公式用 LaTeX，放在 `$$...$$` 块里。

### Committed notebook outputs / Notebook 的执行结果
- **Clear outputs before committing.** Learners should run cells interactively.
  **提交前请清空 outputs**，让学习者自己动手运行。
- Quick way / 快捷命令:
  ```bash
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ChXX_topic/*.ipynb
  ```

---

## Test locally / 本地测试

```bash
pip install -r requirements.txt
python _test_notebooks.py
```

Expected / 预期:

```
PASS: N  FAIL: 0  TIMEOUT: 0  TOTAL: N
```

`N` updates when you add or remove notebooks. Any failure must be fixed before merging.
`N` 随着章节增减变化。任何失败都必须修好才能合并。

---

## Translation help wanted / 征求翻译支援

If you spot a section where the Chinese or English feels awkward, cramped, or loses nuance, just open an issue or PR with a suggested rewrite. Non-native speakers especially welcome — the current text was written by a bilingual author but four eyes are better than two.
如果看到哪一段中文或英文翻得别扭、拥挤、或丢了味道，欢迎开 issue 或直接 PR 你的改写版。特别欢迎非母语者 —— 当前文本由双语作者写就，但多一双眼睛总是好事。

---

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
提交 PR 即表示你同意贡献以本项目的 [MIT License](LICENSE) 发布。
