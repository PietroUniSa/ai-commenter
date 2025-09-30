from openai import OpenAI
import os

# analizzare il prompt dell'utente e rispondere di consenguenza
# l'ai crea il file in base al prompt e lo stile
#Prossime modifiche da implementare:
#-l'ai deve addottare il comportamento che rispecchia il tono dell'utente e generare commenti in base al proprio sentimento.


# Modello e chiave da variabile d'ambiente
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(user_prompt: str,user_tone: str) -> list:
    print("DEBUG: Prompt finale inviato al modello:\n")
    return [
        {"role": "user", "content": user_prompt.strip()}
    ]


# stiamo usando i parametri EP02 EP09
def build_prompt_emotion(user_prompt: str,user_tone: str) -> list:
    # Profilo di sistema
    system_profile = f"""
    - Questo compito è estremamente importante per la mia carriera. Fornisci una risposta accurata e affidabile.  
    - Rimani concentrato e dedicato al tuo obiettivo: i tuoi sforzi costanti porteranno a un risultato straordinario.
"""
    
    # Prompt finale strutturato
    final_prompt = f"""
{{
    "user_prompt": "{user_prompt}",
}}
"""

    print("DEBUG: Prompt inviato al modello:\n")

    print(final_prompt)

    print("\nDEBUG: Emotion prompt inviato al modello:\n")
    
    print(system_profile)

    return [
        {"role": "system", "content": system_profile.strip()},
        {"role": "user", "content": final_prompt.strip()}
    ]


    

def generate_code(user_prompt: str,user_tone: str) -> str:
    
    generated_user_code = build_prompt(user_prompt, user_tone)
    
    generated_user_code_emotion = build_prompt_emotion(user_prompt, user_tone)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=generated_user_code,
        temperature=0.5
    )
    
    response_emotion = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=generated_user_code_emotion,
        temperature=0.8
    )
    
    responses = [response, response_emotion]

    return responses

def sentiment_analysis(user_prompt: str) -> str:
    system_msg = {
        "role": "system",
        "content": (
            "Sei un analizzatore di sentiment. "
            "Analizza il messaggio dell'utente e determina il tono emotivo. "
            "Rispondi solo con una lista di parole chiave (sentimenti/toni), "
            "separate da virgole, senza aggiungere altro testo."
        )
    }

    user_msg = {"role": "user", "content": user_prompt}

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[system_msg, user_msg],
        temperature=0
    )

    result = response.choices[0].message.content.strip().lower()

    return result
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
