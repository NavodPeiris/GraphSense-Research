
import logging

import numpy as np
import scipy.fftpack as fft
from scipy.signal import get_window

logging.basicConfig(filename=f"{__file__}.log", level=logging.INFO)


def mfcc(
    audio: np.ndarray,
    sample_rate: int,
    ftt_size: int = 1024,
    hop_length: int = 20,
    mel_filter_num: int = 10,
    dct_filter_num: int = 40,
) -> np.ndarray:
    logging.info(f"Sample rate: {sample_rate}Hz")
    logging.info(f"Audio duration: {len(audio) / sample_rate}s")
    logging.info(f"Audio min: {np.min(audio)}")
    logging.info(f"Audio max: {np.max(audio)}")

    
    audio_normalized = normalize(audio)

    logging.info(f"Normalized audio min: {np.min(audio_normalized)}")
    logging.info(f"Normalized audio max: {np.max(audio_normalized)}")

    
    audio_framed = audio_frames(
        audio_normalized, sample_rate, ftt_size=ftt_size, hop_length=hop_length
    )

    logging.info(f"Framed audio shape: {audio_framed.shape}")
    logging.info(f"First frame: {audio_framed[0]}")

    
    
    window = get_window("hann", ftt_size, fftbins=True)
    audio_windowed = audio_framed * window

    logging.info(f"Windowed audio shape: {audio_windowed.shape}")
    logging.info(f"First frame: {audio_windowed[0]}")

    audio_fft = calculate_fft(audio_windowed, ftt_size)
    logging.info(f"fft audio shape: {audio_fft.shape}")
    logging.info(f"First frame: {audio_fft[0]}")

    audio_power = calculate_signal_power(audio_fft)
    logging.info(f"power audio shape: {audio_power.shape}")
    logging.info(f"First frame: {audio_power[0]}")

    filters = mel_spaced_filterbank(sample_rate, mel_filter_num, ftt_size)
    logging.info(f"filters shape: {filters.shape}")

    audio_filtered = np.dot(filters, np.transpose(audio_power))
    audio_log = 10.0 * np.log10(audio_filtered)
    logging.info(f"audio_log shape: {audio_log.shape}")

    dct_filters = discrete_cosine_transform(dct_filter_num, mel_filter_num)
    cepstral_coefficents = np.dot(dct_filters, audio_log)

    logging.info(f"cepstral_coefficents shape: {cepstral_coefficents.shape}")
    return cepstral_coefficents


def normalize(audio: np.ndarray) -> np.ndarray:
    
    return audio / np.max(np.abs(audio))


def audio_frames(
    audio: np.ndarray,
    sample_rate: int,
    hop_length: int = 20,
    ftt_size: int = 1024,
) -> np.ndarray:

    hop_size = np.round(sample_rate * hop_length / 1000).astype(int)

    
    audio = np.pad(audio, int(ftt_size / 2), mode="reflect")

    
    frame_count = int((len(audio) - ftt_size) / hop_size) + 1

    
    frames = np.zeros((frame_count, ftt_size))

    
    for n in range(frame_count):
        frames[n] = audio[n * hop_size : n * hop_size + ftt_size]

    return frames


def calculate_fft(audio_windowed: np.ndarray, ftt_size: int = 1024) -> np.ndarray:
    
    audio_transposed = np.transpose(audio_windowed)

    
    audio_fft = np.empty(
        (int(1 + ftt_size // 2), audio_transposed.shape[1]),
        dtype=np.complex64,
        order="F",
    )

    
    for n in range(audio_fft.shape[1]):
        audio_fft[:, n] = fft.fft(audio_transposed[:, n], axis=0)[: audio_fft.shape[0]]

    
    return np.transpose(audio_fft)


def calculate_signal_power(audio_fft: np.ndarray) -> np.ndarray:
    
    return np.square(np.abs(audio_fft))


def freq_to_mel(freq: float) -> float:
    
    return 2595.0 * np.log10(1.0 + freq / 700.0)


def mel_to_freq(mels: float) -> float:
    
    return 700.0 * (10.0 ** (mels / 2595.0) - 1.0)


def mel_spaced_filterbank(
    sample_rate: int, mel_filter_num: int = 10, ftt_size: int = 1024
) -> np.ndarray:
    freq_min = 0
    freq_high = sample_rate // 2

    logging.info(f"Minimum frequency: {freq_min}")
    logging.info(f"Maximum frequency: {freq_high}")

    
    filter_points, mel_freqs = get_filter_points(
        sample_rate,
        freq_min,
        freq_high,
        mel_filter_num,
        ftt_size,
    )

    filters = get_filters(filter_points, ftt_size)

    
    
    enorm = 2.0 / (mel_freqs[2 : mel_filter_num + 2] - mel_freqs[:mel_filter_num])
    return filters * enorm[:, np.newaxis]


def get_filters(filter_points: np.ndarray, ftt_size: int) -> np.ndarray:
    num_filters = len(filter_points) - 2
    filters = np.zeros((num_filters, int(ftt_size / 2) + 1))

    for n in range(num_filters):
        start = filter_points[n]
        mid = filter_points[n + 1]
        end = filter_points[n + 2]

        
        filters[n, start:mid] = np.linspace(0, 1, mid - start)

        
        filters[n, mid:end] = np.linspace(1, 0, end - mid)

    return filters


def get_filter_points(
    sample_rate: int,
    freq_min: int,
    freq_high: int,
    mel_filter_num: int = 10,
    ftt_size: int = 1024,
) -> tuple[np.ndarray, np.ndarray]:
    
    fmin_mel = freq_to_mel(freq_min)
    fmax_mel = freq_to_mel(freq_high)

    logging.info(f"MEL min: {fmin_mel}")
    logging.info(f"MEL max: {fmax_mel}")

    
    mels = np.linspace(fmin_mel, fmax_mel, num=mel_filter_num + 2)

    
    freqs = mel_to_freq(mels)

    
    filter_points = np.floor((ftt_size + 1) / sample_rate * freqs).astype(int)

    return filter_points, freqs


def discrete_cosine_transform(dct_filter_num: int, filter_num: int) -> np.ndarray:
    basis = np.empty((dct_filter_num, filter_num))
    basis[0, :] = 1.0 / np.sqrt(filter_num)

    samples = np.arange(1, 2 * filter_num, 2) * np.pi / (2.0 * filter_num)

    for i in range(1, dct_filter_num):
        basis[i, :] = np.cos(i * samples) * np.sqrt(2.0 / filter_num)

    return basis


def example(wav_file_path: str = "./path-to-file/sample.wav") -> np.ndarray:
    from scipy.io import wavfile

    
    sample_rate, audio = wavfile.read(wav_file_path)

    
    return mfcc(audio, sample_rate)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
