#!/bin/bash
cd /home/hermes/.hermes/workspace/vault/madebyher/learnings
> keyword_research_raw.json
for seed in "madhubani painting" "sikki grass jewelry" "sujni embroidery" "chhath gifts" "handmade gifts india" "bihar handicrafts" "artisan jewelry" "bihar food products" "crochet gifts" "handmade cosmetics india" "women artisans bihar"; do
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$seed'))")
  curl -s "https://suggestqueries.google.com/complete/search?client=firefox&q=$encoded" >> keyword_research_raw.json
  echo "" >> keyword_research_raw.json
done
echo "DONE"
