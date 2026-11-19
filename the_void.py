import os
import sys
import time
import random
import shutil

GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, speed=0.025):
for char in text:
sys.stdout.write(char)
sys.stdout.flush()
time.sleep(speed)
print()

def progress_bar(label, duration=1.5):
print(f"{CYAN}{label}{RESET}")
width = 30
for i in range(width + 1):
percent = int(i / width * 100)
bar = "█" * i + "░" * (width - i)
sys.stdout.write(f"\r{GREEN}[{bar}] {percent:3d}%{RESET}")
sys.stdout.flush()
time.sleep(duration / width)
print("\n")

def matrix_rain(seconds=3):
width = min(shutil.get_terminal_size().columns, 90)
height = min(shutil.get_terminal_size().lines, 24)
drops = [random.randint(-height, 0) for _ in range(width)]
end = time.time() + seconds

while time.time() < end:
for row in range(height):
line = ""
for col in range(width):
if drops[col] == row:
line += f"{WHITE}{random.choice('01XYZ#$%')}{RESET}"
elif 0 <= row - drops[col] < 5:
line += f"{DARK_GREEN}{random.choice('01ABCDEF')}{RESET}"
else:
line += " "
print(line)
drops = [
drop + 1 if random.random() > 0.12 else random.randint(-height, 0)
for drop in drops
]
time.sleep(0.07)
sys.stdout.write(f"\033[{height}A")
sys.stdout.flush()

def main():
clear()
print(f"{GREEN}{BOLD}")
print(r"""
████████╗██╗ ██╗███████╗
╚══██╔══╝██║ ██║██╔════╝
██║ ███████║█████╗
██║ ██╔══██║██╔══╝
██║ ██║ ██║███████╗
╚═╝ ╚═╝ ╚═╝╚══════╝
""")
print(f" {WHITE}T H E V O I D{RESET}")
print(f" {DARK_GREEN}UNKNOWN SYSTEM v9.0{RESET}\n")

time.sleep(1)
type_text(f"{GREEN}[*] Establishing secure connection...{RESET}")
time.sleep(0.6)
type_text(f"{GREEN}[*] Connection established.{RESET}")
time.sleep(0.5)
print()

progress_bar("[+] Scanning digital universe...", 1.4)
progress_bar("[+] Decoding encrypted signals...", 1.2)
progress_bar("[+] Searching for something interesting...", 1.6)

print(f"{PURPLE}[!] AN UNKNOWN SIGNAL HAS BEEN DETECTED{RESET}\n")
time.sleep(1)

for _ in range(12):
code = "".join(random.choices(
"0123456789ABCDEF", k=32
))
print(f"{DARK_GREEN}0x{random.randint(4096,65535):04X} "
f"{code}{RESET}")
time.sleep(0.12)

print()
type_text(f"{CYAN}Rendering the void...{RESET}", 0.04)
time.sleep(0.5)
clear()
matrix_rain(3)
clear()

print(f"{GREEN}{BOLD}")
print("========================================")
print(" YOU FOUND THE VOID")
print("========================================")
print(RESET)

messages = [
"Reality is just code you haven't read yet.",
"Somewhere, something is waiting to be discovered.",
"The universe is stranger than any simulation.",
"You were never supposed to find this screen.",
"Every great discovery begins with a question."
]

type_text(f"{WHITE}{random.choice(messages)}{RESET}", 0.045)
print()
type_text(f"{GREEN}Session terminated. Leave no trace.{RESET}")
print(f"{DARK_GREEN}Thanks for entering THE VOID.{RESET}\n")

if __name__ == "__main__":
try:
main()
except KeyboardInterrupt:
print(f"\n{RED}Connection terminated by user.{RESET}")
