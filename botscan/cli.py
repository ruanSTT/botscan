import argparse
import os
from botscan.linter import format_code, lint_code


def main():
    parser = argparse.ArgumentParser(
        description="Linting e formatação para automações RPA com Python"
    )
    parser.add_argument("path", nargs="?", default=".", help="Caminho do arquivo ou diretório")
    parser.add_argument("--lint", action="store_true", help="Executa apenas o Pylint (com regras RPA)")
    parser.add_argument("--format", action="store_true", help="Executa apenas o Black")
    parser.add_argument("--lang", choices=["pt-br", "en"], default="en", help="Idioma das mensagens (pt-br ou en)")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Caminho não encontrado: {args.path}")
        return

    if args.lint:
        print("Executando Pylint (com regras RPA)...")
        lint_code(args.path, lang=args.lang)
    elif args.format:
        print("Formatando com Black...")
        format_code(args.path)
    else:
        print("Formatando com Black...")
        format_code(args.path)
        print("\n Executando Pylint (com regras RPA)...")
        lint_code(args.path, lang=args.lang)


if __name__ == "__main__":
    main()