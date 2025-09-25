# analyzer.py
import ast

class FunctionInfoVisitor(ast.NodeVisitor):
    """
    Visitatore dell'AST che raccoglie informazioni sulle funzioni
    (nome, argomenti, linee di inizio/fine, return).
    """
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        info = {
            "nome": node.name,
            "argomenti": [a.arg for a in node.args.args],
            "lineno": node.lineno,
            "end_lineno": getattr(node, "end_lineno", node.lineno),
            "return_lines": [],
        }

        # Trova le istruzioni 'return' nella funzione
        for n in ast.walk(node):
            if isinstance(n, ast.Return) and hasattr(n, "lineno"):
                info["return_lines"].append(n.lineno)

        self.functions.append(info)
        self.generic_visit(node)

def analyze_code(code: str):
    """
    Analizza il codice Python e ritorna un riassunto
    con le informazioni principali delle funzioni trovate.
    """
    tree = ast.parse(code)
    visitor = FunctionInfoVisitor()
    visitor.visit(tree)
    return visitor.functions

if __name__ == "__main__":
    # Test veloce: analizza il file di esempio
    with open("examples/esempio.py", "r", encoding="utf-8") as f:
        codice = f.read()
    summary = analyze_code(codice)
    print("Funzioni trovate:", summary)
