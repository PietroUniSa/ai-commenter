from openai import OpenAI
import os

# analizzare il prompt dell'utente e rispondere di consenguenza
# l'utente sceglie se analitico o olisticio
# l'ai commenta il file in base al prompt e lo stile
# crea il file di output



# Modello e chiave da variabile d'ambiente
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_prompt(code: str, cognitive_style: str, user_prompt: str,user_tone: str) -> list:
    # Profilo di sistema
    system_profile = f"""
Sei un assistente esperto in Python che aggiunge commenti dettagliati al codice.
I commenti devono rispettare lo stile cognitivo: {cognitive_style}.
- Utilizza nei commenti un linguaggio che trasmetta chiaramente queste emozioni: "{user_tone}".
- Non attenuare né addolcire il tono: i commenti devono contenere espressioni dirette e fortemente cariche di tali emozioni.
"""
    
    # Prompt finale strutturato
    final_prompt = f"""
{{
    "user_prompt": "{user_prompt}",
    "cognitive_style": "{cognitive_style}",
    "user_tone": "{user_tone}",
    "code": "{code}"
}}
"""

    print("DEBUG: Prompt finale inviato al modello:\n")

    print(final_prompt)

    print("\nDEBUG: Profilo di sistema inviato al modello:\n")
    
    print(system_profile)

    return [
        {"role": "system", "content": system_profile.strip()},
        {"role": "user", "content": final_prompt.strip()}
    ]


def generate_comments(code: str, cognitive_style: str, user_prompt: str,user_tone: str) -> str:
    
    messages = build_prompt(code, cognitive_style, user_prompt, user_tone)

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=1
    )

    return response.choices[0].message.content.strip()

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

    # fallback se il modello restituisce stringa vuota
    if not result:
        result = "neutrale"

    return result


def profile_analysis(user_prompt: str) -> str:
    system_msg = {
        "role": "system",
        "content": (
            "Sei un classificatore di stile cognitivo. "
            "Analizza il messaggio dell'utente e decidi se è scritto "
            "in stile 'analitico' oppure 'olistico'. "
            "Rispondi esclusivamente con una di queste due parole."
        )
    }

    user_msg = {"role": "user", "content": user_prompt}

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[system_msg, user_msg],
        
    )

    result = response.choices[0].message.content.strip().lower()

    # normalizza output
    if result not in ["analitico", "olistico"]:
        result = "neutrale"  # fallback di default

    return result