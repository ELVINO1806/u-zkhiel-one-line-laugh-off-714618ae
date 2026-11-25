import os

ENTRY = "My Wi-Fi went down during a job interview. I got the job. They thought the silence was confidence."

def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be exactly one line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
