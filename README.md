# 🧮 Advanced Calculator

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF8C00?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)

> A scientific calculator built **three times** — as a Python CLI, a Tkinter desktop app, and a modern web app. Same mathematical engine, three completely different implementations across three platforms.

---

## 🧭 Choose Your Version

| | 🖥️ CLI (V1) | 🪟 Desktop (V2) | 🌐 Web (V3) |
|---|---|---|---|
| **Stack** | Python + `math` | Python + Tkinter | HTML + CSS + JavaScript |
| **Run Requirement** | Python only | Python only | Just a browser |
| **Interface** | Terminal menu | Dark GUI window | Dark/light web app |
| **History** | In-session list | None | Persistent via `localStorage` |
| **Scientific Functions** | sin, cos, tan, sqrt, log, factorial, nth root, percentage, exponential | sin, cos, tan, sqrt, log, factorial | sin, cos, tan, sqrt, log, π |
| **Safe Eval** | ✅ `safe_eval()` with allowlist | ✅ `safe_eval()` with allowlist | ✅ `Function()` sandbox |
| **Keyboard Support** | ❌ | ❌ | ✅ Full keyboard input |
| **Theme Toggle** | ❌ | ❌ | ✅ Light / Dark (persistent) |
| **Docs** | [CLI Documentation →](./desktop_version/README.md) | [Desktop Documentation →](./desktop_version/README.md) | [Web Documentation →](./web_version/README.md) |

---

## 🆕 Latest Update — Web Version v3.2

| # | Type | Change |
|---|---|---|
| ✨ | **Added** | Complete Light / Dark theme system using CSS variables for centralized theming |
| ✨ | **Added** | Persistent theme preference via `localStorage` — survives page reloads |
| ✨ | **Added** | Functional theme toggle button wired to the new theming system |
| 🔧 | **Improved** | All styling refactored to use CSS theme variables — future customization requires editing one block |

---

## 📋 Web Version Release History

| Version | Highlights |
|---|---|
| **v3.0** | Initial web release — dark UI, scientific functions, persistent history, responsive layout |
| **v3.1** | Full keyboard support (`Enter`, `Backspace`, `Delete`, `Escape`), `data-key` button attributes |
| **v3.2** | Light / Dark theme system, CSS variables, persistent theme via `localStorage`, functional toggle |

---

## 📋 Version Timeline

| Version | Platform | Highlights |
|---|---|---|
| **V1 — CLI** | Python Terminal | 12-operation menu, full scientific functions, `safe_eval()`, in-session history |
| **V2 — Desktop** | Python + Tkinter | Dark GUI, button grid, scientific function panel, popup error handling |
| **V3 — Web** | HTML / CSS / JS | Keyboard support, persistent history, light/dark theme toggle, responsive layout |

---

## ✨ Shared Features (All Versions)

- ➕ **Basic Arithmetic** — addition, subtraction, multiplication, division
- 📐 **Trigonometry** — sin, cos, tan (degree-based input)
- √ **Scientific Functions** — square root, logarithm, factorial
- 🔒 **Safe Expression Evaluation** — no arbitrary code execution
- ❌ **Error Handling** — divide by zero, invalid log inputs, malformed expressions

---

## 🗂️ Project Structure

```
advanced-calculator/
│
├── README.md                         # 📍 You are here
├── LICENSE
├── .gitignore
│
├── desktop_version/
│   ├── calculator.py                 # 🖥️  V1 — Python CLI calculator
│   ├── calculator_gui.py             # 🪟 V2 — Tkinter desktop GUI
│   └── requirements.txt             # 📦 Python dependencies
│
└── web_version/
    ├── index.html                    # 🌐 V3 — Web calculator layout
    ├── style.css                     # 🎨 V3 — CSS variables, light/dark theme, responsive grid
    └── script.js                     # ⚙️  V3 — Calculation engine, history, keyboard, theme toggle
```

---

## 🔢 Supported Operations

| Operation | CLI | Desktop | Web |
|---|:---:|:---:|:---:|
| Addition / Subtraction / Multiply / Divide | ✅ | ✅ | ✅ |
| Percentage `%` | ✅ | ✅ | ✅ |
| Power `pow(x, y)` | ✅ | ✅ | ✅ |
| Square Root `sqrt()` | ✅ | ✅ | ✅ |
| Logarithm `log()` | ✅ | ✅ | ✅ |
| Trigonometry — sin, cos, tan | ✅ | ✅ | ✅ |
| Factorial `factorial()` | ✅ | ✅ | ❌ |
| Nth Root | ✅ | ❌ | ❌ |
| Exponential `e^x` | ✅ | ❌ | ❌ |
| π constant | ❌ | ❌ | ✅ |
| Custom expression eval | ✅ | ✅ | ✅ |
| Persistent history | ❌ | ❌ | ✅ |
| Keyboard input | ❌ | ❌ | ✅ |
| Theme toggle (persistent) | ❌ | ❌ | ✅ |

---

## ⚡ Quick Start

### CLI Version
```bash
cd desktop_version
python calculator.py
```

### Desktop Version
```bash
cd desktop_version
pip install -r requirements.txt
python calculator_gui.py
```

### Web Version
```bash
cd web_version
# No install needed — just open in browser
open index.html
```

---

## 🔒 Safe Evaluation — All Versions

All three versions use a sandboxed expression evaluator — no raw `eval()` on user input.

**Python (V1 & V2):**
```python
# Only math functions and safe builtins are allowed
allowed_names = {name: obj for name, obj in math.__dict__.items()
                 if not name.startswith("__")}
return eval(expression, {"__builtins__": None}, allowed_names)
```

**Web (V3):**
```javascript
// Function() constructor used as a controlled sandbox
return Function("sin", "cos", "tan", "sqrt", "log",
    "return " + expression)(sin, cos, tan, sqrt, log);
```

---

## 🔮 Planned Features

- [ ] 📊 Graph plotting (matplotlib / Chart.js)
- [ ] 💾 Memory functions (M+, M−, MR, MC)
- [ ] 📱 Mobile-responsive web layout
- [ ] 🔢 Scientific notation support
- [ ] 📐 Unit converter integration

---

## 👨‍💻 Author

<div align="center">

**Yash Kumar Singh**

[![GitHub](https://img.shields.io/badge/GitHub-caffineblud-181717?style=flat-square&logo=github)](https://github.com/caffineblud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Yash_Kumar_Singh-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/yash-kumar-singh-8a4b193b1)

⭐ If you like this project, consider giving it a star.

</div>