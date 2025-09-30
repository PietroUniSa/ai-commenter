def get_user_user_prompt() -> str:
    """
    Chiede all'utente un'introduzione personalizzata (emotiva/personale).
    Se non viene fornita, ritorna stringa vuota.
    """
    intro = input("Vuoi aggiungere un prompt personalizzato (può includere emozioni o tono)?\n> ").strip()
    return intro