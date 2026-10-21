def ask_number(prompt, default):
    while True:
        raw = input(f"{prompt} (default = {default}): ").strip()
        if not raw:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number.")