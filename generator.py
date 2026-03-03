import os, requests
import pyfiglet
import random

colors = [
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"

def show_logo(text="\t SpeedHubX", font="slant"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    for line in ascii_art.splitlines():
        color = random.choice(colors)
        print(color + line + RESET)

def colorful_section_border():
    border = "§" * 62
    return "".join(random.choice(colors) + ch + RESET for ch in border)

def colorful_section_borders():
    borders = "§" * 2
    return "".join(random.choice(colors) + ch + RESET for ch in borders)

def spacing():
    return "\t" * 7 + " " * 4

def show_section():
    print("\n" + colorful_section_border())
    print(colorful_section_borders() + spacing() + colorful_section_borders())
    print(colorful_section_borders() + " " * 14 + "Welcome to SpeedHubX Generator" + " " * 14 + colorful_section_borders())
    print(colorful_section_borders() + spacing() + colorful_section_borders())
    print(colorful_section_border())
    print(colorful_section_borders() + spacing() + colorful_section_borders())
    print(colorful_section_borders() + " " * 6 + "Telegram Channel : https://t.me/strongHansome" + " " * 6 + " " + colorful_section_borders())
    print(colorful_section_borders() + " " * 5 + "Telegram Group   : https://t.me/AmrosoCommunity" + " " * 5 + " " + colorful_section_borders())
    print(colorful_section_borders() + spacing() + colorful_section_borders())
    print(colorful_section_border() + "\n")

def trigger_github(gen_type):
    repo = "AmrosoInfinity/amrosoGeneratorToken"  # ganti dengan repo kamu
    token = os.getenv("GITHUB_TOKEN") # simpan personal access token di Termux
    url = f"https://api.github.com/repos/{repo}/actions/workflows/generator.yml/dispatches"
    headers = {"Authorization": f"token {token}"}
    data = {"ref": "main", "inputs": {"gen_type": gen_type}}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 204:
        print(f"Workflow {gen_type} berhasil dipicu di GitHub Actions.")
    else:
        print("Gagal trigger workflow:", r.text)

def main():
    show_logo()
    show_section()
    print("1. Token Grab\n2. Token Gojek")
    choice = input("Pilih generator: ")

    if choice == "1":
        print("a. Play Generate\nb. Back")
        sub = input("Pilih: ")
        if sub == "a":
            trigger_github("grab")
    elif choice == "2":
        print("a. Play Generate\nb. Back")
        sub = input("Pilih: ")
        if sub == "a":
            trigger_github("gojek")

if __name__ == "__main__":
    main()
