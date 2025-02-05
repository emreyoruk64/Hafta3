# Ödev 3 
# data.txt
with open("data.txt", "w", encoding="utf-8") as file:
    veri = input("Kaydedilecek veriyi giriniz: ")
    file.write(veri)

with open("data.txt", "r", encoding="utf-8") as file:
    okunan_veri = file.read()
    print("Dosyadan okunan veri:", okunan_veri)

# JSON Dosyası
import json

data = {"isim": "Burak", "yas": 35, "sehir": "Şanlıurfa"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSON dosyası oluşturuldu ve veri yazıldı.")

with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)
    print("Dosyadan okunan veri:", json_data)

json_data["yas"] += 5  
json_data["sehir"] = "Uşak"  

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print("Veri güncellendi ve dosyaya kaydedildi.")
