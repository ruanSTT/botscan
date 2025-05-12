from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
import astroid
import ast


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
            "Bloco 'except' genérico detectado — especifique o tipo de exceção como %s (doc: https://docs.python.org/3/tutorial/errors.html#handling-exceptions)",
            "generic-except",
            "Evite capturar todas as exceções — use tipos específicos como FileNotFoundError, ValueError, etc.",
        ),
    }


    def visit_tryexcept(self, node):
        for handler in node.handlers:
            if handler.type is None or (
                isinstance(handler.type, astroid.Name) and handler.type.name == "Exception"
            ):
                suggestion = self.suggest_specific_exception(node.body)
                self.add_message("generic-except", node=handler, args=(suggestion,))


    def suggest_specific_exception(self, body):
        for stmt in body:
            try:
                raw_ast = ast.parse(stmt.as_string())
            except Exception:
                continue

            for sub in ast.walk(raw_ast):
                if isinstance(sub, ast.Call):
                    func_name = getattr(sub.func, 'id', None)
                    if func_name in ("int", "float", "str"):
                        return "ValueError"
                    elif func_name in ("open", "read", "write"):
                        return "IOError"
                elif isinstance(sub, ast.With):
                    return "IOError"
                elif isinstance(sub, ast.Import):
                    return "ImportError"

        return "ValueError or RuntimeError"


    def visit_call(self, node):
        if isinstance(node.func, astroid.Attribute):
            if node.func.attrname == "sleep":
                lineno = node.lineno
                previous_line = node.root().file_lines[lineno - 2].strip()
                while lineno > 0 and not previous_line.startswith("#"):
                    lineno -= 1
                    previous_line = node.root().file_lines[lineno - 2].strip()

                if not previous_line.startswith("#"):
                    self.add_message("sleep-without-comment", node=node)

        if isinstance(node.func, astroid.Name):
            if node.func.name == "print":
                self.add_message("print-used", node=node)


    def visit_const(self, node):
        if isinstance(node.value, str) and "C:\\" in node.value:
            self.add_message("hardcoded-path", node=node)


def register(linter):
    linter.register_checker(RPAStyleChecker(linter))