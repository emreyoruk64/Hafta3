import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Kamera bağlantısını aç 
cap = cv.VideoCapture(0)  

# İzlenecek nesnenin renk aralığını belirle 
lower_color = np.array([100, 150, 50])  # Alt HSV sınırları
upper_color = np.array([140, 255, 255])  # Üst HSV sınırları

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü HSV renk uzayına çevir
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Belirtilen renk aralığını maskele
    mask = cv.inRange(hsv, lower_color, upper_color)

    # Maskeyi uygula
    result = cv.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri göster
    cv.imshow("Original", frame)
    cv.imshow("Mask", mask)
    cv.imshow("Result", result)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()




cap = cv.VideoCapture(0)

# İlk kareyi oku
ret, frame = cap.read()
if not ret:
    print("Kamera görüntüsü alınamadı!")
    cap.release()
    cv.destroyAllWindows()
    exit()

# ROI (Takip edilecek alanı seç)
roi = cv.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
x, y, w, h = roi
track_window = (x, y, w, h)

# ROI'yi HSV renk uzayına çevir ve histogram oluştur
roi_hsv = cv.cvtColor(frame[y:y+h, x:x+w], cv.COLOR_BGR2HSV)
roi_hist = cv.calcHist([roi_hsv], [0], None, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# CamShift takip kriterleri
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # HSV'ye çevir
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Nesneyi histogram kullanarak takip et
    back_proj = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # CamShift algoritmasını uygula
    ret, track_window = cv.CamShift(back_proj, track_window, term_crit)

    # Takip edilen alanı çiz
    pts = cv.boxPoints(ret)
    pts = np.intp(pts)
    cv.polylines(frame, [pts], True, (0, 255, 0), 2)

    cv.imshow("Tracking", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()





# Örnek hareket verisi (X ve Y koordinatları)
x_positions = [100, 120, 140, 160, 180, 200]
y_positions = [200, 220, 240, 260, 280, 300]

plt.figure(figsize=(6, 6))
plt.plot(x_positions, y_positions, marker="o", linestyle="-", color="b")
plt.title("Nesne Hareket Yolu")
plt.xlabel("X Koordinatı")
plt.ylabel("Y Koordinatı")
plt.grid()
plt.show()

