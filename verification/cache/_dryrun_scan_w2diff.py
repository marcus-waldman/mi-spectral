import importlib.util
import sys

spec = importlib.util.spec_from_file_location("runner", "verification/run_layer3_openai.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
a, b = mod.extract_modes("todo/024-w2-differential-analytic-first.md")
print("ModeA chars:", len(a), " ModeB chars:", len(b))
bad_common = ["GRADING", "ESCALATE", "escalation", "-0.22", "0.22", "Stage-1", "Stage 1",
              "consensus", "referee caught", "trap", "B_direct"]
bad_a = ["I_com metric", "I_com-metric", "overstate", "OVERSTATE",
         "differential is exactly zero", "cancels exactly in D", "sd(D) = O(1)",
         "Gram", "Schur", "operator-variance", "invariant subspace", "M_com",
         "EM identity", "self-consistency",
         "(G'I_com G)^{-1} G'I_com I_obs^{-1} I_mis G"]
# (F1)'s "EXACTLY zero" is a GIVEN audited fact in the setup, not an answer leak;
# assert it appears only in the F1 sentence.
assert a.count("EXACTLY zero") == 1 and "conditional-score identity" in a
fails = 0
for t in bad_common:
    for name, txt in (("A", a), ("B", b)):
        if t in txt:
            print(f"LEAK[{name}]: {t!r}")
            fails += 1
for t in bad_a:
    if t in a:
        print(f"LEAK[A]: {t!r}")
        fails += 1
print("Mode A head:", a[:160].replace("\n", " | "))
print("Mode A tail:", a[-160:].replace("\n", " | "))
print("Mode B head:", b[:160].replace("\n", " | "))
print("Mode B tail:", b[-160:].replace("\n", " | "))
print("SCAN:", "FAIL" if fails else "CLEAN")
sys.exit(1 if fails else 0)
