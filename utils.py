import random
import string
 
def random_string(N: int) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

