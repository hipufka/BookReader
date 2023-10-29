import os
import torch
import torchaudio

def slice_text(text: str) -> list:
    lst = []
    while len(text) > 0:
        lst.append(text[:850])
        text = text[850:]

    return lst


def text_to_speech(text: str, book_name: str, lang='en'):
    device = torch.device('cpu')
    sample_rate = 48000
    torch.set_num_threads(4)

    if lang == 'en':
        path = 'https://models.silero.ai/models/tts/en/v3_en.pt'
        speaker = 'en_0'
        local_file = 'model_en_v3_en_en_0.pt'
    if lang == 'ru':
        path = 'https://models.silero.ai/models/tts/ru/v4_ru.pt'
        speaker = 'baya'
        local_file = 'model_ru_v4_ru_baya.pt'
    if lang == 'ua':
        path = 'https://models.silero.ai/models/tts/ua/v4_ua.pt'
        speaker = 'mykyta'
        local_file = 'model_ua_v4_ua_mykyta.pt'

    if not os.path.isfile(local_file):
        print('Model download started')
        torch.hub.download_url_to_file(path, local_file)

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    print('Text slicing started')
    text_parts = slice_text(text)

    print('Processing started')
    audio = []
    num_iterations = 0

    print("Number of iterations:", len(text_parts))
    for slice in text_parts:
        print(f'Iteration number: {num_iterations}')
        aud = model.apply_tts(text=slice, speaker=speaker, sample_rate=sample_rate)
        audio.append(aud)
        num_iterations += 1

    print("Audio concatenation started")
    audio_concat = audio[0]
    for i in range(1, len(audio)):
        audio_concat = torch.cat((audio_concat, audio[i]), 0)

    print("Audio save started")
    torchaudio.save(book_name + ".wav", audio_concat.unsqueeze(0), sample_rate=sample_rate)
