import os
from profiler import get_user_profile, get_user_user_prompt, read_code
from generator import generate_comments
from generator import sentiment_analysis
from generator import profile_analysis

def main():
    # Chiedi percorso file o cartella
    file_path = input("Inserisci il percorso del file o della cartella da analizzare:\n> ").strip()

    # Se è una cartella, cerca i file .py e lascia scegliere
    if os.path.isdir(file_path):
        py_files = [f for f in os.listdir(file_path) if f.endswith(".py")]
        if not py_files:
            print("❌ Nessun file .py trovato nella cartella.")
            return

        print("📂 Sono stati trovati i seguenti file Python:")
        for idx, fname in enumerate(py_files, start=1):
            print(f"  {idx}. {fname}")

        while True:
            try:
                choice = int(input("Seleziona il numero del file da analizzare: "))
                if 1 <= choice <= len(py_files):
                    file_path = os.path.join(file_path, py_files[choice - 1])
                    break
                else:
                    print("❌ Scelta non valida. Riprova.")
            except ValueError:
                print("❌ Inserisci un numero valido.")

    # Leggi codice da analizzare
    code = read_code(file_path)

    # Prompt personalizzato dell'utente
    user_prompt = get_user_user_prompt()

    #Esegue analisi sul tono del prompt
    user_tone = sentiment_analysis(user_prompt)
    
    print("Analisi del sentimento dell'utente", user_tone)

    # Profilazione analitico | olistico
    # cognitive_style = get_user_profile()
    # print(f"Profilo selezionato: {cognitive_style}")
    
    cognitive_style = profile_analysis(user_prompt)
    print(f"Profilo rilevato: {cognitive_style}")
  
    # Generazione commenti con l'ai
    commented_code = generate_comments(code, cognitive_style, user_prompt, user_tone)

    # Salva il risultato
    output_path = file_path.replace(".py", "_commentato.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(commented_code)

    print(f"✅ Codice commentato salvato in {output_path}")

if __name__ == "__main__":
    main()
