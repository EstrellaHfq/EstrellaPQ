import numpy as np

from .keys import generate_keypair
from .operators import (
    build_fractal_laplacian,
    build_integral_kernel,
    build_boolean_operators,
    assemble_hamiltonian
)
from .spectral import (
    spectral_solve,
    spectral_gaps,
    projector_from_eigenvectors
)

# ============================================================
#  EstrellaPQ Reference Implementation
#  This module exposes a clean API for the Python reference
#  version of the EstrellaPQ cryptographic scheme.
# ============================================================

def estrella_pq_keygen(N=64, M=16, a=1.0, k=32):
    """
    Generates a public/secret keypair using the HQF Hamiltonian
    and resonant spectral invariants.

    This is the official reference entry point for key generation.
    """
    return generate_keypair(N=N, M=M, a=a, k=k)


def estrella_pq_demo():
    """
    Demonstration function for developers and reviewers.
    Builds HQF, computes eigenpairs, gaps, and projectors,
    and prints diagnostic information.

    This function is NOT used in PQM4. It is only for
    reference and debugging.
    """

    N = 32
    M = 8
    a = 1.0
    k = 16

    print("Building HQF components...")
    LN = build_fractal_laplacian(N)
    KN = build_integral_kernel(N)
    S, P = build_boolean_operators(M)

    print("Assembling Hamiltonian...")
    H = assemble_hamiltonian(a, LN, KN, S, P)

    print("Computing spectrum...")
    eigenvalues, eigenvectors = spectral_solve(H, k)

    print("Computing spectral gaps...")
    gaps = spectral_gaps(eigenvalues)

    print("Selecting resonant indices...")
    idx_sorted = np.argsort(-gaps)
    S_indices = idx_sorted[:M]

    print("Building resonant projector...")
    Ps = projector_from_eigenvectors(eigenvectors, S_indices)

    print("Generating keypair...")
    pk, sk = generate_keypair(N=N, M=M, a=a, k=k)

    print("Public key length:", len(pk))
    print("Secret key length:", len(sk))

    return {
        "LN": LN,
        "KN": KN,
        "S": S,
        "P": P,
        "H": H,
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
        "gaps": gaps,
        "resonant_indices": S_indices,
        "projector": Ps,
        "public_key": pk,
        "secret_key": sk
    }
