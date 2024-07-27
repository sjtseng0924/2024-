import hashlib
import time

def calculate_checksum(file_path, hash_function):
    start_time = time.time()
    hasher = hashlib.new(hash_function)
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # 64KB buffer
            if not data:
                break
            hasher.update(data)
    checksum = hasher.hexdigest()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return checksum, elapsed_time

hash_functions = [
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha512",
    "sha3_224",
    "sha3_256",
    "sha3_512"
]

file_path = "video.mp4"

results = {}
for hash_function in hash_functions:
    checksum, elapsed_time = calculate_checksum(file_path, hash_function)
    results[hash_function] = (checksum, elapsed_time)

for hash_function, (checksum, elapsed_time) in results.items():
    print(f"{hash_function}:Time - {elapsed_time:.6f} seconds")

fastest_hash = min(results, key=lambda x: results[x][1])
print(f"The fastest hash function is {fastest_hash}")
