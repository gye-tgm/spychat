from spychat.crypto import asymmetric
from spychat.crypto import symmetric


keypair = asymmetric.gen_key()
session_key = symmetric.gen_key()

