import hashlib
from datetime import datetime
salt_answer=""
def break_sha1_hash(target_hash, password_list, mode):
    attempts = 0
    start_time = datetime.now()
    for password in password_list:
        if mode == 1:
            password=(salt_answer+password)
        hash_attempt = hashlib.sha1(password.encode()).hexdigest()
        attempts += 1
        if hash_attempt == target_hash:
            end_time = datetime.now()
            time_taken = end_time - start_time
            return password, attempts, time_taken
    return None, attempts, None
def load_password_list(file_path):
    with open(file_path, 'r') as file:
        password_list = file.read().splitlines()
    return password_list
hashes_to_break = {
    "Easy hash": "ef0ebbb77298e1fbd81f756a4efc35b977c93dae",
    "Medium hash": "0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2",
}
password_list_file = "password.txt"
password_list = load_password_list(password_list_file)

for hash_name, target_hash in hashes_to_break.items():
    clear_text_password, attempts, time_taken = break_sha1_hash(target_hash, password_list, 0)
    if clear_text_password:
        print(f"Hash:{target_hash}")
        print(f"Password: {clear_text_password}")
        print(f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken}")
salt="dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"
Leet_hacker_hash="9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
salt_answer, attempt1, time_taken1 = break_sha1_hash(salt, password_list, 0)
clear_text_password, attempt2, time_taken2 = break_sha1_hash(Leet_hacker_hash, password_list, 1)
attempts = attempt1 + attempt2
time_taken = time_taken1 + time_taken2
if clear_text_password:
    print(f"Hash:{Leet_hacker_hash}")
    print(f"Password: {clear_text_password}")
    print(f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken}")
