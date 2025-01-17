

K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5


buffer_space: list[float] = []
params_space: list[float] = []


machine_time = 0


def push(seed):
    global buffer_space, params_space, machine_time, K, m, t

    
    for key, value in enumerate(buffer_space):
        
        e = float(seed / value)

        
        value = (buffer_space[(key + 1) % m] + e) % 1

        
        r = (params_space[key] + e) % 1 + 3

        
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = r  

    
    assert max(buffer_space) < 1
    assert max(params_space) < 4

    
    machine_time += 1


def pull():
    global buffer_space, params_space, machine_time, K, m, t

    
    def xorshift(x, y):
        x ^= y >> 13
        y ^= x << 17
        x ^= y >> 5
        return x

    
    key = machine_time % m

    
    for _ in range(t):
        
        r = params_space[key]
        value = buffer_space[key]

        
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = (machine_time * 0.01 + r * 1.01) % 1 + 3

    
    x = int(buffer_space[(key + 2) % m] * (10**10))
    y = int(buffer_space[(key - 2) % m] * (10**10))

    
    machine_time += 1

    return xorshift(x, y) % 0xFFFFFFFF


def reset():
    global buffer_space, params_space, machine_time, K, m, t

    buffer_space = K
    params_space = [0] * m
    machine_time = 0


if __name__ == "__main__":
    
    reset()

    
    import random

    message = random.sample(range(0xFFFFFFFF), 100)
    for chunk in message:
        push(chunk)

    
    inp = ""

    
    while inp in ("e", "E"):
        print(f"{format(pull(), '#04x')}")
        print(buffer_space)
        print(params_space)
        inp = input("(e)exit? ").strip()
