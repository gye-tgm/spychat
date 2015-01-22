from Crypto.PublicKey import RSA


def save_key(filename, content):
    with open(filename, 'wb') as file:
        file.write(content)


KEY_LENGTH = 2048
E = 65537

FORMAT = 'PEM'

priv_key_file = 'key.priv'
pub_key_file = 'key.pub'

keypair = RSA.generate(KEY_LENGTH, e=E)

pub_key = keypair.publickey().exportKey(FORMAT)
priv_key = keypair.exportKey(FORMAT)

save_key(pub_key_file, pub_key)
save_key(priv_key_file, priv_key)
