"""
encoder.py
Module 1: Payload Encoder
Supports Base64, XOR, and ROT13 encoding/decoding
"""

import base64

# ── Base64 ────────────────────────────────────
def base64_encode(payload):
    return base64.b64encode(payload.encode()).decode()

def base64_decode(payload):
    return base64.b64decode(payload.encode()).decode()

# ── XOR ───────────────────────────────────────
def xor_encode(payload, key):
    return ''.join(chr(ord(c) ^ key) for c in payload)

def xor_decode(payload, key):
    return xor_encode(payload, key)

# ── ROT13 ─────────────────────────────────────
def rot13_encode(payload):
    result = ""
    for c in payload:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result

def rot13_decode(payload):
    return rot13_encode(payload)

# ── Multi-layer ───────────────────────────────
def multi_layer_encode(payload, key=42):
    step1 = base64_encode(payload)
    step2 = xor_encode(step1, key)
    step3 = rot13_encode(step2)
    return step3

# ── Main function with menu ───────────────────
def encode_payload(payload):
    print("\n" + "="*45)
    print("   MODULE 1 — ENCODER")
    print("="*45)
    print("  Select encoding method:")
    print("  1. Base64")
    print("  2. XOR")
    print("  3. ROT13")
    print("  4. Multi-Layer (Base64 + XOR + ROT13)")
    print("="*45)

    choice = input("  Enter choice (1-4): ").strip()

    if choice == "1":
        method = "base64"
        result = base64_encode(payload)
    elif choice == "2":
        key = int(input("  Enter XOR key (number): ").strip() or "42")
        result = xor_encode(payload, key)
        method = f"xor (key={key})"
    elif choice == "3":
        method = "rot13"
        result = rot13_encode(payload)
    elif choice == "4":
        method = "multi-layer"
        result = multi_layer_encode(payload, key)
    else:
        print("  Invalid choice. Using Base64 by default.")
        method = "base64"
        result = base64_encode(payload)

    print(f"\n  Method  : {method}")
    print(f"  Original: {payload}")
    print(f"  Encoded : {result}")
    print("="*45)
    return result, method