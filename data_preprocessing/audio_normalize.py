import os
from pydub import AudioSegment
from noise_remove import removeNoise

def normalize_audio(audio_path, target_sample_rate=22050):
    # Đọc audio
    audio = AudioSegment.from_file(audio_path)

    # Chỉnh sửa sampling rate
    audio = audio.set_frame_rate(target_sample_rate)

    # Chuyển đổi thành mono
    audio = audio.set_channels(1)

    # Ghi đè lên file âm thanh gốc
    audio.export(audio_path, format="wav")


def main(folder_path):
    path = folder_path

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)

                print(file_path)
                # Remove noise
                file_path = removeNoise(file_path)

                # Normalize audio
                normalized_audio = normalize_audio(file_path)

                print(f"Replaced original audio with normalized audio at {file_path}")

if __name__ == "__main__":
    main(r'code/datasets')
