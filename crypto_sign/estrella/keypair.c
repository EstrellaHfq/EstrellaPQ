#include "api.h"
#include "../../c_api/estrella_pq.h"

/*
 * Keypair generation for PQM4.
 * Delegates to the logical-fractal reference implementation in c_api/.
 */

int crypto_sign_keypair(uint8_t *pk, uint8_t *sk) {
    if (!pk || !sk) {
        return -1;
    }
    return estrella_pq_keygen(pk, sk);
}
