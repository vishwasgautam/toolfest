# ToolFest 🛠

Free online tools for PDF conversion, image compression, and more.

**Live:** [toolfest.in](https://toolfest.in)

## 📁 Project Structure

```
toolfest/
├── index.html              ← Homepage (all tools)
├── pdf-tools/
│   ├── index.html          ← PDF tools hub
│   ├── word-to-pdf.html    ← Word → PDF converter ✅ WORKING
│   ├── merge-pdf.html
│   ├── compress-pdf.html
│   ├── pdf-to-jpg.html
│   ├── jpg-to-pdf.html
│   └── split-pdf.html
├── image-tools/
│   ├── index.html          ← Image tools hub
│   ├── compress.html       ← Image compressor ✅ WORKING
│   ├── resize.html
│   ├── convert.html
│   ├── crop.html
│   ├── rotate-flip.html
│   └── watermark.html
└── assets/
    └── css/
        └── shared.css
```

## 🚀 Hosting on GitHub Pages

1. Push this repo to GitHub
2. Go to Settings → Pages
3. Set Source to main branch, / (root)
4. Your site is live at https://yourusername.github.io/toolfest/
5. Add your custom domain toolfest.in in Settings → Pages → Custom domain

## 💰 Google AdSense Tips

Each tool has its own URL — this is intentional for AdSense:
- toolfest.in/pdf-tools/word-to-pdf.html → High-intent page, great for ads
- toolfest.in/image-tools/compress.html → High traffic potential

Add this to head after AdSense approval:
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
```

## What works right now

- Word to PDF — Parses .docx XML, renders HTML preview, print-to-PDF download
- Image Compressor — Canvas API compression, batch support, ZIP download, before/after compare
- All pages are SEO-optimized with meta descriptions

## Tools Status

| Tool | Status |
|------|--------|
| Word to PDF | Working |
| Image Compress | Working |
| Image Resize | Shell - add canvas resize |
| Image Convert | Shell - add canvas export |
| Merge PDF | Shell - add pdf-lib.js |
| Compress PDF | Shell - add pdf-lib.js |
