# 检索与阅读记录

日期：2026-10-31。固定三篇历史论文示例，非全景扫描。候选集由预先给定的题目限定；实际纳入并局部检查 3 篇，没有把网页估算命中数当筛选数。

| 查询 | 来源 | 结果与检查范围 |
|---|---|---|
| Self-Refine iterative refinement self feedback NeurIPS 2023 | Web → NeurIPS 主来源 | §2–3、Table 1、Appendix K.1；比较表提取核对 |
| Large Language Models Cannot Self-Correct Reasoning Yet ICLR 2024 | Web → ICLR 主来源 | 定义、Table 1/4/8、§5；实际重查前作的关系 |
| CRITIC tool interactive critiquing ICLR 2024 | Web → ICLR 主来源 | §4.2、Table 2、Appendix D.6；工具权限及旧结果复用 |

预先限定包内无整篇排除；暂缓无关任务的结果细节。读到了与“无工具总无效”不一致的正向行，保留并据此限制结论。论文主链接与版本记录在 evidence.json。

未执行：完整 backward/forward citation sweep、跨领域搜索、近期全景、后来解决情况检索、版本/更正/撤稿专项核查。搜索中出现的其他综述、2026 年工作和非主来源页面未纳入证据包；未读取它们的全文，不据此作结论。

停止依据：三篇示例预算已用完，不声称检索饱和。若用于实际项目，下一步应明确目标设置，并检索 2025–2026 年相关发现及直接复现实验。

## 同日独立审核后的重查

初版遗漏了 Huang 等 §3/Table 3、oracle 停止与 §4/Table 7，对 CRITIC 的无工具结果也选择性展示。重新核对主来源 PDF 相关章节和完整模型行后，保留原 C1–C4，补入 C0/C5–C8，退役宽泛 Q1，建立具体 Q2–Q5。原始版本保留在 evals/runs/example-v1。本次为原文复核，不计作新一轮在线发现或召回评估；停止仍因固定三篇预算。

交叉核对时发现 CRITIC 的 Table 2 与 Appendix D.6/Table 10 对 Text-Davinci-003/GSM8K 工具版分别报告 72.2/71.2；按主表记录并保留未解差异，没有把它直接升级为研究 gap。
