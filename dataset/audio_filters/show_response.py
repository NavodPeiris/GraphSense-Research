from __future__ import annotations

from abc import abstractmethod
from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np


class FilterType(Protocol):
    @abstractmethod
    def process(self, sample: float) -> float:
        pass


def get_bounds(
    fft_results: np.ndarray, samplerate: int
) -> tuple[int | float, int | float]:
    
    lowest = min([-20, np.min(fft_results[1 : samplerate // 2 - 1])])
    highest = max([20, np.max(fft_results[1 : samplerate // 2 - 1])])
    return lowest, highest


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter_type.process(item) for item in inputs]

    filler = [0] * (samplerate - size) 
    outputs += filler
    fft_out = np.abs(np.fft.fft(outputs))
    fft_db = 20 * np.log10(fft_out)

   
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    
    bounds = get_bounds(fft_db, samplerate)
    plt.ylim(max([-80, bounds[0]]), min([80, bounds[1]]))
    plt.ylabel("Gain (dB)")

    plt.plot(fft_db)
    plt.show()


def show_phase_response(filter_type: FilterType, samplerate: int) -> None:
    

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter_type.process(item) for item in inputs]

    filler = [0] * (samplerate - size)  
    outputs += filler
    fft_out = np.angle(np.fft.fft(outputs))

    
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("Phase shift (Radians)")
    plt.plot(np.unwrap(fft_out, -2 * pi))
    plt.show()
