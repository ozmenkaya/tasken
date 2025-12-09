import requests

def test_remote_login():
    url = "https://tasken.com.tr/login"
    print(f"Testing DB connection via Login at {url}...")
    
    # Random credentials to trigger DB lookup
    payload = {
        'username': 'test_connection_check',
        'password': 'random_password_123'
    }
    
    try:
        # Use a session to handle cookies/CSRF if needed, though Flask-WTF might not be strict if not configured
        # The app.py didn't show CSRF protection on the login route explicitly, but let's see.
        # Simple POST first.
        response = requests.post(url, data=payload, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            if "Geçersiz kullanıcı adı veya şifre" in response.text:
                print("✅ Database Connection: OK (Received expected 'Invalid credentials' message)")
            else:
                print("⚠️ Unexpected response content. Database might be down or message changed.")
                # print(response.text[:500]) # Debug
        elif response.status_code == 500:
            print("❌ Database Connection: FAILED (Internal Server Error)")
        else:
            print(f"⚠️ Unexpected Status Code: {response.status_code}")

    except Exception as e:
        print(f"❌ Connection Error: {str(e)}")

if __name__ == "__main__":
    test_remote_login()