import librosa
import numpy as np
from nltk.tokenize import SyllableTokenizer
from nltk.tokenize import word_tokenize
# nltk.download('punkt')

# Load the audio file
y, sr = librosa.load('as-it-was.wav')

# Extract pitches and magnitudes
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# Select the predominant pitch at each time step
predominant_pitches = [np.max(pitch) for pitch in pitches.transpose() if np.max(pitch) > 0]
print(len(predominant_pitches))

# Step 2: Generate Lyrics
# Ask GPT 3.5 on website, then paste it into txt file.
lyrics = open('./lyrics.txt', "r", encoding='utf-8')
lyric = ""
# print(lyrics)
for l in lyrics:
    lyric = lyric + l
melody_length = len(pitches)
lyrics_padded = []

# Step 3: Align Lyrics with Melody
# For simplicity, assume one note per syllable
sst = SyllableTokenizer()

def split_lyrics_into_syllables(lyrics):
    """
    Split lyrics into syllables.
    """
    stopwords = [',', '.', '\'', '’']
    tokens = word_tokenize(lyrics)  # Tokenize the lyrics into words
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
    # print(filtered_tokens)
    syllables = []
    for token in filtered_tokens:
        syllable = sst.tokenize(token)
        # print(syllable_count_word)
        syllables.append(syllable)
    return syllables

lyrics_syllables = split_lyrics_into_syllables(lyric) 
# print(lyrics_syllables)

# Flatten the syllables list
flat_lyrics_syllables = [syllable for word in lyrics_syllables for syllable in word]

# Calculate the number of syllables to pad
padding_needed = melody_length - len(flat_lyrics_syllables)

# Pad the syllables list if needed
if padding_needed > 0:
    flat_lyrics_syllables.extend(['la'] * padding_needed)
# If padding_needed is negative, truncate the list
else:
    flat_lyrics_syllables = flat_lyrics_syllables[:melody_length]

# Pair each pitch with a syllable
aligned_lyrics = list(zip(predominant_pitches, flat_lyrics_syllables))

# Output the aligned lyrics
with open('aligned_lyrics.txt', 'w') as file:
    for pitch, syllable in aligned_lyrics:
        # Check if 'pitch' is a NumPy array and convert it to a scalar if it contains only one item
        pitch_value = pitch.item() if isinstance(pitch, np.ndarray) and pitch.size == 1 else pitch
        # print(f"Pitch: {pitch_value:.2f} Hz -> Syllable: {syllable}")
        file.write(f"Pitch: {pitch_value:.2f} Hz -> Syllable: {syllable}\n")