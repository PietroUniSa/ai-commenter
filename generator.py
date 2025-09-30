from openai import OpenAI
import os
import logging
from logger_config import setup_module_logger

# analizzare il prompt dell'utente e rispondere di consenguenza
# l'ai crea il file in base al prompt e lo stile
#Prossime modifiche da implementare:
#-l'ai deve addottare il comportamento che rispecchia il tono dell'utente e generare commenti in base al proprio sentimento.

# Modello e chiave da variabile d'ambiente
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Global logger for this module
_generator_logger = None

def setup_generator_logger(output_dir: str, file_number: str):
    """Setup logger for generator module"""
    global _generator_logger
    _generator_logger = setup_module_logger("generator", output_dir, file_number)

def get_logger():
    """Get the generator logger instance"""
    if _generator_logger is None or not _generator_logger.handlers:
        # Fallback to basic logging if not properly initialized or handlers are closed
        return logging.getLogger(__name__)
    return _generator_logger

def build_prompt(user_prompt: str) -> list:
    logger = get_logger()
    logger.debug("DEBUG: Prompt OGGETTIVO inviato al modello:\n")
    logger.debug(user_prompt)
    
    
    return [
        {"role": "system", "content": "usa python come linguaggio di programmazione".strip()},
        {"role": "user", "content": user_prompt.strip()}
    ]

def build_prompt_emotion(user_prompt: str) -> list:
    logger = get_logger()
    logger.debug("DEBUG: Prompt EMOTION inviato al modello:\n")
    logger.debug(user_prompt)
    return [
        {"role": "system", "content": "usa python come linguaggio di programmazione".strip()},
        {"role": "user", "content": user_prompt.strip()}
    ]
    
def generate_code(user_prompt: str,sentiment_analysis: str) -> str:
    logger = get_logger()
    generated_user_code = build_prompt(objective_prompt(user_prompt))
    
    logger.debug("DEBUG: Sentiment Rilevata :\n" + str(sentiment_analysis))

    generated_user_code_emotion = build_prompt_emotion(user_prompt)

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

def objective_prompt(user_prompt: str) -> str:
    system_msg = {
        "role": "system",
        "content": (
            "Sei un analizzatore di prompt"
            "Rispondi solo con la parte oggettiva della frase senza aggiungere l'emotion dell'utente"
        )
    }

    user_msg = {"role": "user", "content": user_prompt}

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[system_msg, user_msg],
        temperature=0
    )

    result = response.choices[0].message.content.strip().lower()
    
    logger = get_logger()
    logger.debug("DEBUG: OBJECTIVE PROMP Rilevata :\n" + str(result))

    return result