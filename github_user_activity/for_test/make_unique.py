import json

# 讀取原始 JSON 檔案並解析成 Python list
with open("sample.json", "r", encoding="utf-8") as f:
    events = json.loads(f.read())

# 建立一個集合來追蹤已出現過的事件類型
seen_types = set()
unique_events = []
c=0
for event in events:
    c+=1
    event_type = event.get("type")
    if event_type not in seen_types:
        unique_events.append(event)
        seen_types.add(event_type)

# 輸出結果到 console
print(json.dumps(unique_events, indent=2))

# 寫入新的 JSON 檔案
with open("unique_events.json", "w", encoding="utf-8") as f:
    json.dump(unique_events, f, indent=2, ensure_ascii=False)

print(c)