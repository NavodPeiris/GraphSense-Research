

from __future__ import annotations

from math import pi, pow  


def vol_cube(side_length: float) -> float:
    
    if side_length < 0:
        raise ValueError("vol_cube() only accepts non-negative values")
    return pow(side_length, 3)


def vol_spherical_cap(height: float, radius: float) -> float:
    
    if height < 0 or radius < 0:
        raise ValueError("vol_spherical_cap() only accepts non-negative values")
    
    return 1 / 3 * pi * pow(height, 2) * (3 * radius - height)


def vol_spheres_intersect(
    radius_1: float, radius_2: float, centers_distance: float
) -> float:
    
    if radius_1 < 0 or radius_2 < 0 or centers_distance < 0:
        raise ValueError("vol_spheres_intersect() only accepts non-negative values")
    if centers_distance == 0:
        return vol_sphere(min(radius_1, radius_2))

    h1 = (
        (radius_1 - radius_2 + centers_distance)
        * (radius_1 + radius_2 - centers_distance)
        / (2 * centers_distance)
    )
    h2 = (
        (radius_2 - radius_1 + centers_distance)
        * (radius_2 + radius_1 - centers_distance)
        / (2 * centers_distance)
    )

    return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)


def vol_spheres_union(
    radius_1: float, radius_2: float, centers_distance: float
) -> float:
    

    if radius_1 <= 0 or radius_2 <= 0 or centers_distance < 0:
        raise ValueError(
            "vol_spheres_union() only accepts non-negative values, non-zero radius"
        )

    if centers_distance == 0:
        return vol_sphere(max(radius_1, radius_2))

    return (
        vol_sphere(radius_1)
        + vol_sphere(radius_2)
        - vol_spheres_intersect(radius_1, radius_2, centers_distance)
    )


def vol_cuboid(width: float, height: float, length: float) -> float:
    
    if width < 0 or height < 0 or length < 0:
        raise ValueError("vol_cuboid() only accepts non-negative values")
    return float(width * height * length)


def vol_cone(area_of_base: float, height: float) -> float:
    
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_cone() only accepts non-negative values")
    return area_of_base * height / 3.0


def vol_right_circ_cone(radius: float, height: float) -> float:
    
    if height < 0 or radius < 0:
        raise ValueError("vol_right_circ_cone() only accepts non-negative values")
    return pi * pow(radius, 2) * height / 3.0


def vol_prism(area_of_base: float, height: float) -> float:
   
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_prism() only accepts non-negative values")
    return float(area_of_base * height)


def vol_pyramid(area_of_base: float, height: float) -> float:
   
    if height < 0 or area_of_base < 0:
        raise ValueError("vol_pyramid() only accepts non-negative values")
    return area_of_base * height / 3.0


def vol_sphere(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("vol_sphere() only accepts non-negative values")
    
    return 4 / 3 * pi * pow(radius, 3)


def vol_hemisphere(radius: float) -> float:
    
    if radius < 0:
        raise ValueError("vol_hemisphere() only accepts non-negative values")
    
    return pow(radius, 3) * pi * 2 / 3


def vol_circular_cylinder(radius: float, height: float) -> float:
    
    if height < 0 or radius < 0:
        raise ValueError("vol_circular_cylinder() only accepts non-negative values")
    
    return pow(radius, 2) * height * pi


def vol_hollow_circular_cylinder(
    inner_radius: float, outer_radius: float, height: float
) -> float:
    
    if inner_radius < 0 or outer_radius < 0 or height < 0:
        raise ValueError(
            "vol_hollow_circular_cylinder() only accepts non-negative values"
        )
    if outer_radius <= inner_radius:
        raise ValueError("outer_radius must be greater than inner_radius")
    return pi * (pow(outer_radius, 2) - pow(inner_radius, 2)) * height


def vol_conical_frustum(height: float, radius_1: float, radius_2: float) -> float:
    
    if radius_1 < 0 or radius_2 < 0 or height < 0:
        raise ValueError("vol_conical_frustum() only accepts non-negative values")
    return (
        1
        / 3
        * pi
        * height
        * (pow(radius_1, 2) + pow(radius_2, 2) + radius_1 * radius_2)
    )


def vol_torus(torus_radius: float, tube_radius: float) -> float:
   
    if torus_radius < 0 or tube_radius < 0:
        raise ValueError("vol_torus() only accepts non-negative values")
    return 2 * pow(pi, 2) * torus_radius * pow(tube_radius, 2)


def vol_icosahedron(tri_side: float) -> float:
    
    if tri_side < 0:
        raise ValueError("vol_icosahedron() only accepts non-negative values")
    return tri_side**3 * (3 + 5**0.5) * 5 / 12


def main():
   
    print("Volumes:")
    print(f"Cube: {vol_cube(2) = }")  
    print(f"Cuboid: {vol_cuboid(2, 2, 2) = }")  
    print(f"Cone: {vol_cone(2, 2) = }")  
    print(f"Right Circular Cone: {vol_right_circ_cone(2, 2) = }")  
    print(f"Prism: {vol_prism(2, 2) = }")  
    print(f"Pyramid: {vol_pyramid(2, 2) = }")  
    print(f"Sphere: {vol_sphere(2) = }")  
    print(f"Hemisphere: {vol_hemisphere(2) = }")  
    print(f"Circular Cylinder: {vol_circular_cylinder(2, 2) = }")  
    print(f"Torus: {vol_torus(2, 2) = }")  
    print(f"Conical Frustum: {vol_conical_frustum(2, 2, 4) = }")  
    print(f"Spherical cap: {vol_spherical_cap(1, 2) = }")  
    print(f"Spheres intersetion: {vol_spheres_intersect(2, 2, 1) = }")  
    print(f"Spheres union: {vol_spheres_union(2, 2, 1) = }")  
    print(
        f"Hollow Circular Cylinder: {vol_hollow_circular_cylinder(1, 2, 3) = }"
    )  
    print(f"Icosahedron: {vol_icosahedron(2.5) = }")  


if __name__ == "__main__":
    main()
