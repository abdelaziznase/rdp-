import os
import time
import subprocess

# إعداد بيانات الاتصال بـ RDP
hostname = "147.185.221.20:31106"
username = "runneradmin"
password = "p@ssw0rd!"

# دالة لإعداد الاتصال بـ RDP
def start_rdp():
    # تخزين بيانات الاتصال باستخدام cmdkey
    os.system(f"cmdkey /generic:{hostname} /user:{username} /pass:{password}")
    
    # محاولة بدء الاتصال عبر mstsc (Remote Desktop)
    try:
        print(f"Connecting to {hostname}...")
        subprocess.run(f"mstsc /v:{hostname}", check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {hostname}. Retrying...")
        return False
    return True

# بوت لإعادة الاتصال بـ RDP عند الإغلاق
def rdp_reboot():
    while True:
        # حاول الاتصال بـ RDP
        if not start_rdp():
            # في حال فشل الاتصال، أعد المحاولة بعد فترة
            time.sleep(5)  # انتظر 5 ثواني قبل إعادة المحاولة
        else:
            print(f"Connected to {hostname}")
            # انتظر بعض الوقت (مثلاً 10 دقائق) ثم تحقق إذا كان الاتصال لا يزال قائمًا
            time.sleep(600)  # انتظر 10 دقائق (600 ثانية)

# تشغيل البوت
if __name__ == "__main__":
