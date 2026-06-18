# ALONE TV — Blogger.com এ Live করার সম্পূর্ণ গাইড
## (বাংলা ধাপে ধাপে নির্দেশিকা)

---

## 🔴 STEP 1: GitHub Repository তৈরি / Update করুন

আপনার `channels.json` এবং `matches.json` ফাইল অবশ্যই GitHub-এ **Public repository**-তে থাকতে হবে।

### যদি ইতিমধ্যে GitHub-এ আপনার repo থাকে:
1. `https://github.com/tawhid2005/Live-Tv-Wesbsite` এ যান
2. নিশ্চিত করুন যে `channels.json` এবং `matches.json` আছে
3. Repository টি **Public** কিনা চেক করুন: Settings > "Public" বেছে নিন

### JSON URL গুলো যা Template এ ব্যবহার হবে:
```
https://raw.githubusercontent.com/tawhid2005/Live-Tv-Wesbsite/main/channels.json
https://raw.githubusercontent.com/tawhid2005/Live-Tv-Wesbsite/main/matches.json
```

> ⚠️ **সতর্কতা:** যদি ভুল URL হয়, চ্যানেল লোড হবে না!

---

## 🔴 STEP 2: Blogger Blog তৈরি করুন

1. **blogger.com** এ যান
2. Google account দিয়ে Login করুন
3. **"Create New Blog"** বাটন click করুন
4. Blog এর তথ্য দিন:
   - **Title:** `ALONE TV - Watch FIFA World Cup 2026 Live Stream Free`
   - **Address:** `alonetv.blogspot.com` (বা যেকোনো available name)
5. **"Create Blog"** বাটন click করুন

---

## 🔴 STEP 3: Template Apply করুন

1. Blogger Dashboard থেকে **"Theme"** এ click করুন
2. **"Edit HTML"** বাটন click করুন
3. **সমস্ত কোড Select করুন** (Ctrl+A)
4. **Delete করুন** (Delete key)
5. `blogger_template.xml` ফাইলটি খুলুন (Notepad দিয়ে)
6. **সমস্ত কোড Copy করুন** (Ctrl+A, তারপর Ctrl+C)
7. Blogger Edit HTML box-এ **Paste করুন** (Ctrl+V)
8. **"Save Theme"** বাটন click করুন

> ✅ **সফল হলে:** Template save হবে এবং blog দেখা যাবে।

---

## 🔴 STEP 4: একটি নতুন Post তৈরি করুন

Blogger-এ Template শুধু theme/design দেয়। **Content দেখাতে হলে একটি Post দরকার।**

1. Dashboard > **"Posts"** > **"New Post"**
2. **Title দিন:** `ALONE TV - Watch FIFA World Cup 2026 Live Stream & Live TV Free`
3. **Body তে লিখুন:** (নিচের SEO content দিন)

```
Watch FIFA World Cup 2026 Live Stream for free on ALONE TV. 
Stream HD live sports, football, cricket and entertainment channels.
```

4. **"Publish"** করুন
5. Homepage এ গেলে website দেখা যাবে ✅

---

## 🔴 STEP 5: SEO Settings করুন

### Blogger Settings > Search preferences:
- **Meta description:** `Watch FIFA World Cup 2026 Live Stream for free. High-definition live sports, football matches, cricket, and top entertainment channels on ALONE TV.`
- **Custom robots.txt** (Settings > Search preferences > Custom robots.txt):
```
User-agent: *
Allow: /
Sitemap: https://alonetv.blogspot.com/sitemap.xml
```

### Custom robots header tags:
- **Homepage:** All ✅, No Index ❌
- **Archive and search pages:** No Index ✅
- **Post and page:** All ✅

---

## 🔴 STEP 6: Google Search Console এ Submit করুন

1. **search.google.com/search-console** এ যান
2. **"Add Property"** > URL prefix
3. URL দিন: `https://alonetv.blogspot.com/`
4. Verify করুন (HTML tag method সহজ)
5. **"Sitemaps"** > Sitemap URL দিন: `sitemap.xml`
6. Submit করুন

> 📈 ৩-৫ দিনের মধ্যে Google Index করবে।

---

## 🔴 STEP 7: Google Analytics (Optional কিন্তু গুরুত্বপূর্ণ)

1. **analytics.google.com** এ account তৈরি করুন
2. Tracking ID নিন (G-XXXXXXXXXX format)
3. Blogger > Settings > Google Analytics Measurement ID তে বসান

---

## 🔴 STEP 8: Custom Domain (Optional - SEO Boost)

Custom domain যেমন `alonetv.com` ব্যবহার করলে Google ranking ভালো হয়:

1. Namecheap/GoDaddy থেকে domain কিনুন
2. Blogger > Settings > Custom domain
3. DNS settings করুন:
   - CNAME: `www` → `ghs.google.com`
   - 4টি A records Google এর IP-তে

---

## ✅ সমস্যা ও সমাধান

| সমস্যা | সমাধান |
|--------|--------|
| চ্যানেল লোড হচ্ছে না | GitHub repo Public কিনা চেক করুন |
| Template save হচ্ছে না | XML syntax error — সম্পূর্ণ কোড আবার paste করুন |
| Ads দেখাচ্ছে না | Ad blocker disable করুন, এবং কিছুক্ষণ অপেক্ষা করুন |
| Video play হচ্ছে না | Stream URL কাজ করছে কিনা চেক করুন |
| Mobile-এ ভাঙা দেখাচ্ছে | Browser cache clear করুন |

---

## 📊 SEO Best Practices যা আমরা করেছি

- ✅ Title Tag optimized (FIFA World Cup 2026 keywords)
- ✅ Meta Description (150 char)
- ✅ JSON-LD Structured Data (WebSite + SportsEvent schema)
- ✅ Open Graph tags (Facebook sharing)
- ✅ Twitter Card tags
- ✅ Canonical URL
- ✅ robots meta tag (index, follow)
- ✅ DNS prefetch for speed
- ✅ Google Fonts preconnect
- ✅ Lazy loading images
- ✅ Semantic HTML (header, main, nav, footer, section, aside)
- ✅ SEO keyword-rich footer content
- ✅ noscript fallback
- ✅ Tag cloud for long-tail keywords
- ✅ sitemap.xml Blogger auto-generate করে

---

## 📢 Ads সঠিকভাবে কাজ করবে কারণ:

- ✅ Desktop 728x90 Banner — Header-এর নিচে
- ✅ Mobile 320x50 Banner — মোবাইলে উপরে
- ✅ Sidebar 300x250 — সব ডিভাইসে
- ✅ Sidebar 160x600 Skyscraper — Desktop only
- ✅ Sidebar 160x300 Half-page — Desktop only
- ✅ 468x60 Below Player — Desktop only
- ✅ Adsterra Native Banner — Grid-এর নিচে
- ✅ Adsterra Popunder — Body শেষে
- ✅ Adsterra Social Bar — Body শেষে
