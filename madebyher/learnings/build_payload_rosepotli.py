import json

path = "/home/hermes/.hermes/workspace/vault/madebyher/learnings/blog_draft_raw_rosepotli.md"
with open(path) as f:
    content = f.read()

lines = content.split("\n")
title = lines[0].lstrip("# ").strip()
body_lines = []
skip_meta = True
for line in lines[1:]:
    if skip_meta and (line.startswith("Target keyword:") or line.startswith("Category:") or line.strip() == ""):
        continue
    skip_meta = False
    body_lines.append(line)
body = "\n".join(body_lines).strip()

excerpt = "A buying guide to crochet rose potli bags: how to spot genuinely handmade rosework, price ranges, care tips, and where the real ones come from."

payload = {
    "title": title,
    "excerpt": excerpt,
    "body": body,
    "seo_keyword": "crochet rose potli bag",
    "category": "Buying Guide",
}

out_path = "/home/hermes/.hermes/workspace/vault/madebyher/learnings/blog_payload_rosepotli.json"
with open(out_path, "w") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(title)
print(len(body.split()))
