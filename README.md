# 💾 CacheCopiator

**CacheCopiator** is a toolkit to **record and restore web sessions** using Chrome. It saves cookies, `localStorage`, and `sessionStorage` into a `.json` file and allows you to replay that session at any time.

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
│   └── sesp.exe   # Session restorer
├── cachr.py             # Python source (optional)
├── sesp.py    # Python source (optional)
└── README.md
```
## 🚀 Quick Start (Windows .exe)
1.Download the **latest** release **(CacheCopiatorUtility.zip)** and unzip it to any folder.  

2. Add to PATH (optional, for easy access)  
To run `cachr.exe` and `sesp.exe` from any terminal window, you can add the bin folder to your system PATH:

 - 🔧 How to do it (Windows):  
1. Press `Win + R`, type `sysdm.cpl`, press Enter.  
2. Go to Advanced → Environment Variables.  
3. Under System variables, find and select Path, then click Edit.  
4. Click `New` and paste the full path to the bin folder `(e.g., C:\Users\YourName\CacheCopiatorUtility\bin)`.  
5. Click OK to save.  

Now you can run the tools directly from cmd or PowerShell:

```
cachr --url https://example.com --out session_example.json
sesp --url https://example.com --cache session_example.json
```
## 🐍 Running with Python (Optional)
Install requirements:
```
pip install selenium webdriver-manager
```
Then:

```
python cachr.py --url https://example.com --out session_example.json
python sesp.py --url https://example.com --cache session_example.json
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
Also in newest update I added incognito mode for pages that pop-up in process.

## 🤝 Contributing
Pull requests and suggestions are welcome! Fork it and improve it.

## 📄 License
MIT License

`Made by Jjponvv`
