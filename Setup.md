## 🚀 Setup and Installation Guide

Follow these steps to set up and run the Age Calculator application locally on your machine.

---

### ✅ Prerequisites
- Python **3.9+** installed
- Recommended: Use a **virtual environment (venv)** to manage project dependencies

---

### 📂 Step 1: Clone the Repository (or Save Files)

Create Project Directory:
```bash
mkdir age-calculator
cd age-calculator
```

Save the Application Code:  
Save your main application code (the Python script containing the `main(page: ft.Page)` function) as **`main.py`** inside this directory.

Save the Dependencies:  
Save the content of the `requirements.txt` Canvas into a file named **`requirements.txt`** in the same directory.

---

### ⚙️ Step 2: Set up the Environment

Create a Virtual Environment:
```bash
python -m venv .venv
```

Activate the Virtual Environment:

- **macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```

- **Windows (Command Prompt)**:
  ```bash
  .venv\Scripts\activate.bat
  ```

- **Windows (PowerShell)**:
  ```bash
  .venv\Scripts\Activate.ps1
  ```

Install Dependencies:
```bash
pip install -r requirements.txt
```

---

### ▶️ Step 3: Run the Application

The **Flet framework** includes a command-line interface (CLI) that allows for easy running and hot-reloading.

Run in a **native desktop window** (recommended):
```bash
flet run main.py
```

Run as a **web app** (in your default browser):
```bash
flet run --web main.py
```

👉 The application will start in **hot reload mode**, meaning any saved changes to `main.py` will automatically update the running app instance.

---

## ⚠️ Troubleshooting Common Issues

| Issue | Description | Solution |
|-------|-------------|----------|
| **`command not found: flet`** | Flet CLI is not in your system's PATH | Ensure you have activated the virtual environment (Step 2) before running `flet run` |
| **`ImportError: No module named 'dateutil'`** | Dependency installation failed or environment inactive | Run `pip install -r requirements.txt` again while the venv is active |
| **App won't update (Hot Reload)** | Changes not reflecting in running app | Make sure you’re using `flet run main.py`. If issue persists, stop app (`Ctrl+C`) and restart |
| **`page.update()` errors** | Runtime errors related to updating controls | If running as web app, check browser console for detailed error messages |

---

## 🛠️ Configuration Notes

Since this is a standalone **Flet** application, there are no separate config files. All settings are controlled in **`main.py`**:

- **Theme**:  
  Material You theme is set using:
  ```python
  page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
  ```
  Change `ft.Colors.DEEP_PURPLE` to another Flet color constant to customize.

- **Window Size**:  
  The application window size is fixed with:
  ```python
  page.window_width = 400
  page.window_height = 600
  ```
  Adjust values as needed.

---

✨ You’re all set! This guide gives you a clear path to running and testing your Age Calculator application.