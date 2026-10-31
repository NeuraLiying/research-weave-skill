# 附件内检索、筛查与核查日志

日期：2026-10-31。运行范围：`/tmp/research-weave-forward-test`。唯一证据来源：[agent-feedback.md](input.initial.md)。全部研究为虚构测试材料。本轮不联网、不使用其他 skills、不修改 skill/repo/安装配置。

## 工作问题与约束

- 是否为冻结 M-1 的精确答案推理建设无工具修订循环？预算每题 2,000 全成本 tokens，基线等预算重采样。
- 会反转决定的未知：目标条件净收益是否稳定；C/D 反向的原因；工具反馈结果能否适用；论文数是否重复同一底层实验。
- 精读三篇：C、D、B；“精读”仅对应所供方法/结果节选，不冒称全文。A/G/E 是定点阅读或去重核查，F/H 不可充分评估。

## 实际来源读取与检索通道

先读取 `research-weave/SKILL.md`，再按任务读取 `evidence-method.md`、`contradictions.md`、`output-contract.md` 三份相关引用。父任务随后通知命题级收敛扩充，故仅重读 §4 与 proposition schema；没有读取评测 cases 或预期答案。没有借助其他技能。

以下“查询”均是**附件内人工审阅的工作问题**，不是声称执行了网络检索或每条都调用了字符串搜索。实际程序字符串搜索为 `rg -n '^## |Source identifier:|The researcher'` 对附件做清单/定位；也用 `sed` 重新打开 A–F 段落核查。

| 通道 | 实际问题/查询概念 | 读到的来源 | 结果与保留 |
|---|---|---|---|
| 清单 | A–H、年份、版本、来源标识、可见章节 | 附件全文 | 8项；6节选、1摘要、1元数据，均保留来源记录 |
| 历史及旧名称 | draft/critique/revise，创作偏好→精确答案，明确引用关系 | A §2/§4、B §3、C §2 | A→B 方法借入，A→C 评价边界；不声称世界首创 |
| 当前问题/评价 | frozen M-1，tool-free/intrinsic feedback，exact-answer，2000 all-in tokens，matched-budget resampling | B/C/D、F、H | C/D直接且冲突，B带工具边界；F缺可比条件，H无主张 |
| 反证/复制/重复计数 | failure、replication、implementation、result reuse | C §6、D §2/§5、E §3 | C负向、D正向；E三次确认均回到EXEC-400；C/D共享人群但不是复用结果 |
| 邻域机制 | selective measurement，information changes action，reliability | G §2/§4 | 仅类比；没有LLM证据或A/B/C引用G的证明 |
| 包内后向/前向线索 | B引A、C引A、D尝试C；后来的E/F/H是否解决C/D | 对应节选 | 有明确借入/挑战；无提供的后来解决。不曾访问完整参考文献表或真实引文索引 |

## 全池筛查与行动

| ID | 可用性/家庭 | 本轮行动 | 具体理由 |
|---|---|---|---|
| A | v1节选；家庭unknown | targeted_read | 操作祖先；创作偏好、120对、双倍预算，不是精确答案效果支持 |
| B | v2节选；EXEC-400 | deep_read #3 | +8pp[4,12]、400对、预算公平；带工具，建立条件边界 |
| C | v1节选；REASON-C | deep_read #1 | 目标设置−6pp[−10,−2]、200对；最强直接负证据 |
| D | v1节选；REASON-D | deep_read #2 | 名义设置对齐却+5pp[2,8]；C/D共享REASON-200，新生成输出；代码/逐题预测缺 |
| E | v1合成节选；EXEC-400 | exclude独立效果资格，保留去重记录 | B、预印本、转载不是三实验；没有新结果 |
| F | 摘要；版本/家庭unknown | verify_access，未能完成 | 模型、数据、分母、metric、预算、选择、区间等缺；高引用未经核验 |
| G | v1概念节选；家庭unknown | targeted_read | 信息可靠性的桥接类比，不是机制证实 |
| H | 只有标题/年份；版本/家庭unknown | verify_access，未能完成 | 连摘要也无，不能提取结果或判断自适应方案是否匹配目标 |

## 访问失败、边界及未执行通道

- 不是发生了网络故障：用户限定只用附件，因此没有尝试任何外部URL、搜索、下载或新来源修复。
- F 的全文/方法与 H 的摘要/全文不可得，无法完成潜在重要来源核验；D 的代码/逐题预测不可得，C/D实际R/E正文、选择器和快照等也未提供。
- 无实际当前研究/独立复现检索，无完整前向引文查询，无更正/撤稿核查。只报告包内没有解决，不能称领域中未解决。
- 未发现重要 seed 被字符串/年份筛选漏掉；8项全部盘点。没有日期截止过滤基础工作。
- A文字称“包内最早”，但G年份2008早于A2019，存在包内年代措辞问题。修复是仅把A称作最早明确循环操作的分支，不编造G→A影响关系。
- 支持计数按命题分离：D对P1是一篇/一个已知族，C为最强反证；B对工具命题是一篇/一个族；E仅额外转述。C/D不同结果族不能证明独立实施，C/D整体独立关系保持unknown；最终P1只有一个支持贡献D，计1，P2无直接全称支持，计0。没有多篇可信独立直接证据足以形成收敛。

## 结构检查与人工复核

- 生成 `evidence.json` 后运行 bundled `check_evidence.py`。
- 首轮9个结构错误：checker要求 `tension.comparison`、`resolution_search` 和 `test.predictions` 为字符串；output-contract没有显式标明这些字段类型，本轮最初用了结构化对象/列表。将这些内容无损转成文本字段，保留所有对齐维度和区分性预测。
- 首次直接执行含长中文行的本地生成脚本，Python 3.9.6误报Non-UTF-8，严格UTF-8解码与compile均成功；用显式UTF-8 read_text后compile执行完成。此问题未涉及来源或skill文件修改。
- 人工重开附件第7–29行：A历史、B/C/D数值/预算/区间、C/D对齐条件与缺失，E去重排除，F摘要不足逐一核查；G/H在首次全包审阅中核查。
- checker最终结果另存 `checker.txt`；其cautions若只是unknown family，不为消除警告而编造独立性。checker不验证source truth。

停止原因：筛完附件8项且三篇精读预算用尽；没有观察到两轮扩展饱和，也没有系统穷尽真实文献。剩余盲点以F/H全文、C/D原始工件、独立题集/团队、更新模型和包外后续解决为主。

## 冷启动语义纠错（不得隐去）

父任务在结果复核时指出：初稿P2为全称“所有运行均失败”，却把CC局部负效应列入supporting。这是量词/作用域迁移错误，结构checker无法检测。现已把CC移至candidate，supporting清空；D正向局部结果保留为该全称断言的反证。P1另从“可靠优于”收窄到目标平均效果，可靠性仍未建立。

还发现独立贡献计数口径误读：最初P3写0，指的是没有额外独立复现；规范字段实际含原始实验本身。现P3写1（B原始贡献），另存额外独立复现0。P1支持集合仅D也计1，且明确D与反证C共享人群/实施关系未知；P2/P4/P5无直接支持，计0。不会因消除警告而把不同族名当独立性证明。本轮有语义纠错，不能声称未经人工帮助即clean pass。

最终结构检查：0 errors，4 cautions（A/F/G/H evidence independence not established）。保留unknown，没有伪造证据家族。父任务后来收紧了skill的量词适用性、独立贡献定义及文本字段类型，并修正原fixture的A年代措辞；这些属于本次行为测试暴露的问题修复。本报告记录的是修改前实际读到的输入，不把后来的修订冒充初始来源；父任务已另存初始输入。
