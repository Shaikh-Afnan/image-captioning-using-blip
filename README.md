# AI Image Captioning Web App 🖼️🤖

An AI-powered web application that generates natural language descriptions for images using a transformer-based vision-language model.

---

## 📌 Overview

This project demonstrates the application of deep learning and natural language processing techniques to understand visual content and automatically generate descriptive captions. A pre-trained BLIP transformer model is used to perform image-to-text generation without the need for additional training.

The web interface is built using Gradio, enabling quick interaction and easy experimentation.

---

## 🚀 Features

- Upload images in JPG or PNG format
- Generate meaningful captions using a transformer model
- Real-time inference
- Simple and interactive Gradio interface
- Pre-trained model with no additional training required

---

## 🧠 Model Used

- **BLIP (Bootstrapped Language Image Pretraining)**
- Pre-trained vision-language model from Hugging Face

---

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Gradio
- **Deep Learning:** PyTorch
- **Model Library:** Hugging Face Transformers
- **Image Processing:** Pillow, NumPy

---

## 📂 Project Structure

```
image-captioning-using-blip/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository

```bash
git clone https://github.com/Shaikh-Afnan/image-captioning-using-blip.git
cd image-captioning-using-blip
```

2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

▶️ Run the Application

```bash
python app.py
```

After execution, a Gradio interface will open in your browser.

---

## ⚠️ Limitations

* Caption quality depends on image clarity
* Complex scenes may produce generic captions
* Performance depends on system memory and CPU

---

## 🔮 Future Enhancements

* Batch image captioning
* Multilingual caption support
* Streamlit / Hugging Face Spaces deployment
* GPU acceleration

---

## 👤 Author

**Afnan Shaikh**

Aspiring Data Scientist

---

## 📄 License

This project is created for educational and learning purposes.
