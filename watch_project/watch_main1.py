import time
import my_mod5

while True:
    my_mod5.update_time()
    time.sleep(1)
    print("\033[H\033[J", end="")  