#ifndef ESTRELLA_API_H
#define ESTRELLA_API_H

#include <stddef.h>
#include <stdint.h>

/*
 * EstrellaPQ — PQM4-style API
 * Logical-fractal cryptography based on HQF and resonant invariants.
 */

#define CRYPTO_PUBLICKEYBYTES 1560
#define CRYPTO_SECRETKEYBYTES 512
#define CRYPTO_BYTES 64

#define CRYPTO_ALGNAME "EstrellaPQ"

int crypto_sign_keypair(uint8_t *pk, uint8_t *sk);

int crypto_sign(
    uint8_t *sm, size_t *smlen,
    const uint8_t *m, size_t mlen,
    const uint8_t *sk
);

int crypto_sign_open(
    uint8_t *m, size_t *mlen,
    const uint8_t *sm, size_t smlen,
    const uint8_t *pk
);

#endif
