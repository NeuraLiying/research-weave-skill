# Research Weave：调研、定位与设计

调研日期：2026-10-31。目标是帮助研究者在大量论文中分配注意力，并将文献转化为可检查的研究判断。这里将用户提出的历史脉络、关系网络、研究相关性、矛盾性，以及补充提出的支持证据汇聚，作为五个核心维度。

## 1. 调研了什么，吸收什么

检查了以下项目的实际 SKILL.md 或官方文档，未安装或执行第三方 skill。引用的是设计思想，当前实现独立编写。GitHub star 只是选择有影响力设计样本的线索，不是能力验证。截至本次查询，Anthropic skills 约 18.6 万、Superpowers 约 31 万、K-Dense Scientific Agent Skills 约 5.5 万 stars，均为会变化的仓库级数字，不能归属于单个 skill。[Anthropic 仓库](https://github.com/anthropics/skills)、[Superpowers 仓库](https://github.com/obra/superpowers)、[K-Dense 仓库](https://github.com/K-Dense-AI/scientific-agent-skills)。

| 直接检查的对象 | 有价值的设计 | 本 skill 的取舍 |
|---|---|---|
| [K-Dense literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md) | 检索可追溯；区分检索记录、文章版本和研究；引用存在不代表支持论点 | 保留检索/筛选账本与版本去重。常规使用不强制完整 PRISMA，也不引入绘图服务依赖 |
| [K-Dense scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md) | 先提取结果再评价；区分观察、解释与适用范围；按具体结果评价证据 | 判断单位细化到论点。按 ML、理论、系统等研究类型选择标准，避免通用质量打分 |
| [yananlong research-systematic-literature-review](https://github.com/yananlong/codex-skills/blob/main/research/research-systematic-literature-review/SKILL.md) | 分 review profile；检查已知种子能否被检索找回；针对遗漏修复搜索；对覆盖承诺设限 | 这是接近的功能参照，已有 critical evidence map 和对抗检索。我们强调研究决策、论点间网络和矛盾到实验的路径，不主张“首次做证据地图” |
| [drader research](https://github.com/drader/researcher_agent/blob/main/skills/research/SKILL.md) | 按用户目标选产出；明确呈现来源之间的分歧 | 保留任务导向和分歧分析。允许 agent 给出有根据的研究判断；省去常规步骤的反复确认 |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 用真实请求测试行为；分开触发准确性与任务质量；对照与迭代 | 配套触发样例、行为案例、独立试用和明确验证边界；不把自写检查器通过称为效果提升 |
| [Superpowers writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) | 用压力/反例检验说明是否真正改变行为；确定性约束可由代码检查 | 检验摘要越权、重复证据、表面冲突等失败模式。保留判断空间，不照搬所有严格纪律或依赖链 |
| [OpenAI 官方 Skills 说明](https://developers.openai.com/plugins/concepts/skills) | 元数据负责选择，正文提供工作流，可附脚本和参考；工具与工作流分工 | 简短入口 + 按需参考 + 标准库检查器。搜索供应方可以替换，避免把本地路径或账号写入可移植正文 |

本机还检查了 `paper-search`、`scoop-check`、`evidence-grounded-research-strategy` 与 `idea-spark` 的入口。它们分别承担候选检索、新颖性核查、从实验重新定位研究、生成方法方向。Research Weave 提供从文献到判断的证据组织层；这些已有 skill 可以消费它的结果，但不是运行依赖。

## 2. 定位与边界

定位是 **面向研究决策的文献发现与证据综合 skill**。承诺交付：值得读什么、为什么、证据够不够、彼此如何连接、尚有什么未知。它需要具备检索与筛选能力，同时保留对原文的核查。

主要差异在组合及约束：研究决策驱动的注意力分配；同时呈现历史分支、支持汇聚和矛盾；把重要分歧落实成可区分解释的实验。相关概念已有许多先例，需要通过使用与对照验证组合的价值，不能把新的名称视为方法新颖性。

适用场景：进入新方向、已有方向的阅读取舍、研究定位、理解相互冲突的结果，以及增量更新文献图。不直接承诺完整系统综述、正式 meta-analysis、全球首次性证明或一个可发表的方法。

## 3. 五个维度如何执行

| 维度 | 分析单位 | 可审阅的产物 | 常见误判防线 |
|---|---|---|---|
| 历史脉络 | 问题/方法/评价的转变 | 哪篇工作改变了什么，后续哪篇实际采用或挑战 | 时间先后不能直接推出影响；保留分叉和失败路线 |
| 关系网络 | 有条件的论点及证据出处 | 支持、反驳、边界、依赖、迁移、替代关系；事实边与假设边分开 | 关键词或互引不等于相互证实 |
| 研究相关性 | 文献与具体决策的关系 | 事实、机制、方法、评价、边界、反向证据、类比及迁移条件 | 主题相近不保证对当前研究有用 |
| 支持汇聚 | 一个范围明确的命题 | 支持论文数、证据家族、已确认独立检验、条件覆盖和最强反例 | 不能把多篇转述算成多次实验；不能按票数决定真伪 |
| 矛盾性 | 对齐条件后的结论对 | 可比冲突、范围不一致、证据不足、并不对立；替代解释和区分实验 | 不把显著/不显著差异直接叫冲突；不把冲突自动变成 gap |

支持数量确实是评判因子。在质量与适用性相近时，多个独立来源的收敛比单一结果更有说服力。这个因素与可信度、独立性、覆盖面一起分析，不压成一个随意加权的分数。同一篇论文可以包含多个独立实验；不同论文也可能共用同一原始结果，因此账本允许结果级的 evidence_family 覆盖文章默认值。

## 4. 补充的设计

**结论可改变性。** 每项阅读建议都写清楚：读哪个部分、能回答什么、会改变哪个判断。精读、局部阅读、补取原文、暂缓、排除有实质差别。知名论文也可能暂缓，低引用诊断也可能优先。

**证据层级和出处。** 对每条论点分别保存观察、作者解释、agent 推断。摘要可以支持候选筛选，无法单凭摘要将科学结论标为已支持。复用数据、模型或结果的关系要保留；来源不确定时明确未知。

**反向检索与停止。** 搜索历史别名、机制、评价、负结果和邻域启发，避免只支持已有方向。达到预算或连续扩展不再改变实质判断时停止，并报告遗漏。没有查到不等于不存在。

**可以让 gap 消失。** 对重要未知要求可推翻 motivation 的结果，例如对齐成本后简单重采样已足够。这个字段防止把所有观察都解释成“值得继续做”。

**渐进使用。** Scout/Map/Update 共用流程，按投入缩放。只需短回答时不强制生成多个文件；完整使用才输出账本。参考按需加载，运行时不依赖特定数据库、模型或额外 skill。

## 5. Agent 方面可以积累什么

可以积累检索召回修复、来源可追溯性、关系判断、冲突分类、阅读优先级和更新稳定性的行为案例。初期宜评估：重要种子找回情况；错误支持边/冲突边；重复证据误计；决定性来源核查率；阅读预算内覆盖的重要不确定性；新证据是否真正改变旧结论。

目前这些是评估维度，不是已经验证的性能结论。未来可用固定文献包比较普通总结、现有研究 skill 与 Research Weave，盲评研究决策的准确性及耗时/成本，并保留无冲突、无新 gap 的负例。仅增加格式通过率或报告长度不算研究判断提升。

## 6. 这次的实现

源码为 `skills/research-weave/`：入口、三个按需参考、UI 元数据、证据检查脚本。仓库外层提供调研说明、真实文献示例、虚构行为测试包和检查器测试，方便后续优化与公开展示。

当前实现不执行无人值守长期抓取，不自动订阅，不创建远程仓库。质量保证及仍未覆盖的测试见 [验证记录](../evals/validation.md)。发布前需要真实项目上的多次使用与对照；命名、许可证、展示方式可在下一轮决定。
