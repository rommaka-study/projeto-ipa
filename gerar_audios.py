from gtts import gTTS
import os

# ============================================
# CONFIGURAÇÃO
# ============================================
DURACAO = 3  # segundos

# Lista de todos os fonemas
fonemas = [
    # Módulo 1: Vogais Orais
    ("modulo-01-vogais/licao-01-fonema-a", "fonema_a", "a a a"),
    ("modulo-01-vogais/licao-02-fonema-e", "fonema_e", "e e e"),
    ("modulo-01-vogais/licao-03-fonema-e-aberto", "fonema_e_aberto", "é é é"),
    ("modulo-01-vogais/licao-04-fonema-i", "fonema_i", "i i i"),
    ("modulo-01-vogais/licao-05-fonema-o-aberto", "fonema_o_aberto", "ó ó ó"),
    ("modulo-01-vogais/licao-06-fonema-o-fechado", "fonema_o_fechado", "ô ô ô"),
    ("modulo-01-vogais/licao-07-fonema-u", "fonema_u", "u u u"),
]

# Pasta base
base = "cursos/portugues-brasileiro"

print("=" * 50)
print("GERANDO ÁUDIOS DO PROJETO IPA")
print("=" * 50)

for pasta, arquivo, texto in fonemas:
    destino = os.path.join(base, pasta, "audio")
    os.makedirs(destino, exist_ok=True)
    
    caminho = os.path.join(destino, f"{arquivo}.mp3")
    
    print(f"Gerando: {arquivo}.mp3...", end=" ")
    tts = gTTS(texto, lang="pt", slow=True)
    tts.save(caminho)
    print("✓")

print("=" * 50)
print("TODOS OS ÁUDIOS FORAM GERADOS!")
print(f"Total: {len(fonemas)} arquivos")
print("=" * 50)
