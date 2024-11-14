# Vietnamese_TextToSpeech_Chrome_Extension
This is a basic Chrome extension for Vietnamese text-to-speech.

## Description
For works, novels, or news, whether in print or online, both domestic and international, prolonged reading or viewing can lead to feelings of laziness, difficulty maintaining focus, and affect eye prescription. Therefore, VietRead is a technology that uses artificial intelligence (AI) to convert text into speech with flexibility, naturalness, and emotion, creating a sense of closeness and authenticity for the listener. By fine-tuning advanced pre-trained models such as xTTS-v2 with Vietnamese data, the system will enhance the quality of the generated speech and ensure it accurately reflects the original text content. The application of Text-to-Speech (TTS) based on deep learning models has developed significantly and achieved speech synthesis quality comparable to that of humans. As a result, advancements in text-to-speech technology can provide essential support across various fields.

## Data
### Data collection
Data is from YouTube videos and crawled by using crawl_data_and_text.py (in folder data_preprocessing). 

### Data processing
After crawling data, 2 stages must be conducted: normalize texts, and normalize audios.

#### Normalize texts
Firstly, using normalize_data_metadataTTS.ipynb (in folder data_preprocessing) to normalize texts in metadata.csv then convert them back to original files (use replace_metadata_files.py in folder data_preprocessing). Secondly, check to spell manually and ensure all audios are matched with their subtitles in metadata.cvs. Finally, convert metadata.cvs to metadata.txt for model training (use normalize_text.py in folder data_preprocessing).

#### Normalize audios
Removing noise and normalizing all audios by using audio_normalize.py (in folder data_preprocessing).

# Model 
Due to the time-consuming data stage, the dataset of audio for training is about 22 hours which is not enough to achieve an optimal model for Vietnamese. More data will be collected in the future to reach 50 hours for better model training (finetuning-vixtts-gpt2.ipynb). 

# Chrome Extention
Folder VietRead is a basic pack of Chrome Extention which is using a laptop to be a local server. This extension uses best_model.pth, vocab.json, and config.json which are outputs of model training. 

<img width="1512" alt="Ảnh màn hình 2024-10-26 lúc 19 29 19" src="https://github.com/user-attachments/assets/7eb28424-5e3d-4713-ac26-824015b86412">










