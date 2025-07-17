import time
import sys

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_song():
    lyrics = [
        ("\n'Di mo ba ako lilisanin?", 0.11),
        ("Hindi pa ba sapat pagpapahirap sa 'kin? (Damdamin ko)", 0.09),
        ("Hindi na ba ma-mamamayapa?", 0.12),
        ("Hindi na ba ma-mamamayapa?", 0.13),
        ("Hindi na makalaya", 0.18),
        ("Dinadalaw mo 'ko bawat gabi", 0.18),
    ]

    for lyric, speed in lyrics:
        animate_text(lyric, speed)
        time.sleep(0.5)  # jeda antar lirik

if __name__ == "__main__":
    sing_song()