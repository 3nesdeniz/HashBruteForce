def detect_hash_type(hash_string):
    #Boşlukları temizlemek için
    hash_string = hash_string.strip() 
    
    #Türü uzunluktan yola çıkarak belirlemek için
    hash_length = len(hash_string)
    
    if hash_length == 32:
        return "md5"
    elif hash_length == 40:
        return "sha1"
    elif hash_length == 64:
        return "sha256"
    elif hash_length == 128:
        return "sha512"
    else:
        return None