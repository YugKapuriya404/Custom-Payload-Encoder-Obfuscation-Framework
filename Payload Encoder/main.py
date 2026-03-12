"""
main.py
Payload Encoder & Obfuscation Framework
Runs all modules automatically.
"""

from encoder          import encode_payload
from obfuscator       import obfuscate_payload
from evasion_tester   import run_evasion_test
from report_generator import generate_report

def main():
    print("\n" + "="*45)
    print("   PAYLOAD ENCODER & OBFUSCATION FRAMEWORK")
    print("="*45)

    # User input
    payload = input("\n  Enter payload to test : ").strip()

    results = []
    final_output = None
    method = None

    # ── Top-level menu ────────────────────────
    print("\n" + "="*45)
    print("  Select encryption type:")
    print("  1. Encoding  (Base64 / XOR / ROT13)")
    print("  2. Obfuscation  (Hex / Reverse / Toggle / Insert)")
    print("="*45)
    top_choice = input("  Enter choice (1 or 2): ").strip()

    # ── Encoding path ─────────────────────────
    if top_choice == "1":
        print("\n[STEP 1] Encoding Payload...")
        final_output, method = encode_payload(payload)

    # ── Obfuscation path ──────────────────────
    elif top_choice == "2":
        print("\n[STEP 1] Obfuscating Payload...")
        print("\n" + "="*45)
        print("   MODULE 2 — OBFUSCATOR")
        print("="*45)
        print("  Select obfuscation method:")
        print("  1. Hex Escape")
        print("  2. Reverse")
        print("  3. Case Toggle")
        print("  4. Random Insert")
        print("="*45)
        obf_choice = input("  Enter choice (1-4): ").strip()
        obf_map    = {"1": "hex", "2": "reverse", "3": "toggle", "4": "insert"}
        method     = obf_map.get(obf_choice, "hex")
        final_output = obfuscate_payload(payload, method)

    else:
        print("  Invalid choice. Exiting.")
        return

    # ── Evasion test ──────────────────────────
    print("\n[STEP 2] Running Evasion Test...")
    evasion = run_evasion_test(payload, final_output)
    results.append({"payload": payload, "method": method,
                    "encoded": final_output, "evasion": evasion})

    # ── Report ────────────────────────────────
    print("\n[STEP 3] Generating Report...")
    report = generate_report(results)
    print(report)

    with open("payload_report.txt", "w") as f:
        f.write(report)
    print("  Report saved to: payload_report.txt")

if __name__ == "__main__":
    main()