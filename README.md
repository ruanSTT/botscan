# botscan-rpa

> A specialized linter for RPA automation with Python, using [Black](https://black.readthedocs.io/) and [Pylint](https://pylint.readthedocs.io/) with smart checks focused on process robotics.

---

## Overview

**botscan-rpa** is a command-line tool that enforces good coding practices for Python automation scripts, especially for those developing RPA with libraries like `pywinauto`, `botcity`, `uiautomation`, and others.

It uses:

- **Pylint==3.1.0** to detect style issues and potential bugs.
- **Black==24.3.0** to automatically format code.
- 🛡️ Custom rules for automation:
  - Prevents uncontrolled use of `print()`.
  - Detects `time.sleep()` without explanation.
  - Warns about hardcoded paths like `C:\\Users\\...`.
  - Identifies dangerous generic `try/except` blocks.

---

## Installation

Clone the repository and install it with:

```bash
git clone https://github.com/ruan-stt/botscan-rpa.git
cd botscan-rpa
pip install -e .