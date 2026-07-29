#ifndef ESTRELLA_PQ_H
#define ESTRELLA_PQ_H

#include <stddef.h>
#include <stdint.h>

/*
 * EstrellaPQ — C API (reference)
 * Compatible in spirit with PQClean/PQM4 style.
 *
 * Key sizes (must match Python reference):
 *  - Public key: 1560 bytes
 *  - Secret key: 512 bytes
 */

#define ESTRELLA_PQ_PUBLIC_KEY_BYTES 1560
#define ESTRELLA_PQ_SECRET_KEY_BYTES 512

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Key generation API
 *
 * pk: output buffer for public key (size ESTRELLA_PQ_PUBLIC_KEY_BYTES)
 * sk: output buffer for secret key (size ESTRELLA_PQ_SECRET_KEY_BYTES)
 *
 * Returns 0 on success, non-zero on error.
 */
int estrella_pq_keygen(uint8_t *pk, uint8_t *sk);

#ifdef __cplusplus
}
#endif

#endif /* ESTRELLA_PQ_H */
