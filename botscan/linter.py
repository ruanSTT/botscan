from pylint.lint import Run
from pylint.reporters.text import TextReporter
from io import StringIO


TRANSLATIONS = {
    "W9904": {
        "pt-br": "Bloco 'except' genérico detectado — especifique o tipo de exceção.",
        "en": "Generic 'except' block detected — please specify the exception type.",
    },
    "W9901": {
        "pt-br": "Uso de time.sleep() sem justificativa em comentário.",
        "en": "Use of time.sleep() without comment explanation.",
    },
    "W9902": {
        "pt-br": "Uso de caminho hardcoded detectado.",
        "en": "Hardcoded path detected.",
    },
    "W9903": {
        "pt-br": "Uso de print() em vez de logging.",
        "en": "Use of print() instead of logging.",
    },
}

DOC_LINKS = {
    "W9901": "https://docs.python.org/3/library/time.html#time.sleep",
    "W9902": "https://peps.python.org/pep-0517/#file-paths",
    "W9903": "https://docs.python.org/3/library/functions.html#print",
    "W9904": "https://docs.python.org/3/tutorial/errors.html#handling-exceptions",
}


def append_doc_link(message: str, code: str) -> str:
    link = DOC_LINKS.get(code)
    if link:
        return f"{message} (📚 More info: {link})"
    return message


def lint_code(path: str, lang: str = "en"):
    """Executa o Pylint com o plugin botscan e imprime mensagens traduzidas."""
    buffer = StringIO()
    reporter = TextReporter(output=buffer)

    args = [
        "--load-plugins=botscan",
        "--disable=all",
        "--enable=W9901,W9902,W9903,W9904",
        path,
    ]

    Run(args, reporter=reporter, do_exit=False)

    output = buffer.getvalue()

    for line in output.splitlines():
        for code in TRANSLATIONS:
            if code in line:
                msg = TRANSLATIONS[code][lang]
                print("🔧", append_doc_link(msg, code))
                break
        else:
            print(line)