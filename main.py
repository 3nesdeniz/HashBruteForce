# Hash Brute Force Tool
# Basit hash kırma programı

import argparse
from hashDetector import detect_hash_type
from hashCracker import crack_hash

def main():
    # Komut satırı argümanları
    parser = argparse.ArgumentParser(description="Hash Brute Force Tool")
    
    parser.add_argument('--hash', required=True, help='Kırılacak hash')
    parser.add_argument('-w', '--wordlist', required=True, help='Wordlist dosyası')
    parser.add_argument('-t', '--type', choices=['md5', 'sha1', 'sha256', 'sha512'], help='Hash türü')
    
    args = parser.parse_args()
    
    print("\n=== HASH BRUTE FORCE TOOL ===\n")
    
    # Hash türünü belirle
    if args.type:
        hash_type = args.type
        print("Hash Türü: " + hash_type.upper())
    else:
        hash_type = detect_hash_type(args.hash)
        if hash_type:
            print("Hash Türü: " + hash_type.upper() + " (otomatik olarak algılandı)")
        else:
            print("Hata: Hash türü algılanamadı.")
            return
    
    print("Wordlist: " + args.wordlist)
    print("\nKırma işlemi başlıyor...\n")
    
    # BruteForce 
    found, password, attempts = crack_hash(args.hash, args.wordlist, hash_type)
    
    
    print("=================================================")
    if found:
        print("[+] ŞİFRE BULUNDU: " + password)
    else:
        print("[-] Şifre bulunamadı")
    
    print("[*] Denenen kelime: " + str(attempts))
    print("=================================================")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("İşlem durduruldu!")
