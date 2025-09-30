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
    Se il file non esiste o non è leggibile, solleva un'eccezione.
    """
    if not file_path.endswith(".py"):
        raise ValueError(f"Il file specificato non sembra un file Python: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        print(f"[DEBUG] Codice letto correttamente da: {file_path}")
        return code
    except Exception as e:
        raise RuntimeError(f"Errore durante la lettura del file {file_path}: {e}")
