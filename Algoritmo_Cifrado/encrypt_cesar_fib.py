import string

'''
encrypt_with_fibonacci: toma un mensaje y una semilla (un par de números enteros que determinan el inicio de la 
secuencia de Fibonacci) como entrada. La función genera una clave a partir de la secuencia de Fibonacci y 
luego utiliza esta clave para cifrar el mensaje utilizando el cifrado de César. La clave generada es una 
cadena de caracteres del alfabeto en minúsculas y su longitud es igual a la del mensaje.
'''

# Function to get the next number in the Fibonacci sequence
def next_fibonacci(a, b):
    return a + b, a

# Function to encrypt a message using the Caesar cipher with a key generated from the Fibonacci sequence
def encrypt_with_fibonacci(message, seed):
    alphabet = string.ascii_lowercase
    key = ''
    a, b = seed[0], seed[1]
    while len(key) < len(message):
        a, b = next_fibonacci(a, b)
        key += alphabet[b % len(alphabet)]
    encrypted_message = ''
    for i, letter in enumerate(message.lower()):
        if letter in alphabet:
            new_position = (alphabet.index(letter) + alphabet.index(key[i])) % len(alphabet)
            encrypted_message += alphabet[new_position]
        else:
            encrypted_message += letter
    return (key, encrypted_message)

# Function to decrypt a message encrypted with the Caesar cipher using the key generated from the Fibonacci sequence
def decrypt_with_fibonacci(key, encrypted_message):
    alphabet = string.ascii_lowercase
    decrypted_message = ''
    for i, letter in enumerate(encrypted_message.lower()):
        if letter in alphabet:
            new_position = (alphabet.index(letter) - alphabet.index(key[i])) % len(alphabet)
            decrypted_message += alphabet[new_position]
        else:
            decrypted_message += letter
    return decrypted_message

def main():
    message = input('Enter a message: ')
    seed = (1, 1)
    key, encrypted_message = encrypt_with_fibonacci(message, seed)
    print('Message: ' + message)
    print('Key: ' + key)
    print('Encrypted message: ' + encrypted_message)
    decrypted_message = decrypt_with_fibonacci(key, encrypted_message)
    print('Decrypted message: ' + decrypted_message)


if __name__ == '__main__':
    main()

