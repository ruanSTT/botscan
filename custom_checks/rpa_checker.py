from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
import astroid


class RPAStyleChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "botscan"
    priority = -1
    msgs = {
        "W9901": (
            "Uso de time.sleep() sem justificativa em comentário",
            "sleep-without-comment",
            "Evite sleeps sem explicar o motivo (RPA pode travar sem isso).",
        ),
        "W9902": (
            "Uso de caminho hardcoded detectado",
            "hardcoded-path",
            "Evite usar caminhos fixos. Use variáveis de ambiente ou pathlib.",
        ),
        "W9903": (
            "Uso de print() em vez de logging",
            "print-used",
            "Substitua print() por logging para melhor rastreabilidade.",
        ),

        "W9904": (
        "Bloco 'except' genérico detectado — especifique o tipo de exceção",
        "generic-except",
        "Evite capturar todas as exceções — use tipos específicos como FileNotFoundError, ValueError, etc.",
    ),
    }


    def visit_tryexcept(self, node):
        for handler in node.handlers:
            if handler.type is None:
                self.add_message("W9904", node=handler)


    def visit_call(self, node):
        if isinstance(node.func, astroid.Attribute):
            if node.func.attrname == "sleep":
                lineno = node.lineno
                prev = node.root().file_lines[lineno - 2].strip()

                if not prev.startswith("#"):
                    self.add_message("sleep-without-comment", node=node)
                
                if node.func.name == "sleep":
                    self.add_message("sleep-without-comment", node=node)
                    print("🔗 Sugestão: Use WebDriverWait (https://www.selenium.dev/documentation/webdriver/waits/)")


        if isinstance(node.func, astroid.Name):
            if node.func.name == "print":
                self.add_message("print-used", node=node)


    def visit_const(self, node):
        if isinstance(node.value, str) and "C:\\" in node.value:
            self.add_message("hardcoded-path", node=node)


def register(linter):
    linter.register_checker(RPAStyleChecker(linter))