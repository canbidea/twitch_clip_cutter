import subprocess

# Videonun dosya yolu ve adını belirtin
video_path = "c:/Users/Canberk/Desktop/PY/video.mp4"

# Parçaları almak istediğiniz dakikaları ve süreyi belirtin
dakikalar = [20, 39, 42, 54]  # Parçaları almak istediğiniz dakikaları burada belirtin
parca_suresi = 120  # Her bir parçanın süresini saniye cinsinden belirtin

# Her bir parçayı oluşturun
for dakika in dakikalar:
    baslangic_zamani = (dakika - 1) * 60  # Dakikanın 1 dakika gerisini başlangıç olarak alın
    bitis_zamani = baslangic_zamani + parca_suresi  # Parçanın bitiş zamanını hesaplayın
    
    # FFmpeg'i kullanarak parçayı kesin ve kaydedin
    parca_adi = f"parca_{dakika}-{bitis_zamani}.mp4"  # Parçanın adını oluşturun
    subprocess.call(['ffmpeg', '-i', video_path, '-ss', str(baslangic_zamani), '-t', str(parca_suresi), '-c', 'copy', parca_adi])
    
    print(f"{dakika}-{bitis_zamani} aralığındaki parça oluşturuldu: {parca_adi}")