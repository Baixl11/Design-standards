# Development Guidelines Skill Suite

这是一套面向 AI Coding 的工程治理 Skills，集中解决两个问题：

1. 新项目缺少可执行约束，导致技术栈、目录、数据所有权、接口和测试策略各自为政。
2. 需求变更只修改当前文件，遗漏契约、数据、调用方、迁移、测试、发布和回滚。

根目录是源码与分发仓库，不是单个 Skill。安装时将各 Skill 目录平铺到 Codex Skills 目录；`README.md`、catalog、evals 和维护脚本不会被安装。

## 执行阶段

| 阶段 | Skill | 何时使用 |
|---|---|---|
| 技术决策 | `ai-dev-tech-stack-orchestrator` | 用户明确要求技术选型、架构比较或新项目工程规划时 |
| 技术栈指导 | `*-standard` | 已明确使用对应框架，需要初始化、修改或审查工程规范时 |
| 修改前 | `change-impact-analysis` | existing-project 或 greenfield 开始实施修改前；`local` 使用轻量清单，其余模式按风险扩展 |
| 修改后 | `data-consistency-regression-test` | 任何实际修改完成后，按同一风险模式核对 diff、测试、数据传播和发布风险 |

catalog 用 `standard_options` 表示 orchestrator 必须七选一的技术标准，用 `workflow_companions` 表示阶段性交接。它们都是显式工作流关系，不是假设运行时一定能自动加载；缺少 companion 时，当前 Skill 执行最小检查并标记 `degraded`。

## 触发优先级

1. 用户只要求技术选型或架构比较：使用 orchestrator。
2. 用户已经指定技术栈并要求开发：使用对应技术栈 Skill，不重复做选型。
3. Next.js 项目优先使用 Next.js Skill，不同时套用 React SPA Skill。
4. Electron renderer 仍由 Electron Skill 统筹；只在明确需要 renderer 深入规则时再参考 React/Vue Skill。
5. `local` 修改仍做改前/改后最小检查，但不强制生成完整影响报告；按风险升级检查深度。

## 当前 Skills

- `ai-dev-tech-stack-orchestrator`
- `react-typescript-web-standard`
- `vue-typescript-web-standard`
- `nextjs-fullstack-standard`
- `electron-desktop-standard`
- `flutter-mobile-standard`
- `fastapi-backend-standard`
- `springboot-backend-standard`
- `change-impact-analysis`
- `data-consistency-regression-test`

## 安装

默认安装到 `${CODEX_HOME}/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。

```bash
./install_to_target.sh
./install_to_target.sh /custom/skills/path
./install_to_target.sh /custom/skills/path --dry-run
./install_to_target.sh /custom/skills/path --update
./install_to_target.sh /custom/skills/path --update --force
```

Windows PowerShell：

```powershell
.\install_to_target.ps1
.\install_to_target.ps1 -Target C:\custom\skills
.\install_to_target.ps1 -Target C:\custom\skills -DryRun
.\install_to_target.ps1 -Target C:\custom\skills -Update
.\install_to_target.ps1 -Target C:\custom\skills -Update -Force
```

安装器先运行套件校验，再严格按 catalog 安装；不会分发未登记目录。默认跳过已存在的 Skill。`--update` / `-Update` 只替换由安装 manifest 管理且未被修改的完整 Skill 目录，从而清除旧版本残留文件；检测到本地修改、未知来源或版本降级时拒绝覆盖。

`--force` / `-Force` 必须与 update 一起使用。强制更新前会把旧目录移动到目标 Skills 目录的同级备份区，不直接删除。安装使用同文件系统 staging、并发锁、文件哈希和失败回滚；目标内的符号链接/Junction、普通同名文件以及 source/target 路径重叠都会被拒绝。目标根的 `.development-guidelines-install.json` 记录受管版本和 SHA-256。

## 维护校验

```powershell
python -B -X utf8 scripts/validate_suite.py .
python -B -X utf8 -m unittest discover -s scripts -p "test_*.py" -v
```

`evals/cases.json` 是前向测试契约，不把静态字段校验冒充行为测试。执行独立 Skill 场景后，将原始回复、初始路由、阶段性交接、模式、状态和逐条证据记录为 JSON，再运行：

```powershell
python -B -X utf8 scripts/evaluate_outputs.py path/to/captured-responses.json
```

使用 `--allow-partial` 可在迭代中只检查部分场景；发布判断应覆盖全部场景。每条 assertion 必须对应 case 的 `must` 或 `must_not`，包含布尔结果和可审计证据。

维护原则：

- 技术栈规则先检查项目实际版本和既有约定。
- 将推荐方案、已观察事实和强制安全约束分开。
- 不用文档数量衡量规范完整度。
- 测试结果必须包含实际命令、退出码和未运行原因。
- catalog、frontmatter、agents 元数据、模式枚举和 companion 名称必须保持一致。
