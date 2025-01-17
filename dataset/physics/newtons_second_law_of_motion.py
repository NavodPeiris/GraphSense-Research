

def newtons_second_law_of_motion(mass: float, acceleration: float) -> float:
    
    force = 0.0
    try:
        force = mass * acceleration
    except Exception:
        return -0.0
    return force


if __name__ == "__main__":
    import doctest

    
    doctest.testmod()

    
    mass = 12.5
    acceleration = 10
    force = newtons_second_law_of_motion(mass, acceleration)
    print("The force is ", force, "N")
