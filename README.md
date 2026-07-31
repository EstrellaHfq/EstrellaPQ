# EstrellaPQ — Logical–Fractal Post-Quantum Cryptography

> **Research Prototype – Reference Implementation**
>
> EstrellaPQ is an experimental post-quantum cryptographic research project based on the **Logical–Fractal Quantum Hamiltonian (HQF)** and its resonant spectral invariants.
>
> **This repository represents the first public reference implementation of the HQF framework.**
> It is intended for mathematical validation, software development, reproducibility, and interoperability testing.
>
> **Important:** The Hamiltonian currently implemented in this repository is an **initial simplified (partially coupled) reference operator** designed to validate the numerical framework, spectral algorithms, software architecture, and cryptographic interfaces.
>
> It **must not** be interpreted as the complete coupled HQF operator described in the theoretical research programme. Future releases will progressively incorporate the full interaction terms while preserving the external cryptographic API whenever possible.

---

# Overview

EstrellaPQ is a research implementation derived from the **Logical–Fractal Quantum Hamiltonian (HQF)** and the **Quantum Fractal–Logical Unified Field**.

The project combines concepts from

- fractal geometry,
- logical operators,
- spectral theory,
- resonant projectors,
- multiscale analysis,
- post-quantum cryptography.

The long-term objective is to investigate cryptographic primitives whose security is derived from resonant spectral invariants of HQF operators.

The present repository provides a reproducible reference implementation suitable for experimentation and future software development.

---

# Current Development Status

The repository currently contains:

- ✅ Mathematical reference implementation in Python.
- ✅ Numerical HQF operator construction.
- ✅ Spectral decomposition.
- ✅ Resonant projector construction.
- ✅ Key generation prototype.
- ✅ Portable C API.
- ✅ PQM4-compatible project structure.
- 🚧 Experimental signature interface.
- 🚧 Experimental verification interface.
- 🚧 Full coupled HQF operator (under development).
- 🚧 Complete HQF signature algorithm (under development).

The current implementation should therefore be considered a **research prototype** rather than a production cryptographic library.

---

# Mathematical Model

The present implementation uses the simplified reference Hamiltonian

\[
H_{HQF}=A_F^{\alpha}\otimes I+I\otimes S+K\otimes P
\]

where

- \(A_F^{\alpha}\) is the discrete fractal Laplacian,
- \(K\) is the integral kernel operator,
- \(S\) is the logical operator,
- \(P\) is the Boolean projector.

This operator provides a numerically stable framework for

- spectral decomposition,
- resonant projector computation,
- validation of numerical routines,
- software architecture development.

The **fully coupled HQF operator described in the theoretical framework is intentionally not yet implemented in this repository.**

Future versions will progressively introduce the complete interaction terms and multiscale coupling mechanisms described in the HQF research programme.

---

# Repository Structure

```
EstrellaPQ/
│
├── python_reference/
│      Reference HQF implementation
│
├── c_api/
│      Portable C reference API
│
├── crypto_sign/
│   └── estrella/
│          PQM4-compatible implementation
│
├── tests/
│      Numerical validation tests
│
├── LICENSE
└── README.md
```

---

# Python Reference

The Python implementation includes

- Fractal Laplacian construction
- Integral kernel operator
- Logical operators
- HQF Hamiltonian assembly
- Spectral decomposition
- Spectral gap computation
- Resonant projector construction
- Reference key generation
- Numerical stability tests

Example

```python
from python_reference.estrella_pq_reference import estrella_pq_demo

estrella_pq_demo()
```

The demo computes

- HQF operator,
- eigenvalues,
- eigenvectors,
- resonant spectral gaps,
- projectors,
- reference keypair.

---

# C Reference API

The directory `c_api/` contains a portable implementation intended as the software bridge between the mathematical reference implementation and embedded environments.

The API provides

- deterministic reference key generation,
- fixed-size public keys,
- fixed-size secret keys,
- portable interface suitable for integration into external frameworks.

---

# PQM4 Integration

The directory

```
crypto_sign/estrella
```

contains an experimental implementation compatible with the standard

```
crypto_sign_keypair()
crypto_sign()
crypto_sign_open()
```

API used by PQClean, SUPERCOP and PQM4-style frameworks.

Its current purpose is

- software integration,
- compilation testing,
- benchmarking,
- interface validation.

The signature and verification algorithms are **experimental** and will be progressively replaced by the complete HQF signature scheme as the mathematical framework evolves.

---

# Research Goals

The long-term objectives of EstrellaPQ include

- complete HQF coupled Hamiltonian,
- resonant signature algorithm,
- deterministic reference implementation,
- optimized C implementation,
- ARM Cortex-M implementation,
- benchmarking,
- interoperability testing,
- independent cryptanalytic evaluation.

The project welcomes reproducibility studies, numerical verification, code review, and independent security analysis.

---

# License

Apache License 2.0

