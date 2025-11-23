# OneSignal iOS Bildirim Ayarları Rehberi

Bu rehber, uygulamanızın iOS cihazlarda bildirim alabilmesi için gereken ayarları içerir.

## ⚠️ ÖNEMLİ: Hangi Yöntemi Kullanıyorsunuz?

Uygulamanızın çalışma şekline göre yapmanız gerekenler değişir:

### DURUM 1: Web Uygulaması / PWA (Tarayıcı Üzerinden)
Eğer kullanıcılarınız sitenize Safari'den girip **"Ana Ekrana Ekle" (Add to Home Screen)** diyerek kullanıyorsa:
*   **APNs Sertifikasına (Apple Developer Hesabı) İHTİYACINIZ YOKTUR.**
*   iOS 16.4 ve üzeri sürümlerde, web uygulamaları (PWA) standart Web Push teknolojisini kullanır.
*   Mevcut OneSignal Web kurulumunuz (Chrome/Firefox ile aynı) iOS'ta da çalışır.
*   **Tek Şart:** Kullanıcının uygulamayı "Ana Ekrana Ekle"mesi gerekir.

### DURUM 2: Native iOS Uygulaması (App Store)
Eğer uygulamanızı **App Store**'a yükleyecekseniz (Swift, Capacitor, React Native vb. ile paketleyip):
*   **APNs (Apple Push Notification Service) Sertifikası GEREKLİDİR.**
*   Aşağıdaki adımları takip etmelisiniz.

---

## Native iOS Uygulaması İçin APNs Kurulumu (Sadece Durum 2 İçin)

Eğer App Store için uygulama geliştiriyorsanız bu adımları uygulayın:

### 1. Sertifika İstek Dosyası (CSR) Oluşturma
1. Mac bilgisayarınızda **Keychain Access (Anahtar Zinciri Erişimi)** uygulamasını açın.
2. Menüden **Certificate Assistant** > **Request a Certificate from a Certificate Authority** seçin.
3. E-posta adresinizi girin, "Saved to disk" seçeneğini işaretleyin ve kaydedin (`CertificateSigningRequest.certSigningRequest`).

### 2. Apple Developer Portal Ayarları
1. [Apple Developer Portal](https://developer.apple.com/account) adresine gidin.
2. **Certificates, Identifiers & Profiles** > **Identifiers** kısmına gidin.
3. Uygulamanızın App ID'sini bulun (yoksa oluşturun).
4. **Push Notifications** özelliğini işaretleyin ve kaydedin.
5. **Certificates** sekmesine gidin, **+** butonuna basın.
6. **Apple Push Notification service SSL (Sandbox & Production)** seçeneğini seçin.
7. App ID'nizi seçin ve oluşturduğunuz CSR dosyasını yükleyin.
8. Oluşan sertifikayı (`aps.cer`) indirin.

### 3. .p12 Dosyası Oluşturma
1. İndirdiğiniz `.cer` dosyasına çift tıklayarak Keychain'e ekleyin.
2. Keychain Access'te sertifikayı bulun (genellikle "Apple Push Services" adıyla başlar).
3. Sertifikaya sağ tıklayın ve **Export** deyin.
4. `.p12` formatında kaydedin ve bir şifre belirleyin.

### 4. OneSignal Ayarları
1. OneSignal panelinde uygulamanızı seçin.
2. **Settings** > **Platforms** > **Apple iOS** kısmına gidin.
3. Oluşturduğunuz `.p12` dosyasını yükleyin.
4. Belirlediğiniz şifreyi girin.
5. **Save** butonuna tıklayın.

Artık OneSignal, Apple cihazlarına native bildirim gönderebilir.
