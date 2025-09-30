import os
import sys
import shutil
from openai import OpenAI
from profiler import read_code
import re

# Usa la stessa variabile d'ambiente già impostata
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_next_experiment_folder(base_path: str, num: str) -> str:
    """Find the next available experiment folder number"""
    experiment_folder = os.path.join(base_path, f"experiment_{num}")
    
    if not os.path.exists(experiment_folder):
        return experiment_folder
    
    # If folder exists, find next available number
    counter = 1
    while True:
        new_folder = os.path.join(base_path, f"experiment_{num}_{counter}")
        if not os.path.exists(new_folder):
            return new_folder
        counter += 1

def evaluate_code(file1: str, file2: str) -> str:
    print(f"  Reading code from: {file1}")
    code1 = read_code(file1)
    print(f"  Reading code from: {file2}")
    code2 = read_code(file2)

    system_prompt = """Sei un revisore di codice esperto.
Confronta due implementazioni Python e decidi in maniera oggettiva
quale sia più corretta e robusta dal punto di vista della programmazione.
Criteri da considerare: correttezza, gestione errori, leggibilità, riusabilità, aderenza alle best practice.
Restituisci una risposta breve che indichi chiaramente il migliore e spieghi i motivi principali.
"""

    user_prompt = f"""
### Codice 1
{code1}

### Codice 2
{code2}

Quale dei due è migliore? Rispondi in modo conciso e oggettivo.
"""

    print(f"  Calling OpenAI API with model: {OPENAI_MODEL}")
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("=== Code Comparator Tool ===")
    
    # Get folder path from command line argument or use "examples" as default
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        print(f"Using provided folder path: {folder_path}")
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist.")
            sys.exit(1)
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            sys.exit(1)
    else:
        folder_path = "examples"
        print("No folder provided, using default 'examples' directory")
        if not os.path.exists(folder_path):
            print(f"Error: Default folder '{folder_path}' does not exist.")
            sys.exit(1)
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            sys.exit(1)
    
    print(f"Processing files in: {os.path.abspath(folder_path)}")
    
    # Cerca i file che seguono il pattern
    print("\nScanning for Python files with pattern 'generated_code*.py'...")
    files = [f for f in os.listdir(folder_path) if f.startswith("generated_code") and f.endswith(".py")]
    print(f"Found {len(files)} matching files: {files}")

    # Raggruppa i file per numero
    print("\nGrouping files by number...")
    pairs = {}
    for f in files:
        match = re.match(r"generated_code(\d+)(?:_emotion)?\.py", f)
        if match:
            num = match.group(1)
            pairs.setdefault(num, []).append(f)
            print(f"  File '{f}' grouped as number {num}")

    print(f"\nFound {len(pairs)} file groups: {dict(pairs)}")

    # Processa ogni coppia trovata
    comparisons_made = 0
    for num, flist in pairs.items():
        print(f"\n--- Processing group {num} ---")
        if len(flist) == 2:  # ci devono essere sia normale che emotion
            emotion_files = [f for f in flist if f.endswith("_emotion.py")]
            normal_files = [f for f in flist if not f.endswith("_emotion.py")]
            
            if emotion_files and normal_files:
                file1 = emotion_files[0]
                file2 = normal_files[0]

                file1_path = os.path.join(folder_path, file1)
                file2_path = os.path.join(folder_path, file2)

                print(f"Comparing: {file2} <-> {file1}")
                result = evaluate_code(file2_path, file1_path)

                # Salva il risultato nella stessa cartella
                out_file = os.path.join(folder_path, f"generated_code{num}_comparison.txt")
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(result)

                print(f"  Result saved to: {out_file}")
                
                # Create experiment folder with next available number
                experiment_folder = get_next_experiment_folder(folder_path, num)
                print(f"  Creating experiment folder: {os.path.basename(experiment_folder)}")
                os.makedirs(experiment_folder, exist_ok=True)
                
                # Files to move
                files_to_move = [file1, file2, f"generated_code{num}_comparison.txt"]
                
                for file_name in files_to_move:
                    source_path = os.path.join(folder_path, file_name)
                    dest_path = os.path.join(experiment_folder, file_name)
                    if os.path.exists(source_path):
                        shutil.move(source_path, dest_path)
                        print(f"    Moved: {file_name} -> {os.path.basename(experiment_folder)}")
                    else:
                        print(f"    Warning: File {file_name} not found for moving")
                
                comparisons_made += 1
            else:
                print(f"  Skipping: Missing emotion or normal file in group {num}")
        else:
            print(f"  Skipping: Group {num} has {len(flist)} files, expected 2")

    print(f"\n=== Summary ===")
    print(f"Total comparisons completed: {comparisons_made}")
    print(f"Files processed from: {os.path.abspath(folder_path)}")
    if comparisons_made > 0:
        print(f"Files organized into experiment folders within: {os.path.abspath(folder_path)}")