"""
report_generator.py
Module 4: Report Generator
Generates final audit report of encoding and evasion results.
"""

from datetime import datetime

def generate_report(results):
    """
    results: list of dicts with keys:
      payload, method, encoded, evasion (dict)
    """
    report = []
    report.append("=" * 50)
    report.append("   PAYLOAD ENCODER & OBFUSCATION REPORT")
    report.append("=" * 50)
    report.append(f"  Date    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"  Total Tests : {len(results)}")
    report.append("")

    evaded_count = 0

    for i, r in enumerate(results, 1):
        report.append(f"  --- Test {i} ---")
        report.append(f"  Payload    : {r['payload']}")
        report.append(f"  Method     : {r['method']}")
        report.append(f"  Encoded    : {str(r['encoded'])[:50]}...")
        ev = r['evasion']
        report.append(f"  Original Detected  : {ev['original_detected']}")
        report.append(f"  Obfuscated Detected: {ev['obfuscated_detected']}")
        status = "EVADED" if ev['evaded'] else "CAUGHT"
        report.append(f"  Result     : {status}")
        report.append("")
        if ev['evaded']:
            evaded_count += 1

    report.append("=" * 50)
    report.append("  SUMMARY")
    report.append("=" * 50)
    report.append(f"  Total payloads tested : {len(results)}")
    report.append(f"  Successfully evaded   : {evaded_count}")
    report.append(f"  Caught                : {len(results) - evaded_count}")
    report.append(f"  Evasion rate          : {evaded_count/len(results)*100:.0f}%")
    report.append("")
    report.append("  Recommendations:")
    report.append("  - Use multi-layer encoding for better evasion")
    report.append("  - Static signatures alone are not enough")
    report.append("  - Combine behavioral + signature detection")
    report.append("  - Update signature databases regularly")
    report.append("=" * 50)

    return "\n".join(report)
