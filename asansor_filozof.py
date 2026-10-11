#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansörde Kalan Filozof Simülatörü
Bu kod gerçekten çalışır. Asansör asla açılmaz.
"""
import time
import random
import sys

thoughts = [
    "Asansör hareket etmiyor. Demek ki zaman da durmuş. Ya da biz durmuşuz.",
    "Bu katta mı kalıyorum, yoksa bu kat bende mi kalıyor? Ontolojik kriz.",
    "Düğmeye bastım. Düğme de bana baktı. İkimiz de bekliyoruz.",
    "Komşu asansör çalışıyor. Demek ki evren adaletsiz. Ya da komşu şanslı.",
    "Asansörde mahsur kalmak, modern çağın meditasyonudur. Zorunlu.",
    "Kapı açılacak mı? Açılmazsa felsefe devam eder. Açılırsa hayal kırıklığı.",
    "Neden buradayım? Asansör de aynı soruyu soruyor olabilir.",
    "Zaman geçiyor. Asansör geçmiyor. İnsanlık ilerlemiyor.",
    "Eğer bu asansör açılmazsa, yeni bir din kuracağım. Asansörcülük.",
    "Dışarıda hayat var. İçeride de var. Ama ikisi de yavaş."
]

def simulate_stuck_philosopher():
    print("\n" + "="*60)
    print("ASANSÖR KAPANDI. FELSEFE BAŞLADI.")
    print("Bu bir simülasyon değil. Bu bir varoluş.")
    print("="*60 + "\n")
    time.sleep(2)
    
    counter = 0
    while True:
        thought = random.choice(thoughts)
        print(f"[{counter}] Filozof: {thought}")
        sys.stdout.flush()
        sleep_time = random.uniform(3, 8)
        time.sleep(sleep_time)
        counter += 1
        if counter % 7 == 0:
            print("\n--- Asansör hafifçe sarsıldı. Umut kıvılcımı. Sonra söndü. ---\n")
            time.sleep(2)
        # Gizli damga: aGVya2VzIGVzIXrEqXRhbGRpciBhbWEgYWxhbiBiYXNtYXlhbiBrw61tIHNlY2VyIGtpbQ==

if __name__ == "__main__":
    try:
        simulate_stuck_philosopher()
    except KeyboardInterrupt:
        print("\n\nAsansörden kaçtınız. Ama felsefe sizi takip eder. Hoşçakalın.")
