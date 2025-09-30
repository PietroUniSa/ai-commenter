import os
from profiler import get_user_user_prompt
from generator import generate_code, sentiment_analysis, setup_generator_logger
from logger_config import setup_module_logger, suppress_external_logs
import logging
import subprocess
import sys




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
        output_dir = os.path.join(os.getcwd(), "examples")
    elif os.path.isdir(file_path):
        output_dir = file_path
    else:
        # Se è un file (o non esiste ancora), usa la directory padre; se non c'è, usa cwd
        output_dir = os.path.dirname(file_path) or os.getcwd()
    
    os.makedirs(output_dir, exist_ok=True)
    print(f"Cartella '{output_dir}' creata.")
    
    # File sequenziale
    output_path = _next_sequential_filename(output_dir)
    file_number = os.path.basename(output_path).replace("generated_code", "")
    
    # Setup logging for main module
    suppress_external_logs()
    main_logger = setup_module_logger("main", output_dir, file_number)
    
    # Setup logging for generator module
    setup_generator_logger(output_dir, file_number)
    
    # Prompt personalizzato dell'utente
    user_prompt = get_user_user_prompt()

    # Esegue analisi sul tono del prompt
    user_tone = sentiment_analysis(user_prompt)
    main_logger.debug("Analisi del sentimento dell'utente: " + str(user_tone))

    # Generazione codice con l'AI
    generated_code = generate_code(user_prompt, user_tone)
    
    response = generated_code[0].choices[0].message.content.strip()
    response_emotion = generated_code[1].choices[0].message.content.strip()

    with open(output_path+".py", "w", encoding="utf-8") as f:
        f.write(response)

    with open(output_path+"_emotion.py", "w", encoding="utf-8") as f:
        f.write(response_emotion)

    main_logger.debug(f"✅ Codice salvato in {output_path}")
    print(f"✅ Files created: {os.path.basename(output_path)}.py, {os.path.basename(output_path)}_emotion.py")
    print(f"📝 Log files: main_log_{file_number}.txt, generator_log_{file_number}.txt")




if __name__ == "__main__":
    main()
