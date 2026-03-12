"""
evasion_tester.py
Module 3: Evasion Testing
Simulates signature-based detection against original
and obfuscated payloads.
"""

# Simulated signature database (keywords detectors look for)
SIGNATURES = [
    "cmd.exe",
    "powershell",
    "wget",
    "curl",
    "nc -e",
    "eval(",
    "exec(",
    "base64",
    "shellcode",
    "reverse_shell",
    "/bin/sh",
    "whoami",
    "nmap",
    "metasploit",
]

def scan_payload(payload):
    """Check if payload matches any known signatures."""
    detected = []
    payload_lower = payload.lower()
    for sig in SIGNATURES:
        if sig.lower() in payload_lower:
            detected.append(sig)
    return detected

def run_evasion_test(original, obfuscated):
    """Compare detection on original vs obfuscated payload."""
    print("\n" + "="*45)
    print("   MODULE 3 — EVASION TESTER")
    print("="*45)

    # Scan original
    orig_hits = scan_payload(original)
    print(f"\n  [Original Payload]")
    print(f"  Payload   : {original}")
    if orig_hits:
        print(f"  DETECTED  : {orig_hits}")
        print(f"  Status    : CAUGHT by {len(orig_hits)} signature(s)")
    else:
        print(f"  Status    : Not detected")

    # Scan obfuscated
    obf_hits = scan_payload(obfuscated)
    print(f"\n  [Obfuscated Payload]")
    print(f"  Payload   : {obfuscated[:60]}...")
    if obf_hits:
        print(f"  DETECTED  : {obf_hits}")
        print(f"  Status    : CAUGHT by {len(obf_hits)} signature(s)")
    else:
        print(f"  Status    : EVADED detection!")

    # Result
    print(f"\n  [Evasion Result]")
    if orig_hits and not obf_hits:
        print(f"  SUCCESS - Obfuscation bypassed detection!")
        evaded = True
    elif not orig_hits:
        print(f"  Original was not detected either.")
        evaded = False
    else:
        print(f"  FAILED - Obfuscated payload still detected.")
        evaded = False

    print("="*45)
    return {
        "original_detected":   len(orig_hits) > 0,
        "obfuscated_detected": len(obf_hits) > 0,
        "evaded":              evaded,
        "orig_hits":           orig_hits,
        "obf_hits":            obf_hits,
    }
