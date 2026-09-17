import json

body = open("/home/hermes/.hermes/workspace/vault/madebyher/learnings/blog_draft_raw_makhana.md").read()
lines = body.split("\n")
assert lines[0].startswith("# ")
title = lines[0][2:].strip()
rest = "\n".join(lines[1:]).strip()

payload = {
    "title": title,
    "excerpt": "A buying guide to Bihar's fox nut superfood: what makhana is, how to judge quality online, GI-tagged Mithila sourcing, and how to store it.",
    "body": rest,
    "seo_keyword": "makhana online",
    "category": "Buying Guide",
}

with open("/home/hermes/.hermes/workspace/vault/madebyher/learnings/blog_payload_makhana.json", "w") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(title)
print(len(rest.split()))
