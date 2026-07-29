import numpy as np

from .spectral import spectral_solve, spectral_gaps, projector_from_eigenvectors
from .operators import (
    build_fractal_laplacian,
    build_integral_kernel,
    build_boolean_operators,
    assemble_hamiltonian
)

# ============================================================
#  Key sizes (reference values)
#  Derived from the Cryptography paper:
#  “Public keys are ~1.5 KB; secret keys ~512 bytes.”
# ============================================================

PUBLIC_KEY_BYTES = 1560   # ~1.56 KB
SECRET_KEY_BYTES = 512    # 512 bytes


# ============================================================
#  Key generation
#  Derived from Estrella + Cryptography paper:
#  - Spectral gaps are entropy sources.
#  - Resonant projectors define algebraic invariants.
# ============================================================

def generate_keypair(N=64, M=16, a=1.0, k=32):
    """
    Generates a public/secret keypair using resonant spectral invariants
    of the HQF Hamiltonian.

    Steps:
    1. Build HQF components (LN, KN, S, P).
    2. Assemble H(N,M).
    3. Compute first k eigenpairs.
    4. Compute spectral gaps.
    5. Select resonant indices (largest gaps).
    6. Build resonant projector P_S.
    7. Derive public and secret keys from invariants.
    """

    # --- HQF components ---
    LN = build_fractal_laplacian(N)
    KN = build_integral_kernel(N)
    S, P = build_boolean_operators(M)

    # --- Hamiltonian ---
    H = assemble_hamiltonian(a, LN, KN, S, P)

    # --- Spectrum ---
    eigenvalues, eigenvectors = spectral_solve(H, k)

    # --- Resonant invariants ---
    gaps = spectral_gaps(eigenvalues)

    # Select indices with largest gaps
    idx_sorted = np.argsort(-gaps)
    S_indices = idx_sorted[:M]

    # Resonant projector
    Ps = projector_from_eigenvectors(eigenvectors, S_indices)

    # --- Secret key: internal resonant projector ---
    sk_raw = Ps.tobytes()
    sk = sk_raw[:SECRET_KEY_BYTES]

    # --- Public key: truncated eigenvalues ---
    pk_raw = eigenvalues.tobytes()
    pk = pk_raw[:PUBLIC_KEY_BYTES]

    return pk, sk
