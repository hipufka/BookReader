import os
import logging
import torch
import torchaudio

logging.basicConfig(level=logging.INFO)
SLICE_LEN = 850

models = {'en': ('https://models.silero.ai/models/tts/en/v3_en.pt',
                 'en_0',
                 'model_en_v3_en_en_0.pt'),
          'ua': ('https://models.silero.ai/models/tts/ua/v4_ua.pt',
                 'mykyta',
                 'model_ua_v4_ua_mykyta'),
          'ru': ('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                 'baya',
                 'model_ru_v4_ru_baya.pt')
          }


def slice_text(text: str) -> list:
    lst = []
    while len(text) > 0:
        lst.append(text[:SLICE_LEN])
        text = text[SLICE_LEN:]

    return lst


def text_to_speech(text: str, book_name: str, lang='en'):
    device = torch.device('cpu')
    sample_rate = 48000
    torch.set_num_threads(4)

    path = models[lang][0]
    speaker = models[lang][1]
    local_file = models[lang][2]

    if not os.path.isfile(local_file):
        logging.info('Model download started')
        torch.hub.download_url_to_file(path, local_file)

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    logging.info('Text slicing started')
    text_parts = slice_text(text)

    logging.info('Processing started')
    audio = []
    num_iterations = 0

    logging.info("Number of iterations: %s", len(text_parts))
    for slice in text_parts:
        logging.info('Iteration number: %s', num_iterations)
        aud = model.apply_tts(text=slice, speaker=speaker, sample_rate=sample_rate)
        audio.append(aud)
        num_iterations += 1

    logging.info("Audio concatenation started")
    audio_concat = audio[0]
    for i in range(1, len(audio)):
        audio_concat = torch.cat((audio_concat, audio[i]), 0)

    logging.info("Audio save started")
    torchaudio.save(book_name + ".wav", audio_concat.unsqueeze(0), sample_rate=sample_rate)
    logging.info("Audio save finished")
