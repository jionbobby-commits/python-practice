# Python 练习库

这是我用来记录 Python 学习过程与练习代码的个人仓库。当前重点：**函数、模块、面向对象编程和封装**。

- Python：3.14.3（项目虚拟环境 `.venv`）
- Git 分支：`main`
- 远程仓库：<https://github.com/jionbobby-commits/python-practice>
- 最近整理：2026-10-25，详见 [整理报告.md](整理报告.md)

> 这里保留的是学习过程，不是需要“看起来完美”的项目。很多 `exit*.py` 是当天的练习，文件名和代码都尽量保留原样；有错误的文件通常会保留，并在整理报告中记录。

## 快速开始

在仓库根目录打开 PowerShell：

```powershell
cd "D:\PYTHON练习"
$python = "D:\PYTHON练习\.venv\Scripts\python.exe"

# 最简单的冒烟测试
& $python main.py

# 运行一个普通练习（该练习会等待键盘输入）
& $python "字符串\age.py"
```

也可以先激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

如果 PowerShell 禁止运行激活脚本，不必修改系统策略，直接用上面的 `$python` 绝对路径即可。

## 目录说明

| 目录 | 内容 |
| --- | --- |
| `字符串/` | 早期基础练习：字符串切片、格式化、编码、条件、`for`/`while` 循环、BMI 等。目录名沿用当时课程，内容不只有字符串。 |
| `列表/` | 列表增删改查、排序、输入处理；`exit6.py` 是一道未完成且有语法错误的练习。 |
| `元组与字典/` | 元组、电话簿字典、成绩字典、字典推导式。 |
| `字典与集合/` | 字典遍历、集合交并差、输入去重。 |
| `数据类型转换/` | `int`、`float`、`str`、`eval`、`chr`/`ord` 等转换。注意其中用了 `eval`，只适合本地练习输入。 |
| `赋值和深浅拷贝/` | 集合、字典、排序与深浅拷贝阶段的综合小练习。 |
| `函数/` | 函数参数、作用域、`lambda`、递归、返回值和导入练习。 |
| `异常处理/` | `try/except`、主动抛出异常、输入校验练习。 |
| `模块/` | 自定义模块与包、`__init__.py`、从其他目录导入；保留原来的 `10-16`、`10-17` 日期目录以维持导入上下文。 |
| `面向对象/` | 类、对象、属性、方法、封装、`__str__`/`__add__`，以及学生管理、购物车、足球评分三个小项目。 |
| `综合项目/` | 不属于单一语法阶段的完整小项目：Streamlit 页面、AI 接口调用、爬虫。 |
| `学习笔记/` | 学习过程中的问答和概念笔记，目前有 `类与对象_自测.md`。 |
| `_待整理/` | 用途暂不确定或自动生成的文件，没有删除；说明见 [_待整理/README.md](_待整理/README.md)。 |
| `_整理备份/` | 2026-10-25 整理前的 ZIP、Git bundle 和操作记录，不提交 Git。恢复方法见 [_整理备份/README.md](_整理备份/README.md)。 |
| `main.py` | 最基础的 `print("Hello GitHub")` 冒烟测试。 |
| `.venv/` | Python 虚拟环境，约 480 MB。不要移动或提交；其中还有一个本地 `id.py` 练习，按安全规则未改动。 |
| `.idea/` | PyCharm 项目配置。只保留项目配置，临时工作区文件已由 `.gitignore` 忽略。 |
| `.git/` | Git 元数据，禁止手动修改。 |

## 各项目的运行方式

### 1. 普通练习脚本

在根目录直接运行完整路径即可：

```powershell
& $python "函数\exit1.py"
& $python "列表\school_work.py"
```

部分文件会调用 `input()`，需要在终端中手动输入。不要用“运行后立即关闭”的方式启动，否则会看到 `EOFError`。

### 2. 模块与包

这些脚本依赖“当前工作目录”，建议进入对应目录再运行：

```powershell
Push-Location "模块\10-16"
& $python main.py
Pop-Location

Push-Location "模块\10-17"
& $python main.py
Pop-Location

Push-Location "模块\10-17\day17"
& $python main.py
Pop-Location
```

`模块/10-17/main.py` 会同时导入同目录的 `calculator.py` 和 `类/book.py`；`day17/main.py` 使用 `tools` 包。保留这些目录结构，才能保持原来的导入关系。

### 3. Streamlit 页面

`01web.py` 和 `AI_friend.py` 使用相对路径 `./file/...`，`AI_friend.py` 还会把聊天记录写到 `sessions/`。因此要先进入应用目录：

```powershell
Push-Location "综合项目\Streamlit应用"
& $python -m streamlit run 01web.py
# 或
& $python -m streamlit run AI_friend.py
Pop-Location
```

- `01web.py`：图片展示与简单表单页面。
- `streamlit_test.py`：标题、副标题的最小页面。
- `AI_friend.py`：本地 AI 聊天页面。它连接本机 `http://localhost:11434/v1`，模型名为 `deepseek-r1:7b`，需要本机已启动 Ollama 并准备该模型；`api_key="ollama"` 只是本地占位值，不是真实密钥。页面能打开不等于模型服务已经可用。

### 4. DeepSeek 接口调用

```powershell
$env:DEEPSEEK_API_KEY = "在这里填写你自己的密钥"
& $python "综合项目\AI接口调用\deepseekai.py"
```

不要把真实密钥写进 `.py` 文件，也不要提交到 Git。该脚本会联网并可能产生 API 费用，本次整理没有实际调用。

### 5. 爬虫

```powershell
& $python "综合项目\爬虫\爬虫入门.py"
```

需要网络和已安装的 `requests`。`爬视频.py` 中的视频/音频 URL 和请求头目前为空，是未完成占位代码，不能直接运行；它还会在当前目录写出多媒体文件。

## 学习与检查说明

- 普通练习用 Python 3.14 做过语法解析和模拟输入测试；结果见整理报告。
- 项目没有使用 `pytest`。当前不建议为了练习引入复杂测试框架。
- `列表/exit6.py` 第 2 行尚未写完，不能编译。
- 三个早期文件有未使用的跨目录导入，直接运行会报 `ModuleNotFoundError`：`函数/exit5.py`、`模块/10-17/类/exit1.py`、`赋值和深浅拷贝/exit.py`。这些是整理前就存在的问题，本次没有改源代码，报告中给出了建议。
- `.venv` 中已经安装了 `streamlit`、`openai`、`requests`、`moviepy`；不需要为了让目录“完整”而重新安装依赖。

## Git 与上传 GitHub

本次整理后的文件移动默认**尚未提交**。建议先检查：

```powershell
git status --short
git diff --stat
```

确认无误后再提交：

```powershell
git add -A
git commit -m "整理 Python 学习目录并补充说明"
git push
```

注意：

1. `.gitignore` 只能阻止新文件被跟踪，**不会自动取消已经跟踪的历史文件**。仓库里目前仍有 2 个 `函数/__pycache__/*.pyc` 和部分 `.idea` 配置被 Git 跟踪。
2. 这些历史缓存不影响代码运行，但会让 GitHub 仓库不整洁。是否取消跟踪需要你确认，命令和说明写在整理报告中，本次没有替你执行。
3. 聊天记录示例 `综合项目/Streamlit应用/sessions/20261023_090123.json` 仍被 Git 跟踪；以后新生成的会话文件默认被忽略。
4. 上传前不要在公开仓库中放入 API 密钥、身份证号、真实聊天记录等隐私数据。

## 下一步建议

1. 先完成 `列表/exit6.py`，再把异常处理练习中的输入校验和空列表问题修好。
2. 学完函数后，给 `get_average`、`password_check` 等函数补上边界测试。
3. 继续封装练习时，尝试把“数据”和“操作数据的方法”放在同一个类里，并保持单文件项目能独立运行。
4. 熟悉 `from pathlib import Path`，以后处理文件路径时不要依赖启动目录。
5. 每完成一个阶段，在 `学习笔记/` 写一段“我学会了什么/还没搞懂什么”，比只堆代码更有帮助。
