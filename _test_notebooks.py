"""Execute-test all notebooks; report pass/fail.

Runs every `.ipynb` under the chapter folders and the references folder via
`nbconvert --execute`, reporting a simple pass / fail / timeout summary.
批量执行所有 notebook 并汇报通过 / 失败 / 超时。
"""
import glob
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
NB_PATTERNS = [
    "Ch0*/*.ipynb",
    "Ch1*/*.ipynb",
    "00_references/*.ipynb",
]

results = []
notebooks = []
for pat in NB_PATTERNS:
    notebooks.extend(glob.glob(os.path.join(ROOT, pat)))
notebooks = sorted(set(notebooks))

print(f"Found {len(notebooks)} notebooks to test\n")

for nb in notebooks:
    rel = os.path.relpath(nb, ROOT)
    print(f"[{len(results)+1:2d}/{len(notebooks)}] {rel}", flush=True)
    start = time.time()
    tmp = tempfile.NamedTemporaryFile(suffix=".ipynb", delete=False).name
    try:
        r = subprocess.run(
            [sys.executable, "-m", "nbconvert",
             "--to", "notebook", "--execute",
             "--output", tmp,
             "--ExecutePreprocessor.timeout=180",
             "--ExecutePreprocessor.kernel_name=python3",
             nb],
            capture_output=True, text=True, timeout=240,
        )
        ok = r.returncode == 0
        elapsed = time.time() - start
        if ok:
            print(f"    PASS in {elapsed:.1f}s")
            results.append((rel, "PASS", elapsed, ""))
        else:
            err = r.stderr.strip().split("\n")[-1][:250]
            print(f"    FAIL in {elapsed:.1f}s: {err}")
            results.append((rel, "FAIL", elapsed, err))
    except subprocess.TimeoutExpired:
        results.append((rel, "TIMEOUT", 180, ""))
        print("    TIMEOUT")
    finally:
        try:
            os.remove(tmp)
        except Exception:
            pass

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
pass_cnt = sum(1 for _, s, _, _ in results if s == "PASS")
fail_cnt = sum(1 for _, s, _, _ in results if s == "FAIL")
to_cnt = sum(1 for _, s, _, _ in results if s == "TIMEOUT")
print(f"PASS: {pass_cnt}  FAIL: {fail_cnt}  TIMEOUT: {to_cnt}  TOTAL: {len(results)}")
print()
if fail_cnt or to_cnt:
    print("Failures:")
    for rel, status, t, err in results:
        if status != "PASS":
            print(f"  [{status}] {rel} ({t:.0f}s)")
            if err:
                print(f"      -> {err}")
