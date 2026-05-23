import cv2
import os
import shutil
import subprocess
import msvcrt
from datetime import datetime

SAVE_DIR = "captures"
REPO_URL = "https://github.com/klawisha/testpy.git"

os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
    input("Press Enter to exit...")
    exit()

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
filename = datetime.now().strftime("%Y%m%d_%H%M%S.mp4")
filepath = os.path.join(SAVE_DIR, filename)

fps = 20.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(filepath, fourcc, fps, (width, height))

print("Recording started")
print("Press S in terminal to save and upload")
print("Press Q in camera window to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)
    cv2.imshow("Research Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8", errors="ignore").lower()

        if key == "s":
            break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Saved: {filepath}")

if not os.path.exists("repo"):
    subprocess.run(["git", "clone", REPO_URL, "repo"], check=True)

shutil.copy(filepath, os.path.join("repo", filename))

os.chdir("repo")

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"Upload {filename}"])
subprocess.run(["git", "push", "--force"], check=True)

os.chdir("..")

try:
    shutil.rmtree(SAVE_DIR)
except Exception as e:
    print("Cleanup error:", e)

print("Temporary files removed")
input("Done. Press Enter to exit...")