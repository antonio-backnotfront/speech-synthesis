import os
import re
from pydub import AudioSegment
from pydub.playback import play

# Polish diacritic map
POLISH_CHAR_MAP = str.maketrans({
    'ą': 'a', 'ę': 'e', 'ć': 'c', 'ł': 'l',
    'ó': 'o', 'ż': 'z', 'ź': 'z', 'ń': 'n', 'ś': 's'
})

AUDIO_DIRS = [
    "stacje",
    "perony_i_tory",
    "do_z_stacji"
]

def normalize_text(text):
    text = text.lower().translate(POLISH_CHAR_MAP)
    text = re.sub(r"[^\w\s]", "", text)
    return text

def find_audio(phrase):
    filename = phrase.replace(" ", "_") + ".wav"
    for folder in AUDIO_DIRS:
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            return AudioSegment.from_wav(path)
    return None

def synthesize_speech(text):
    words = normalize_text(text).split()
    i = 0
    result = AudioSegment.empty()
    missing = []

    while i < len(words):
        found = False
        for j in range(min(5, len(words) - i), 0, -1):
            phrase = " ".join(words[i:i + j])
            audio = find_audio(phrase)
            if audio:
                result += audio
                i += j
                found = True
                break
        if not found:
            missing.append(words[i])
            i += 1

    return result, missing

if __name__ == "__main__":
    user_input = input("Wpisz komunikat po polsku:\n")
    audio, missing = synthesize_speech(user_input)

    if missing:
        print("Nie znaleziono nagrań dla następujących słów/fraz:")
        print(", ".join(missing))
    else:
        print("Odtwarzanie komunikatu...")
        play(audio)
