import numpy as np
from numpy.linalg import eigh

# ============================================================
#  Spectral solver for HQF
#  Derived from Estrella, Section 4.3:
#  “Dominant eigenpairs of H(N,M) are computed via ARPACK, SLEPc,
#   or block-Lanczos…”
#  For the reference implementation we use eigh().
# ============================================================

def spectral_solve(H, k):
    """
    Computes the first k eigenvalues and eigenvectors of H.
    This reference implementation uses numpy.linalg.eigh,
    consistent with the theoretical structure of HQF.
    """
    vals, vecs = eigh(H)
    idx = np.argsort(vals)[:k]
    return vals[idx], vecs[:, idx]


# ============================================================
#  Resonant invariants: spectral gaps
#  Derived from Estrella, Definition 2.4:
#  “γ_k = λ_{k+1} - λ_k”
# ============================================================

def spectral_gaps(eigenvalues):
    """
    Computes spectral gaps γ_k = λ_{k+1} - λ_k.
    These gaps are used as resonant invariants for key generation.
    """
    return np.diff(eigenvalues)


# ============================================================
#  Projector onto resonant subspace
#  Derived from Estrella, Definition 2.4:
#  “P_S = Σ_{k∈S} |u_k><u_k|”
# ============================================================

def projector_from_eigenvectors(vecs, indices):
    """
    Builds the projector P_S onto the resonant subspace defined by
    the eigenvectors with indices in S.
    """
    dim = vecs.shape[0]
    P = np.zeros((dim, dim))
    for k in indices:
        u = vecs[:, k].reshape(-1, 1)
        P += u @ u.T
    return P
