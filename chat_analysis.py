import re
from collections import defaultdict

# Metin dosyasının adını ve yolunu belirtin
chat_log_path = "c:/Users/Canberk/Desktop/PY/chat.log"

# Her bir dakikadaki mesaj sayısını tutacak bir sözlük oluşturun
message_counts = defaultdict(int)

# Metin dosyasını açın ve satır satır okuyun
with open(chat_log_path, "r", encoding="utf-8") as file:
    for line in file:
        # Her satırı düzenli ifade ile tarih ve mesaj olarak ayırın
        match = re.search(r"\[(.*?)\] (.*?): (.*)", line)
        if match:
            timestamp = match.group(1)
            message = match.group(3)
            
            # Sadece dakika bilgisini alın
            minutes = int(timestamp.split(":")[1])
            
            # Dakikadaki mesaj sayısını güncelle
            message_counts[minutes] += 1

# Dakika başına düşen mesaj sayısını hesaplayın
average_message_count = sum(message_counts.values()) / len(message_counts)

# Ortalamanın üzerindeki dakikaları bulun
highlighted_minutes = [minute for minute, count in message_counts.items() if count > average_message_count]

# Sonuçları yazdırın
print("Dakika Başına Ortalama Mesaj Sayısı:", average_message_count)
print("Ortalamanın Üzerindeki Dakikalar:")
for minute in highlighted_minutes:
    print(f"Dakika: {minute}, Mesaj Sayısı: {message_counts[minute]}")