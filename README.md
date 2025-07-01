# 🔐 File Encryption Tool (Python)

A simple command-line tool to encrypt and decrypt files using symmetric AES encryption via the `cryptography` package.

Each file gets its own key (`filename.key`), so you can securely send encrypted files and keys separately — ideal for backups, sharing, or protection from ransomware(being in hostage only).

---

## 💡 Features

- ✅ Lists all files in your folder (excluding scripts and keys)
- 🔒 Encrypts any file using a one-time key (saved as `filename.key`)
- 🔓 Decrypts files using the correct `.key` file
- 💾 All offline — no network or server used

---

## 🛠 How to Use

1. Clone the repository  
2. Run the script:

```bash
python encryption_tool.py
```

### Choose:

[1] List files
[2] Encrypt a file (creates file.key)
[3] Decrypt a file (uses file.key)
[4] Exit


### 🧠 Example Use Case
Imagine you want to email a sensitive document:
Encrypt report.pdf → sends report.pdf (encrypted)
Save/send report.pdf.key through a different channel (e.g., USB, messenger)
The receiver uses the script + key to decrypt it


###⚠️ Notes
Do not delete the .key file if you plan to decrypt later
Each file uses a unique key — no global key management
This is for educational or personal use, not enterprise-grade encryption



