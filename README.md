# 📸 Image Compressor

A simple Python script to compress and downscale images for use on websites. It uses the [Pillow](https://python-pillow.org/) library to resize images while preserving aspect ratio and image quality.

---

## 🔧 Features

- Automatically resizes images that are too wide
- Compresses images to reduce file size
- Lets users customize:
  - 📏 Maximum width (in pixels)
  - 📉 Compression quality (1–100)
- Stores a log of processed files in a `images.json` file

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install Pillow
```

### 2. Run the script

```bash
python imageCompressor.py
```

### 3. Follow the prompts:

```
Enter input folder path (default: ./uncompressed/):
Enter output folder path (default: ./compresssed/):
Enter quality (1-100, default: 85):
Enter max width in pixels (default: 1000):
```

You can press **Enter** to accept the default value for each.

---

## 📂 Example File Structure

```
project/
├── imageCompressor.py
├── images.json
├── uncompressed/
│   ├── image1.jpg
│   └── image2.png
└── compresssed/
    ├── image1.jpg
    └── image2.png
```

---

## 📄 Notes

- The `images.json` file tracks which images have been compressed.
- If the JSON is corrupted or empty, it will be automatically reinitialized.
