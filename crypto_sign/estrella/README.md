# EstrellaPQ — Logical-Fractal Cryptography (PQM4 Interface)

This directory contains the PQM4-style interface for the EstrellaPQ
logical-fractal cryptographic scheme, derived from the HQF Hamiltonian
and resonant spectral invariants.

## Files

- `api.h` — PQM4-compatible API.
- `keypair.c` — keypair generation (delegates to `c_api/estrella_pq.c`).
- `sign.c` — reference signature function.
- `verify.c` — reference verification function.

## Status

This is a **reference implementation**:

- Keypair generation is based on the logical-fractal theory (HQF + resonant invariants).
- Signature/verification is a deterministic placeholder, ready for the full HQF-based scheme.

The Python reference (`python_reference/`) contains the full spectral logic.
