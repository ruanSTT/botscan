# botscan-rpa

> Linter especializado para automações RPA com Python, usando [Black](https://black.readthedocs.io/) e [Pylint](https://pylint.readthedocs.io/) com verificações inteligentes voltadas à robótica de processos.

---

## Visão Geral

**botscan-rpa** é uma ferramenta de linha de comando que aplica boas práticas de codificação para scripts de automação em Python, especialmente para quem desenvolve RPA com bibliotecas como `pywinauto`, `botcity`, `uiautomation`, entre outras.

Ela usa:

- **Pylint==3.1.0** para detectar problemas no estilo e possíveis bugs.
- **Black==24.3.0** para formatar automaticamente o código.
- 🛡️ Regras customizadas voltadas a automações:
  - Evita `print()` sem controle.
  - Detecta `time.sleep()` sem explicação.
  - Alerta sobre caminhos hardcoded como `C:\\Users\\...`.
  - Identifica `try/except` genéricos perigosos.

---

## Instalação

Clone o repositório e instale com:

```bash
git clone https://github.com/ruan-stt/botscan-rpa.git
cd botscan-rpa
pip install -e .