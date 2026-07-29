#include "api.h"
#include <string.h>

/*
 * Reference verification.
 *
 * Recomputes the deterministic placeholder signature and compares it
 * with the first CRYPTO_BYTES bytes of sm.
 */

int crypto_sign_open(
    uint8_t *m, size_t *mlen,
    const uint8_t *sm, size_t smlen,
    const uint8_t *pk
) {
    if (!m || !mlen || !sm || !pk) {
        return -1;
    }

    if (smlen < CRYPTO_BYTES) {
        return -1;
    }

    size_t msg_len = smlen - CRYPTO_BYTES;

    uint8_t sig_ref[CRYPTO_BYTES];
    for (size_t i = 0; i < CRYPTO_BYTES; i++) {
        sig_ref[i] = (uint8_t)((i ^ (msg_len & 0xFF)) & 0xFF);
    }

    if (memcmp(sm, sig_ref, CRYPTO_BYTES) != 0) {
        return -1;
    }

    memcpy(m, sm + CRYPTO_BYTES, msg_len);
    *mlen = msg_len;

    return 0;
}
