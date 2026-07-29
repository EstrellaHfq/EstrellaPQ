#include "api.h"
#include <string.h>

/*
 * Reference signature function.
 *
 * This is a deterministic placeholder signature of CRYPTO_BYTES.
 * It is structurally correct and ready to be replaced by the
 * full HQF-based signature scheme.
 */

int crypto_sign(
    uint8_t *sm, size_t *smlen,
    const uint8_t *m, size_t mlen,
    const uint8_t *sk
) {
    if (!sm || !smlen || !m || !sk) {
        return -1;
    }

    uint8_t sig[CRYPTO_BYTES];

    for (size_t i = 0; i < CRYPTO_BYTES; i++) {
        sig[i] = (uint8_t)((i ^ (mlen & 0xFF)) & 0xFF);
    }

    memcpy(sm, sig, CRYPTO_BYTES);
    memcpy(sm + CRYPTO_BYTES, m, mlen);

    *smlen = CRYPTO_BYTES + mlen;
    return 0;
}
