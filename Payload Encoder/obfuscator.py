"""
obfuscator.py
Module 2: String Obfuscation
Techniques: random insert, split, reverse, escape
"""

import random
import string

# ── Random character insertion ────────────────
def random_insert(payload, char="%", every=3):
    result = ""
    for i, c in enumerate(payload):
        result += c
        if (i + 1) % every == 0:
            result += char
    return result

# ── Character splitting (hex escape) ─────────
def hex_escape(payload):
    return ''.join(f"\\x{ord(c):02x}" for c in payload)

# ── Reverse ───────────────────────────────────
def reverse_payload(payload):
    return payload[::-1]

# ── Case toggle ───────────────────────────────
def case_toggle(payload):
    return ''.join(c.upper() if i % 2 == 0 else c.lower()
                   for i, c in enumerate(payload))

# ── Null byte insert ──────────────────────────
def null_insert(payload):
    return '\x00'.join(payload)

# ── Main function ─────────────────────────────
def obfuscate_payload(payload, method):
    print("\n" + "="*45)
    print("   MODULE 2 — OBFUSCATOR")
    print("="*45)
    print(f"  Method  : {method}")
    print(f"  Original: {payload}")

    if   method == "insert":  result = random_insert(payload)
    elif method == "hex":     result = hex_escape(payload)
    elif method == "reverse": result = reverse_payload(payload)
    elif method == "toggle":  result = case_toggle(payload)
    elif method == "null":    result = null_insert(payload)
    else:
        print("  Unknown method.")
        return payload

    print(f"  Obfuscated: {result}")
    print("="*45)
    return result
