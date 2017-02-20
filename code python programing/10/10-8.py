def safe_input(line):
    try:
        return raw_input(line)
    except (EOFError, KeyboardInterrupt):
        return None

a = safe_input('hi>> ')
print a