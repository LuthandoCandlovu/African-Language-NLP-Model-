import random
import pandas as pd

# Sample isiZulu words/phrases for different sentiments
positive_phrases = [
    "Ngiyakuthanda", "Kuhle kakhulu", "Ngiyajabula", "Siyakwamukela",
    "Kumnandi", "Ngiyabonga", "Kuhle", "Siyajabula", "Yinhle", "Ngiyayithanda"
]
neutral_phrases = [
    "Kulungile", "Angazi", "Kunjani", "Yini lokhu", "Kungenzeka",
    "Mhlawumbe", "Ngicabanga", "Kusho ukuthini", "Kuyaphawuleka", "Okunye"
]
negative_phrases = [
    "Angijabule", "Akukuhle", "Ngiyakhathazeka", "Kubi", "Angithandi",
    "Kuyangikhathaza", "Angiyithandi", "Kuyangicasula", "Kunzima", "Kabi"
]

# Create 1000 samples
samples = []
for i in range(1000):
    sentiment = random.choice(["positive", "neutral", "negative"])
    if sentiment == "positive":
        phrase = random.choice(positive_phrases)
        label = 2
    elif sentiment == "neutral":
        phrase = random.choice(neutral_phrases)
        label = 1
    else:
        phrase = random.choice(negative_phrases)
        label = 0
    # Add some variation: sometimes add extra words
    if random.random() > 0.5:
        phrase += " " + random.choice(["manje", "kakhulu", "impela", "nje", "kancane"])
    samples.append({"text": phrase, "label": label})

# Shuffle and save
df = pd.DataFrame(samples)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("data/raw/synthetic_zulu.csv", index=False)
print(f"✅ Generated {len(df)} synthetic isiZulu samples in data/raw/synthetic_zulu.csv")
print(df['label'].value_counts())
