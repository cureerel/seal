import sys
import string
from typing import List, Dict, Any


__version__ = "0.1.0"

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print(f"seal version {__version__}")
    else:
        print(f"seal version {__version__}")

def tokenizer(text: Any) -> Dict[str, Any]:    
    # --- Error Handling ---
    if text is None:
        return {
            "tokens": [],
            "length": 0,
            "frequencies": {},
            "error": "Input cannot be None. Please provide a valid string."
        }
    
    if not isinstance(text, str):
        return {
            "tokens": [],
            "length": 0,
            "frequencies": {},
            "error": f"Invalid input type: expected 'str', got '{type(text).__name__}'."
        }
    
    if len(text.strip()) == 0:
        return {
            "tokens": [],
            "length": 0,
            "frequencies": {},
            "error": "Input string is empty or contains only whitespace."
        }

    # --- Tokenization & Cleaning ---
    try:
        # 1. Split by spaces (raw tokens)
        raw_tokens = text.split()
        
        # 2. Clean each token (remove punctuation, lowercase)
        cleaned_tokens: List[str] = []
        for word in raw_tokens:
            clean_word = word.strip(string.punctuation)  # Remove .,!?;:
            clean_word = clean_word.lower()              # Convert to lowercase
            if clean_word:                               # Skip empty strings
                cleaned_tokens.append(clean_word)
        
        # 3. If after cleaning there are no tokens (e.g., text was just punctuation)
        if not cleaned_tokens:
            return {
                "tokens": [],
                "length": 0,
                "frequencies": {},
                "error": "No valid tokens found after cleaning (text might contain only punctuation)."
            }

        # 4. Build the frequency dictionary (Key-Value pairs)
        frequencies: Dict[str, int] = {}
        for word in cleaned_tokens:
            frequencies[word] = frequencies.get(word, 0) + 1

        # Success Response
        return {
            "tokens": cleaned_tokens,
            "length": len(cleaned_tokens),
            "frequencies": frequencies,
            "error": None  # No error
        }

    except Exception as e:
        # Catch any unexpected errors (e.g., memory issues, etc.)
        return {
            "tokens": [],
            "length": 0,
            "frequencies": {},
            "error": f"An unexpected error occurred during processing: {str(e)}"
        }