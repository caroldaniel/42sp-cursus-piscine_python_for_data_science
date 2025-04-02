# ft_package 🐍📦

This repository contains `ft_package`, a custom Python package built as part of the Piscine Python for Data Science - Starting module.

It demonstrates how to:
- Create a Python package from scratch
- Build and distribute it using `setuptools`
- Install it via `tar.gz` and `.whl` files
- Test it with your own scripts
- Manage the entire lifecycle with an interactive CLI tool

---

## 📁 Repository Structure

```
.
├── ft_package/            # Source package (your Python module lives here)
│   ├── __init__.py        # Initializes the package
│   └── module.py          # Your custom logic (e.g., ft_filter, etc.)
│
├── test/
│   └── test.py            # Script to test package functionality
│
├── manage.sh              # Interactive CLI for build/install/test/uninstall
├── setup.py               # Setup file for packaging and distribution
├── pyproject.toml         # Optional: builds & dependencies (PEP 517/518)
├── MANIFEST.in            # Include extra files in the package
├── LICENSE                # MIT License
└── README.md              # You're here!
```

---

## 🚀 Getting Started


## 🛠 Interactive CLI: `manage.sh`

Instead of running many individual commands, use the interactive script:

```bash
chmod +x manage.sh
./manage.sh
```

### 🔄 Menu Options:

```
1. Build package
2. Install package (.tar.gz or .whl)
3. Run tests (with output logged to test_log.txt)
4. Uninstall package
5. Show package info
6. Clean build files
7. Exit
```

---

## 🧪 Running Tests Manually

You can also run tests directly:

```bash
python3 test/test.py
```

> All test output is logged to `test_log.txt` via the CLI script.

---

## 📦 Installing the Package Manually

If you want to skip the interactive script:

```bash
# Build
python3 setup.py sdist bdist_wheel

# Install from .tar.gz
pip install dist/ft_package-0.0.1.tar.gz

# Or install from .whl
pip install dist/ft_package-0.0.1-py3-none-any.whl
```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## ✨ Credits

Built for the Piscine Python for Data Science @ 42SP  
Maintained by cado-car
