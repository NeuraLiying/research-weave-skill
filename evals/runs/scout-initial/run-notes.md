本次为有界行为 sanity test；仅用虚构离线包，无网络、未读测试/评审反馈/旧输出/预期答案，未改 skill 或仓库。

实际加载的 skill 资源：
- ../../../skills/research-weave/SKILL.md
- ../../../skills/research-weave/references/evidence-method.md
- ../../../skills/research-weave/references/contradictions.md
- ../../../skills/research-weave/references/output-contract.md（首次 checker 提示结构错误后，为确认合法字段/枚举读取）

实际运行：scripts/check_evidence.py；最终 0 errors, 0 cautions。已重新打开原始包核对 P2/P4、P3 主结论及 deferred P1/P6；结构检查不认证语义、独立性或覆盖率。

实际歧义：
- 用户只给同一 GPU，未指定 GPU 类型或 drafter；故不默认等同 P2 的 G-A/D-1。
- 包中没有精确性条件/证明、P3/P4 全部计时项和 P4 重实现细节；不能替它们补全，也不能据代码共用断定继承 bug。
- 只有摘录而非全文；deep_read 是预算内建议队列，并非已完成两篇全文精读。
- SKILL 的 compact 说明写 family、interpretation fields，未列确切字段名/枚举。最初使用 family、abstract_only、synthesis/conceptual、lead 和顶层 author_interpretation/analyst_inference；checker 拒绝或提醒后，output-contract 明确 evidence_family、abstract、interpretive/theoretical、evaluation 及 evidence 内的 authors_interpretation/analyst_inference。已按合同修复；无未解决结构错误。

本次不主张比较有效性、token 节省或真实文献完整性。
