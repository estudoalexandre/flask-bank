import os

def generate_secret_key():
    return os.urandom(24).hex()

if __name__ == "__main__":
    print("Your secret key is:", generate_secret_key())