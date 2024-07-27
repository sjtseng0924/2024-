import random
random_bytes = bytearray(random.randint(0, 255) for _ in range(1048576))
with open("random.bin", "wb") as file:
    file.write(bytes(random_bytes))