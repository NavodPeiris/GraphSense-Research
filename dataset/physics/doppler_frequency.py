

def doppler_effect(
    org_freq: float, wave_vel: float, obs_vel: float, src_vel: float
) -> float:

    if wave_vel == src_vel:
        raise ZeroDivisionError(
            "Division by zero implies vs=v and observer in front of the source"
        )
    doppler_freq = (org_freq * (wave_vel + obs_vel)) / (wave_vel - src_vel)
    if doppler_freq <= 0:
        raise ValueError(
            "Non-positive frequency implies vs>v or v0>v (in the opposite direction)"
        )
    return doppler_freq


if __name__ == "__main__":
    import doctest

    doctest.testmod()
