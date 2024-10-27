from math import gcd
from Crypto.Util.number import getPrime
import random
import time
from secret import FLAG

class Verifier:
    def __init__(self, seed, n, a, b):
        self.state = seed
        self.n = n
        self.a = a
        self.b = b
        self.previous_states = set()

    def next_state(self, x):
        new_state = (self.a * self.state + self.b * (1 - x)) % self.n
        self.state = new_state
        return new_state

    def get_secret_bit(self) -> int:
        return random.randrange(2)

    def verify(self, user_state, x):
        if user_state in self.previous_states:
            print("Error: repeated state")
            return False

        self.previous_states.add(user_state)

        self.next_state(x)

        if self.state != user_state:
            return False

        return True

def main():
    print("Welcome to our zkpwarmup challenge baby zkp!")

    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    print(f"{n=}")

    random.seed(int(time.time()))
    seed = random.randrange(1, n)
    a = random.randrange(1, n)
    b = random.randrange(1, n)
    print(f"{b=}")

    print("Can you prove that you know the LCG seed without revealing it to the verifier?\n")
    verifier = Verifier(seed, n, a, b)
    n_rounds = 128
    for i in range(n_rounds):
        x = verifier.get_secret_bit()
        
        print("Provide state: ")
        try:
            state = int(input()) % n
        except ValueError:
            print("Invalid input!")
            return
        
        if verifier.verify(state, x):
            print(f"Verification passed! {n_rounds - i - 1} rounds remaining")
        else:
            print(b"Verification failed!")
            return

    print(FLAG)
    print(f"You've convinced the verifier you know the LCG seed. {FLAG}")

if __name__ == "__main__":
    main()