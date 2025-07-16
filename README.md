# 💾 CashCopiator

**CashCopiator** is a toolkit to **record and restore web sessions** using Chrome. It saves cookies, `localStorage`, and `sessionStorage` into a `.json` file and allows you to replay that session at any time.

No Python installation required — compiled Windows binaries are included!

---

## ⚙️ Features

- 📥 Record session data from any URL (cookies + storage)
- 📤 Replay session later using the same browser context
- 🖱️ CLI or Windows `.exe` support (no Python setup needed)
- 🗃️ Saves to a single JSON file

---

## 🧾 File Structure

```bash
.
├── bin/                 # Precompiled Windows binaries
│   ├── cachr.exe            # Session recorder
│   └── session_pusher.exe   # Session restorer
├── cachr.py             # Python source (optional)
├── session_pusher.py    # Python source (optional)
└── README.md
```
## 🚀 Quick Start (Windows .exe)
1. Add to PATH (optional, for easy access)
To run `cachr.exe` and `session_pusher.exe` from any terminal window, you can add the bin folder to your system PATH:

🔧 How to do it (Windows):
Press `Win + R`, type `sysdm.cpl`, press Enter.

Go to Advanced → Environment Variables.

Under System variables, find and select Path, then click Edit.

Click `New` and paste the full path to the bin folder `(e.g., C:\Users\YourName\cashCopiator\bin)`.

Click OK to save.

Now you can run the tools directly from cmd or PowerShell:

```
cachr --url https://example.com --out session_example.json
session_pusher --url https://example.com --cach session_example.json
```
## 🐍 Running with Python (Optional)
Install requirements:
```
pip install selenium webdriver-manager
```
Then:

```
python cachr.py --url https://example.com 
python session_pusher.py --url https://example.com --cach session_example.json
```
## 📄 Output Format
Each session is saved as a .json file like this:
```
{
  "url": "https://example.com",
  "cookies": [ ... ],
  "localStorage": { ... },
  "sessionStorage": { ... }
}
```
## 🔐 Security Note
Session files may contain sensitive authentication tokens. Do not share them.

## 🤝 Contributing
Pull requests and suggestions are welcome! Fork it and improve it.

## 📄 License
MIT License

`Made by Jjponvv`
