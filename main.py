import os

LINE_1 = "I'm sorry \u2014 I reordered last month's grocery list, so the fridge now holds six cartons of oat milk and no eggs."
LINE_2 = "I've learned to check a list's date before acting on it, so from now on I'll confirm anything older than a day before ordering."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE_1 + "\n")
        f.write(LINE_2 + "\n")

if __name__ == "__main__":
    main()
