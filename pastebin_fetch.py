import os, requests, random

def fetch_tokens(paste_url):
    try:
        r = requests.get(paste_url.strip())
        if r.status_code == 200:
            return r.text.strip().splitlines()
        else:
            print("Gagal mengambil token dari Pastebin.")
            return []
    except Exception as e:
        print("Error:", e)
        return []

def run_generator(gen_type):
    if gen_type == "grab":
        url = "https://pastebin.com/raw/fCze2dA1"  # link raw Pastebin Grab
        tokens = fetch_tokens(url)
        if tokens:
            print("=== Token Grab (Random) ===")
            print(random.choice(tokens))  # ambil 1 token random
        else:
            print("Tidak ada token Grab ditemukan.")
    elif gen_type == "gojek":
        url = "https://pastebin.com/raw/PASTE_ID_GOJEK"  # ganti dengan Pastebin Gojek
        tokens = fetch_tokens(url)
        if tokens:
            print("=== Token Gojek (Random) ===")
            print(random.choice(tokens))  # ambil 1 token random
        else:
            print("Tidak ada token Gojek ditemukan.")
    else:
        print("Generator type tidak valid.")

if __name__ == "__main__":
    gen_type = os.getenv("GEN_TYPE", "grab")
    run_generator(gen_type)