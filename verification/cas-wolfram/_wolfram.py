#!/usr/bin/env python
r"""Shared Wolfram-kernel plumbing for the cas-wolfram independent-CAS checks.

Factored out of verify_term_ac.py / verify_traces.py: kernel auto-discovery (the
14.3 binary lives deep under SystemFiles\Kernel\Binaries) and a retry wrapper for
the flaky fresh-install WSTP startup. Import from the verify_* scripts.

Override the kernel path with the WOLFRAM_KERNEL environment variable.
"""
import glob
import os
import time


def discover_kernel():
    r"""Locate the Wolfram kernel binary (deep under SystemFiles on Windows)."""
    env = os.environ.get("WOLFRAM_KERNEL")
    if env:
        return env
    roots = [
        r"C:\Program Files\Wolfram Research\*\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
        r"C:\Program Files\Wolfram Research\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
    ]
    matches = sorted(m for r in roots for m in glob.glob(r))
    return matches[-1] if matches else None


def start_with_retry(session_cls, wlexpr, kernel, attempts=3, delay=3):
    r"""Start a WolframLanguageSession, retrying the flaky fresh-install startup."""
    last = None
    for i in range(1, attempts + 1):
        session = None
        try:
            session = session_cls(kernel) if kernel else session_cls()
            session.evaluate(wlexpr("1"))
            return session
        except Exception as e:
            last = e
            if session is not None:
                try:
                    session.terminate()
                except Exception:
                    pass
            if i < attempts:
                print(f"  kernel start attempt {i} failed ({type(e).__name__}); retrying in {delay}s...")
                time.sleep(delay)
    raise last


def open_session():
    r"""Convenience: import wolframclient, discover the kernel, return a live session.

    Returns (session, wlexpr). Raises RuntimeError with a friendly message if the
    client is missing or no kernel can be started.
    """
    try:
        from wolframclient.evaluation import WolframLanguageSession
        from wolframclient.language import wlexpr
    except ImportError:
        raise RuntimeError("wolframclient not installed  ->  py -m pip install wolframclient")
    kernel = discover_kernel()
    if kernel:
        print(f"Using kernel: {kernel}")
    try:
        session = start_with_retry(WolframLanguageSession, wlexpr, kernel)
    except Exception as e:
        raise RuntimeError(
            f"No Wolfram kernel after retries ({type(e).__name__}: {e}). "
            "Launch the Wolfram app once to finish first-run activation, or set WOLFRAM_KERNEL."
        )
    return session, wlexpr
