import random
import time

sleep_s = random.randrange(10)
print(f"sleeping for {sleep_s}s")
time.sleep(sleep_s)

# fail with a 3% chance
should_succeed = random.choices((True, False), weights=(97, 3))[0]
print(should_succeed)

if should_succeed:
    print("success")
    exit(0)

print("failure")
exit(1)
