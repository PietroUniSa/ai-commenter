import os
from profiler import get_user_user_prompt
from generator import generate_code
from comparator import evaluate_code
from generator import sentiment_analysis

def _next_sequential_filename(directory: str, base: str = "generated_code") -> str:
    """
    Return a path like generated_code1.py, generated_code2.py ... in directory,
    picking the first filename that does not yet exist.
    """
    i = 1
    while True:
        candidate = f"{base}{i}"
        full_path = os.path.join(directory, candidate)
        if not os.path.exists(full_path):
            return full_path
        i += 1


def main():
    # Chiedi percorso file o cartella
    file_path = input("Inserisci il percorso di salvataggio:\n> ").strip()

    # Determina directory di output
    if not file_path:
        print("Percorso vuoto: uso la cartella corrente.")
        output_dir = os.getcwd()
    elif os.path.isdir(file_path):
        output_dir = file_path
    else:
        # Se è un file (o non esiste ancora), usa la directory padre; se non c'è, usa cwd
        parent = os.path.dirname(file_path)
        output_dir = parent if parent else os.getcwd()
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)

    # Prompt personalizzato dell'utente
    user_prompt = get_user_user_prompt()

    # Esegue analisi sul tono del prompt
    user_tone = sentiment_analysis(user_prompt)
    print("Analisi del sentimento dell'utente", user_tone)

    # Generazione codice con l'AI
    generated_code = generate_code(user_prompt, user_tone)
    
    response = generated_code[0].choices[0].message.content.strip()
    response_emotion = generated_code[1].choices[0].message.content.strip()
    
    # File sequenziale
    output_path = _next_sequential_filename(output_dir)

    with open(output_path+".py", "w", encoding="utf-8") as f:
        f.write(response)

    with open(output_path+"_emotion.py", "w", encoding="utf-8") as f:
        f.write(response_emotion)

    print(f"✅ Codice salvato in {output_path}")

    # Confronta subito i due file appena generati
    file1 = output_path + ".py"
    file2 = output_path + "_emotion.py"

    result = evaluate_code(file1, file2)
    print("\n=== Valutazione GPT-4o ===")
    print(result)


if __name__ == "__main__":
    main()
