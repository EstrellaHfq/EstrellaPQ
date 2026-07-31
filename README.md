EstrellaPQ — Logical‑Fractal Post‑Quantum Cryptography

EstrellaPQ is a post‑quantum cryptographic scheme derived from the Logical‑Fractal Quantum Hamiltonian (HQF) and its resonant spectral invariants. The scheme is based on the Estrella framework and the Quantum Fractal‑Logical Unified Field, combining fractal geometry, logical operators, and multiscale spectral analysis.

This repository contains:

- A Python reference implementation of HQF, spectral decomposition, resonant gaps, projectors, and key generation.
- A C API compatible with PQClean/PQM4, providing a portable interface for embedded and microcontroller environments.
- A PQM4 scheme directory (crypto_sign/estrella) implementing the standard crypto_sign_* API for keypair generation, signing, and verification.

The Python reference is the mathematically complete version of the scheme.  
The C and PQM4 implementations provide a structural and functional interface for integration, testing, and benchmarking.
Project status

This repository contains the reference prototype of HQF-Sign. The current Hamiltonian is a simplified, partially coupled operator intended for validating the software architecture, numerical routines and cryptographic API. It is not the complete coupled HQF operator described in the research programme. Future releases will incorporate the full interaction terms while preserving the external API whenever possible.
---------------------------------------------------------------------

Overview

EstrellaPQ is built on the HQF Hamiltonian:

H_QF = A_F^α ⊗ I + I ⊗ S

where:

- A_F^α is a fractal Laplacian  
- S is a logical operator  
- The security of the scheme derives from resonant spectral invariants: normalized gaps, multiscale projectors, resonance indices, and stability under renormalization.

The public and secret keys are derived from the spectral structure of HQF and the resonant projector associated with the largest spectral gaps.

---------------------------------------------------------------------

Repository Structure

EstrellaHfq/  
    python_reference/      Full HQF + spectral reference implementation  
    c_api/                 C API compatible with PQClean/PQM4  
    crypto_sign/  
        estrella/          PQM4 scheme implementation  
    LICENSE                Apache 2.0  
    README.md              This file  

---------------------------------------------------------------------

Python Reference

The Python implementation provides:

- fractal Laplacian construction  
- integral kernel operator  
- logical operators  
- HQF assembly  
- eigenvalue/eigenvector computation  
- spectral gaps  
- resonant projector selection  
- key generation  

To run the demo:

from python_reference.estrella_pq_reference import estrella_pq_demo  
estrella_pq_demo()

This prints HQF components, spectrum, gaps, resonant indices, projectors, and generates a keypair.

---------------------------------------------------------------------

C API

The C API (c_api/estrella_pq.h, c_api/estrella_pq.c) provides:

- fixed‑size public and secret keys  
- a portable keypair generator  
- deterministic reference behavior for integration and testing  

This API is used directly by the PQM4 scheme.

---------------------------------------------------------------------

PQM4 Scheme

The directory crypto_sign/estrella contains:

- api.h — PQM4‑compatible API  
- keypair.c — calls the C reference key generator  
- sign.c — deterministic reference signature  
- verify.c — deterministic reference verification  
- LICENSE — Apache 2.0  
- README.md — scheme‑level documentation  

The signature implementation is a placeholder and will be replaced by the full HQF‑based signature scheme.

---------------------------------------------------------------------



---------------------------------------------------------------------

License

Apache License 2.0.

