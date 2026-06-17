import re

filepath = r"C:\Users\DELL\.gemini\antigravity-ide\brain\6c1c5eb9-7065-4bba-8074-bf8a78f24102\.system_generated\steps\17\content.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Search for mpegts
matches = [m.start() for m in re.finditer(r'mpegts', content, re.IGNORECASE)]
print("mpegts matches found:", len(matches))
for idx in matches:
    print(content[max(0, idx - 100):min(len(content), idx + 200)])
    print("-" * 50)

# Search for ts stream logic or custom hls / player code
ts_matches = [m.start() for m in re.finditer(r'\.ts', content, re.IGNORECASE)]
print("ts matches found:", len(ts_matches))
