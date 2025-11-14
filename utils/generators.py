import time
import random
import string

def uniq_email(prefix="siarhei_auto"):
    # гарантированно уникальный e-mail
    stamp = int(time.time() * 1000)
    rnd = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{prefix}_{stamp}_{rnd}@yandex.ru"
