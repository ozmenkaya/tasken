import requests
import sys

def check_url(name, base_url):
    print(f"\nTesting {name} at {base_url}...")
    
    endpoints = [
        ('/', 302),  # Redirects to login usually
        ('/login', 200),
        ('/static/manifest.json', 200),
        ('/api/app-info', 200)
    ]
    
    all_passed = True
    
    for endpoint, expected_status in endpoints:
        url = f"{base_url.rstrip('/')}{endpoint}"
        try:
            response = requests.get(url, timeout=10, allow_redirects=False)
            status = response.status_code
            
            if status == expected_status:
                print(f"✅ {endpoint}: OK ({status})")
            elif expected_status == 302 and status == 200:
                 # Sometimes / redirects to login which returns 200 if we follow redirects, 
                 # but here allow_redirects=False, so we expect 302. 
                 # If it returns 200, maybe it's already the login page?
                 print(f"⚠️ {endpoint}: Got {status}, expected {expected_status}")
            else:
                print(f"❌ {endpoint}: Failed (Got {status}, expected {expected_status})")
                all_passed = False
        except Exception as e:
            print(f"❌ {endpoint}: Error - {str(e)}")
            all_passed = False
            
    return all_passed

if __name__ == "__main__":
    print("--- System Health Check ---")
    
    # 1. Check Local
    local_url = "http://127.0.0.1:5004"
    check_url("Local System", local_url)
    
    # 2. Check Remote (User provided)
    remote_url = "https://tasken.com.tr"
    check_url("Remote Server", remote_url)
