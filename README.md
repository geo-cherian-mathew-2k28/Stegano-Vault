<div align="center">

  <h1>🔐 Stegano-Vault</h1>
  
  <p>
    <b>A Lightweight LSB Image Steganography Tool</b>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/badge/Numpy-Array_Manipulation-013243?style=for-the-badge&logo=numpy" />
    <img src="https://img.shields.io/badge/Pillow-Image_Processing-yellow?style=for-the-badge" />
  </p>
  
  <br />

  <p>
    <b>Stegano-Vault</b> is a CLI tool designed to demonstrate the concept of <i>Security through Obscurity</i>. It allows users to embed secret text messages into the Least Significant Bits (LSB) of PNG images, making the data invisible to the naked eye.
  </p>

</div>

<hr />

## ⚡ Features
* **Encodes** text into images without visual distortion.
* **Decodes** hidden messages from carrier images.
* **Efficiency:** Uses `NumPy` for fast pixel-array manipulation.
* **Safety:** Includes a delimiter system to ensure message integrity.

## 🧠 How It Works (The Algorithm)
This tool utilizes **LSB (Least Significant Bit) Substitution**:

1.  **Input:** The tool takes a string (e.g., "Hi") and converts it to binary (`01001000 01101001`).
2.  **Processing:** It iterates through the image pixels. Each pixel has RGB values (e.g., `(255, 100, 50)`).
3.  **Manipulation:** The algorithm changes the **last bit** of the binary representation of the pixel color to match the message bit.
    * *Before:* `1111111`**`1`** (255)
    * *After:* `1111111`**`0`** (254)
4.  **Result:** The color change (1 value difference) is imperceptible to humans, but the data is stored physically in the image file.

## 🛠️ Installation & Usage

### 1. Clone or Download
```bash
    git clone https://github.com/geo-cherian-mathew-2k28/Stegano-Vault.git
    cd Stegano-Vault

Install Dependencies

pip install Pillow numpy
     Run the Tool
     python main.py


⚠️ Important Note
Always use .PNG images. JPEG images use lossy compression, which alters pixel values to save space. This compression will destroy the hidden LSB data. PNG is lossless and preserves the bits exactly as they are.
