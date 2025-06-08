# 🚉 Corpus-Based Speech Synthesizer for Train Announcements

This application generates spoken train announcements for **Warszawa Centralna** by stitching together pre-recorded `.wav` audio files using a simple concatenative synthesis method.

---

## 📁 Application Folder Structure

The main folder must contain three required subfolders for audio files:

### 🎯 Required Folders

- `stacje`  
- `perony_i_tory`  
- `do_z_stacji`  

These correspond to the `AUDIO_DIRS` variable in the Python script.

---

## 🎵 Audio File Guidelines

Each folder should include `.wav` files with speech recordings for phrases or words that may appear in a user-provided Polish announcement.

### ✅ File Naming Rules

- All names must be in **lowercase**
- Polish diacritics must be **removed**  
  (e.g. `ł` → `l`, `ó` → `o`, `ż` → `z`, etc.)
- **Use underscores** (`_`) to separate words
- The file name (without `.wav`) must **exactly match** the normalized input phrase

---

### 📌 Example Structure

```bash
speech_synthesis/
├── do_z_stacji/
│ ├── do_stacji.wav
│ └── pociag_do_stacji.wav
│
├── perony_i_tory/
│ ├── drugiego.wav
│ └── drugim.wav
│
├── stacje/
│├── poznan_glowny.wav
│└── warszawa_wschodnia.wav
└─ main.py
```

---

## ▶️ Usage

The user enters a sentence in Polish, and the program:

1. Normalizes the text (lowercase, removes Polish characters, etc.)
2. Searches for matching audio fragments
3. Plays the complete announcement
4. Reports any missing segments

---

## 🛠️ Dependencies

Install required packages:

```bash
pip install pydub simpleaudio