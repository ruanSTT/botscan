import subprocess


TRANSLATIONS = {
    "W9904": {
        "pt-br": "Bloco 'except' genérico detectado — especifique o tipo de exceção.",
        "en": "Generic 'except' block detected — please specify the exception type.",
    },
    #TODO: add mais mensagens personalizadas
}


def lint_code(path, lang="en"):
    result = subprocess.run(
        ["pylint", path, "--disable=all", "--enable=W9904"],
        capture_output=True, text=True
    )

    output = result.stdout

    for line in output.splitlines():
        if "W9904" in line:
            print("🔧", TRANSLATIONS["W9904"][lang])
        else:
            print(line)