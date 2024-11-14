import torchaudio
from df.enhance import enhance, init_df, load_audio, save_audio



def removeNoise(filename):
    # Specify the backend, e.g., 'soundfile' or 'sox_io'
    torchaudio.set_audio_backend("soundfile")

    # Load default model
    model, df_state, _ = init_df()

    audio_path = filename

    audio, _ = load_audio(audio_path, sr=df_state.sr())
    # Denoise the audio
    enhanced = enhance(model, df_state, audio)
    # Save for listening
    save_audio(filename, enhanced, df_state.sr())

    return audio_path

# if __name__ == "__main__":
    
    