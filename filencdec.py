from cryptography.fernet import Fernet
class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
encryptor=Encryptor()
mykey=encryptor.key_create()
filename = input("Enter the filename to be encrypted / decrypted : ")
key_file = input("Enter the name keyfile : ")
encryptor.key_write(mykey, key_file)
loaded_key=encryptor.key_load(key_file)
encryptor.file_encrypt(loaded_key, filename, 'enc'+filename)
encryptor.file_decrypt(loaded_key, 'enc'+filename, 'dec'+filename)
print("Encrypted file saved as ", 'enc'+filename)
print("Decrypted file saved as " ,'dec'+filename)
print("Key file used to perform these operation is :" , key_file)
