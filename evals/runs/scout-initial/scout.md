先调优 **fixed γ**；adaptive 暂只值得一次全开销诊断。最贴近目标的 P2（local:P2-v2，Errata）修正了 adaptive 漏计的 KV-cache rebuild：收益从 P1 的 +9% 降为 **+2%，95% 区间 [-3%, +7%]，5 seeds**。这是收益不确定，不是证明无收益；fixed 仍在同一 test 选 γ，且所有摘录都未给精确输出保证。用户 GPU 类型和 drafter 未指定，D-1/G-A 的外推也有条件。

精读队列（只占两篇）：
1. **P2 — deep_read**：核查修正后全开销、区间和 fixed 选择；决定是否值得投入 adaptive。
2. **P4 — deep_read**：核查 dev-tuned fixed 与高接受率代码场景，检查按 P1-v1 重实现的可比性；决定 fixed 已足够是否能解释目标现象。其 -1% 区间 [-4%, +2%] 不能证明 chat 无益。

P3 仅 **targeted_read**：+11% [+6%, +16%] 是 T-9/G-B 的正证据；共享作者、代码和 CHAT-500，不能算独立确认，是否继承计时问题未知。P2/P4 的宽区间相容且任务不同（scope_mismatch），没有确立的可比冲突。P1 **defer**（旧计时被修正）；P5 **exclude**（重复旧结果，无新实验）；P6 **defer**（恒定成本的统计类比）；P7 **verify_access**（abstract 缺关键设置）。

下一步诊断：先补查当前 decoding 与 adaptive γ 的精确性条件/证明，摘录不足以保证分布；随后在相同 T-7、chat 请求、drafter、GPU、batch=1 上，用独立 dev 调 fixed γ，在未用于调优的请求上配对比较。计入 head、rejection 后 KV-cache rebuild 及所有 draft/verify 时间，按接受率与成本比分层报告端到端 tokens/sec、区间和样本量。两个待分辨解释是：接受率/成本异质性确实给 adaptive 留出空间；或 fixed 已吸收收益，剩余差异来自噪声、选择与额外成本。前者预测某些预先定义层有稳定净增益；后者预测全开销下增益消失。预先定最小实用收益门槛；若区间上界也低于门槛，停止该目标下 adaptive 优先投入；区间仍宽则仅说明诊断未定论。

仅使用虚构离线包，全文不可得；未做网络检索、精确性验证或性能实验。该 Scout 不作新颖性或真实文献覆盖判断。
