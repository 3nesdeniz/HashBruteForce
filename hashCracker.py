import hashlib

def crack_hash(target_hash, wordlist_path, hash_type):
    # Hash türüne karar vermek için
    if hash_type == "md5":
        htype = hashlib.md5
    elif hash_type == "sha1":
        htype = hashlib.sha1
    elif hash_type == "sha256":
        htype = hashlib.sha256
    elif hash_type == "sha512":
        htype = hashlib.sha512
    else:
        return (False, None, 0)
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            attempt_count = 0
            
            for line in file:
                word = line.strip()
                
                if word=="":
                    continue
                
                attempt_count += 1
                
                hashed_word = htype(word.encode('utf-8')).hexdigest()
                
                if hashed_word == target_hash.lower():
                    return (True, word, attempt_count)
            
            # Bulunamadı
            return (False, None, attempt_count)
            
    except:
        print("Hata: Dosya bulunamadı veya okunamadı!")
        return (False, None, 0)