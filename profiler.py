def get_user_profile() -> str:
    """
    Chiede allo sviluppatore lo stile preferito:
    - Analitico (commenti dettagliati riga per riga)
    - Olistico (docstring e pochi commenti sintetici)
    """
    ans = input("Preferisci spiegazioni passo-passo (A) o sintetiche (O)? ").strip().lower()
    return "analitico" if ans.startswith("a") else "olistico"


def get_user_user_prompt() -> str:
    """
    Chiede all'utente un'introduzione personalizzata (emotiva/personale).
    Se non viene fornita, ritorna stringa vuota.
    """
    intro = input("Vuoi aggiungere un prompt personalizzato (può includere emozioni o tono)?\n> ").strip()
    return intro


def read_code(file_path: str) -> str:
    """
    Legge il contenuto di un file Python e lo restituisce come stringa.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
