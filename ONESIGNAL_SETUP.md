# OneSignal Entegrasyonu Kurulumu

OneSignal bildirimlerinin çalışması için aşağıdaki adımları takip edin:

## 1. OneSignal Hesabı Oluşturun
1. [OneSignal](https://onesignal.com/) adresine gidin ve hesap oluşturun.
2. Yeni bir "App" oluşturun (Web Push seçeneğini seçin).
3. "Site Setup" adımında site URL'nizi girin (Localhost için `http://localhost:5004` veya sunucu IP'niz).

## 2. API Anahtarlarını Alın
1. OneSignal panelinde **Settings** > **Keys & IDs** menüsüne gidin.
2. `ONESIGNAL_APP_ID` ve `REST API KEY` değerlerini kopyalayın.

## 3. .env Dosyasını Güncelleyin
Proje ana dizinindeki `.env` dosyasını açın ve aşağıdaki satırları ekleyin:

```bash
ONESIGNAL_APP_ID=sizin-app-id-degeriniz
ONESIGNAL_API_KEY=sizin-api-key-degeriniz
```

## 4. Uygulamayı Yeniden Başlatın
Değişikliklerin aktif olması için servisi yeniden başlatın:

```bash
sudo systemctl restart tasken
# veya
gunicorn -c gunicorn.conf.py app:app
```

## Bildirim Senaryoları
Sistem şu durumlarda otomatik bildirim gönderir:
- **Yeni Görev:** Görev atanan kişilere.
- **Görev Tamamlandı:** Görevi oluşturan kişiye.
- **Durum Değişikliği:** Görevi oluşturan kişiye.
- **Yeni Yorum:** Görevdeki diğer kişilere ve oluşturana.
- **Görev Silindi:** Görevdeki kişilere.
