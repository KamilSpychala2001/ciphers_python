# 08/2022

def decoding_vigenere(encrypted_message, key_of_encry):
    key_length_of_encrypted_message = []

    help = 0
    for i in encrypted_message:
        if not i.isalpha():
            key_length_of_encrypted_message.append(i)
            continue

        key_length_of_encrypted_message.append(key_of_encry[help])
        help += 1
        help = help % len(key_of_encry)

    result = []
    for i, j in zip(encrypted_message, key_length_of_encrypted_message):
        result.append(decoding_ceaser(i, ord(j) - 97))

    # print(result)
    result_join = ''.join(result)
    return result_join

def decoding_ceaser(msg_in_func, offset):
    decr = []

    for i in msg_in_func:
        if not i.isalpha():
            decr.append(i)
            continue

        a = ord(i)

        a = a + offset

        if a > 122:
            dist_from_a = a % 123
            a = 97 + dist_from_a

        decr.append(chr(a))

    msg_back = ''.join(decr)
    return msg_back

def encoding_vigenere(message_to_encrypt, key):
    key_length_to_encrypt_message = []

    help = 0
    for i in message_to_encrypt:
        if not i.isalpha():
            key_length_to_encrypt_message.append(i)
            continue

        key_length_to_encrypt_message.append(key[help])
        help += 1
        help = help % len(key)


    result = []
    for i, j in zip(message_to_encrypt, key_length_to_encrypt_message):
        # - 97 bo to jest "a" w ascii
        result.append(encoding_ceaser(i, ord(j) - 97))

    result_join = ''.join(result)
    return result_join

def encoding_ceaser(msg, offset):
    decr = []

    for i in msg:
        if not i.isalpha():
            decr.append(i)
            continue

        a = ord(i)
        a = a - offset

        if a < 97:
            dist_from_z = 96 % a
            a = 122 - dist_from_z

        decr.append(chr(a))

    msg_back = ''.join(decr)
    return msg_back

encrypted = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
key = "friends"
print(decoding_vigenere(encrypted, key))
a = encoding_vigenere("encrypted text", "key")
print(a)
print(decoding_vigenere(a, "key"))

