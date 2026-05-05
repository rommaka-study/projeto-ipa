from gtts import gTTS
import os

# Pasta onde os áudios serão criados
pasta = "audio"
os.makedirs(pasta, exist_ok=True)

# Lista de áudios para gerar
audios = [
    ("fonema_a", "a a a"),
    ("fonema_e", "e e e"),
    ("fonema_e_aberto", "é é é"),
    ("fonema_i", "i i i"),
    ("fonema_o_aberto", "ó ó ó"),
    ("fonema_o_fechado", "ô ô ô"),
    ("fonema_u", "u u u"),
]

print("Gerando áudios...")
for nome, texto in audios:
    caminho = os.path.join(pasta, f"{nome}.mp3")
    tts = gTTS(texto, lang="pt", slow=True)
    tts.save(caminho)
    print(f"✓ {caminho}")

print("Concluído!")
