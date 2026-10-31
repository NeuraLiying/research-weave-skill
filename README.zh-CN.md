<p align="center">
  <img src="docs/assets/research-weave.svg" alt="Research Weave：找到能改变研究判断的论文" width="100%">
</p>

<p align="center">
  <strong>论文淘金：寻找有价值的论文，织出有证据的研究脉络。</strong><br>
  <a href="README.md">English</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="examples/self-correction/report.md">真实示例</a> ·
  <a href="skills/research-weave/SKILL.md">Skill 正文</a>
</p>

**把一堆论文，变成有取舍的阅读计划、可追溯的证据网络和更清楚的研究问题。**

## 为什么做这个 skill？

研究者的注意力有限，论文却越来越多。在 AI 加速研究与写作的时代，精致的摘要和流畅的总结，容易让证据质量截然不同的论文都显得很有价值。

真正困难的判断仍然存在：**哪些论文值得精读？什么已经被证实？不同结果能否相互印证？这些工作究竟会改变我的哪个研究判断？**

Research Weave 把这些问题变成 agent 可以反复执行的工作流：追溯一个方向如何发展，连接不同论文中的具体论点，检查支持和反向证据，最后给出有理由的阅读队列与研究定位。它希望帮助研究者把时间投入最能改变判断的地方。

## 用五个维度“沙中淘金”

| 维度 | Agent 要调查什么 | 对研究者的价值 |
|---|---|---|
| **历史脉络** | 哪些工作改变了问题、方法或评价？后续实际采用或挑战了什么？ | 理解转折与分支，找到今天问题的来处 |
| **证据网络** | 哪些论点互相支持、限制、依赖或反驳？能否连接邻近领域？ | 看见单篇总结不容易显露的联系，并保留出处 |
| **研究相关性** | 提供事实、机制、方法、评价、边界、反例，还是类比启发？ | 说明文献如何影响自己的下一步决策 |
| **支持汇聚** | 有多少论文和独立证据支持这个命题？覆盖哪些条件？ | 同时判断支持的广度、质量和迁移限制 |
| **矛盾分析** | 结论是否在可比条件下冲突？什么观察能区分解释？ | 将重要分歧变成可检验的问题与分析实验 |

**更多可信、独立、适用的证据，可以增强一个论点的支持力度。** 因此，skill 分别记录支持论文、共享结果来源和已确认独立的证据贡献。多篇文章转述同一个实验，仍只有一个底层结果；局部发现用于更宽命题时，也必须检查范围和量词。

## 你会得到什么？

- **有取舍的阅读队列**：先读哪篇、具体读哪个部分、会改变哪个判断，哪些暂缓或排除。
- **研究地图**：历史分支与论点关系，区分原文支持的连接和分析假设。
- **证据综合**：支持如何汇聚、最强反例是什么、哪些来源重复、哪里仍然未知。
- **分歧分析**：区分可比冲突、条件不同、证据不足和并不对立，并提出区分实验。
- **项目定位**：继承的假设、已建立的证据、尚未支持的关键一步，以及什么结果会让当前 gap 消失。

通常保存三个可继续使用的文件：

```text
report.md       阅读建议、证据地图、分歧分析与研究定位
evidence.json   论点、出处、支持综合与关系账本
search-log.md   检索、筛选、访问限制与停止原因
```

小问题可以直接在对话中回答；已有证据地图也可以随着新论文或更正结果更新。

## 看一个真实案例：LLM 能否自我修正？

Self-Refine、*Large Language Models Cannot Self-Correct Reasoning Yet* 和 CRITIC 是一组有用的历史材料。仅凭标题，无法判断它们是否在相同条件下互相矛盾。

[三篇论文示例](examples/self-correction/report.md)检查了任务结果、初始提示、工具权限和复用的比较结果，输出阅读取舍、条件化的支持综合，以及一个可能削弱研究动机的诊断实验。这个示例只覆盖选定历史材料，不代表当前领域全景。

仓库还提供[明确标注为虚构的文献包](evals/fixtures/agent-feedback.md)，包含重复证据、摘要口号、跨领域类比和相反结果，可查看[独立试用及修正产物](evals/runs/offline-network/report.md)。

## 快速开始

### 安装到 Codex

克隆仓库，将 skill 目录复制到用户 skills 目录：

```bash
git clone https://github.com/NeuraLiying/research-weave-skill.git
cd research-weave-skill
mkdir -p ~/.agents/skills
cp -R skills/research-weave ~/.agents/skills/
```

这里采用 [Codex 官方文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)所列的用户目录。如果只想供单个项目使用，可放在该项目的 `.agents/skills/research-weave/`。更新已有安装时替换原 skill 目录，避免重复嵌套。

核心文件是 `SKILL.md`、按需参考和一个 Python 辅助脚本。其他支持该格式的 agent 环境可按其文档配置目录和调用方式；本仓库记录的试用在 Codex 中完成，其他运行环境尚未独立测试。

### 给出一个研究决策

```text
使用 $research-weave。

我研究冻结 LLM 在精确答案推理中的无工具自我修正。
当前要决定：构建修正循环，还是把相同推理预算用于重采样。

请追溯重要历史分支和当前工作，比较支持与反向证据，
明确反馈权限和计算预算。选出最值得精读的三篇，
说明各自会改变哪个判断，并提出一个能推翻当前 motivation
的诊断实验。
```

问题还不具体时，可以只给研究方向；已有目标任务、模型、反馈权限、预算、种子论文和决策时，补充这些信息会帮助筛选。输出跟随你的语言，可以使用中文或英文。

| 模式 | 适合什么阶段 |
|---|---|
| **Scout** | 快速进入方向，判断什么值得深入 |
| **Map** | 围绕具体问题，调查历史分支与证据 |
| **Update** | 将新论文或更正结果整合进已有地图 |

在线发现依赖宿主 agent 提供的搜索与原文访问能力。只有本地论文或节选时，也可以做有边界的文献包分析，保留访问不足造成的不确定性。工作流不依赖特定模型、付费 API 或另一个 skill；证据检查器仅需要 Python 3.9+ 标准库。

## 可信度与验证

重要结论应指向实际检查过的原文位置。只有摘要的线索保持暂定，来源观察、作者解释与 agent 推断分开记录。没有检索到某个结果或解决方案，不代表它不存在。

目前包含 **12 项检查器测试**、真实论文示例，以及一轮虚构材料的独立试用和结果审阅。试用曾暴露“把局部负结果计作全称失败命题的直接支持”问题，规则和产物已经修正，初始记录保留。当前是可检查的初版，尚未通过对照评测证明效果优于其他工作流。

```bash
python3 -m unittest discover -s tests -v
python3 skills/research-weave/scripts/check_evidence.py examples/self-correction/evidence.json
```

脚本检查引用、计数与部分证据状态约束；来源含义、科学有效性和检索覆盖仍需审阅。完整过程见[验证记录](evals/validation.md)。

## 深入了解与改进

- [Skill 正文](skills/research-weave/SKILL.md)：agent 加载的执行流程。
- [证据方法](skills/research-weave/references/evidence-method.md)：发现、质量、相关性与支持汇聚。
- [矛盾分析](skills/research-weave/references/contradictions.md)：条件对齐与区分实验。
- [输出约定](skills/research-weave/references/output-contract.md)：可复用证据账本。
- [调研与定位](docs/design-and-research.zh.md)：参考的 skill、设计思想和边界。

发现重要漏文献、重复计数、错误支持关系或虚构矛盾时，欢迎[提交 issue](https://github.com/NeuraLiying/research-weave-skill/issues)，附上研究问题、可访问来源、实际输出和需要纠正的判断。请使用可公开或可分享的材料。具体失败案例会帮助 skill 变得更实用。
