
from collections import namedtuple

Particle = namedtuple("Particle", "x y z mass")  
Coord3D = namedtuple("Coord3D", "x y z")  


def center_of_mass(particles: list[Particle]) -> Coord3D:
    if not particles:
        raise ValueError("No particles provided")

    if any(particle.mass <= 0 for particle in particles):
        raise ValueError("Mass of all particles must be greater than 0")

    total_mass = sum(particle.mass for particle in particles)

    center_of_mass_x = round(
        sum(particle.x * particle.mass for particle in particles) / total_mass, 2
    )
    center_of_mass_y = round(
        sum(particle.y * particle.mass for particle in particles) / total_mass, 2
    )
    center_of_mass_z = round(
        sum(particle.z * particle.mass for particle in particles) / total_mass, 2
    )
    return Coord3D(center_of_mass_x, center_of_mass_y, center_of_mass_z)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
