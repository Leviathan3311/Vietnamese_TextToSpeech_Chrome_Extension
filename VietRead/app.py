from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import torch
import torchaudio
from tqdm import tqdm
from underthesea import sent_tokenize
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from TTS.vocoder.models.gan import GAN as HiFiGAN


app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}}) 

# Device configuration
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Model paths
xtts_checkpoint = "VietRead/best_model.pth"
xtts_config = "VietRead/config.json"
xtts_vocab = "VietRead/vocab.json"
checkpoint_dir = "VietRead"

# Load model
config = XttsConfig()
config.load_json(xtts_config)
XTTS_MODEL = Xtts.init_from_config(config)
XTTS_MODEL.load_checkpoint(config, checkpoint_path=xtts_checkpoint, vocab_path=xtts_vocab, checkpoint_dir=checkpoint_dir, use_deepspeed=False)
XTTS_MODEL.to(device)

print("Model loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Sử dụng get_json để nhận dữ liệu JSON
    text = data.get('text')
    voice = data.get('voice')  # Lấy giọng nói đã chọn

    if text is not None:
        # Đường dẫn tới audio mẫu dựa vào lựa chọn giọng
        speaker_audio_file = "VietRead/vi_sample_male.wav" if voice == "male" else "VietRead/vi_sample.wav"
        lang = "vi"
        output_file_path = "VietRead/audio/output_audio.wav"

        # Get conditioning latents
        gpt_cond_latent, speaker_embedding = XTTS_MODEL.get_conditioning_latents(
            audio_path=speaker_audio_file,
            gpt_cond_len=XTTS_MODEL.config.gpt_cond_len,
            max_ref_length=XTTS_MODEL.config.max_ref_len,
            sound_norm_refs=XTTS_MODEL.config.sound_norm_refs,
        )

        tts_texts = sent_tokenize(text)
        
        # Generate audio chunks
        wav_chunks = []
        for text_chunk in tqdm(tts_texts):
            wav_chunk = XTTS_MODEL.inference(
                text=text_chunk,
                language=lang,
                gpt_cond_latent=gpt_cond_latent,
                speaker_embedding=speaker_embedding,
                temperature=0.1,
                length_penalty=1.0,
                repetition_penalty=10.0,
                top_k=10,
                top_p=0.3,
            )
            wav_chunks.append(torch.tensor(wav_chunk["wav"]))
        
        # Concatenate and save the output audio
        out_wav = torch.cat(wav_chunks, dim=0).unsqueeze(0).cpu()
        torchaudio.save(output_file_path, out_wav, 24000)
        print(f"Audio saved successfully as {output_file_path}")

        # Trả về đường dẫn audio cho client
        return jsonify({'output_audio': f'/audio/{output_file_path.split("/")[-1]}'})

    else:
        return jsonify({'error': 'Input text not provided.'})


if __name__ == '__main__':
    app.run(debug=True) 
