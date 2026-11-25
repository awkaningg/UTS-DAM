import requests
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

TARGET = "https://museumnasional.or.id/"

UA = "Nining-UTS-DAM/1.0 (clementincmharum@gmail.com)"

def cek_kepatuhan(url, user_agent=UA):
    p = urlparse(url)
    base = f"{p.scheme}://{p.netloc}"
    rp = RobotFileParser()
    rp.set_url(base + "/robots.txt")
    try:
        rp.read()
        isi = requests.get(base + "/robots.txt", timeout=10).text
    except Exception as e:
        return {"error": str(e)}
    
    return {
        "url": url,
        "boleh_diakses": rp.can_fetch(user_agent, url),
        "crawl_delay": rp.crawl_delay(user_agent),
        "isi_robots_txt": isi[:300],
    }

hasil = cek_kepatuhan(TARGET)
for k, v in hasil.items():
    print(f"{k}: {v}\n")
