# CodeAlpha AI Internship — Task 1: Language Translation Tool

A beginner-friendly language translation web app built with **Python**, **Streamlit**, and **deep-translator**. Users can enter text, choose a source language (or auto-detect it), select a target language, translate, and download the result as a text file.

## Features

- Simple Streamlit web interface
- Source-language and target-language selectors
- Auto-detect source language
- Translation using the Google Translate service through `deep-translator`
- Empty-input and same-language checks
- Friendly error messages for connection/rate-limit problems
- Output shown in a read-only result box
- Download translated text as `translation.txt`
- Input limit of 5,000 characters
- Basic offline tests using `pytest`

## Project structure

```text
codealpha_language_translation_tool/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_app_helpers.py
```

## Requirements

- Python 3.10 or newer recommended
- Internet connection
- `pip`
- A modern web browser

## Installation and run instructions

### 1. Extract the project

Unzip the downloaded project folder and open a terminal in that folder.

### 2. Create a virtual environment (recommended)

**Windows (Command Prompt):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install libraries

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Main libraries:
- `streamlit` — builds the web interface.
- `deep-translator` — sends text to the translation service and returns translated text.
- `pytest` — runs basic project checks.

### 4. Start the app

```bash
streamlit run app.py
```

Streamlit normally opens the app in your browser. If it does not, copy the local URL printed in the terminal (often `http://localhost:8501`) into your browser.

## How to use

1. Choose the source language, or select **Auto-detect**.
2. Choose the target language.
3. Enter text in the text box.
4. Click **Translate**.
5. Read the result and optionally download it as a `.txt` file.
6. Click **Clear** to reset the input and result.

## Testing

Run the included offline tests from the project root:

```bash
pytest
```

These tests check that the project files and main translation UI are present. They do **not** test the external translation service. To test a real translation, start the app and translate a short sentence while connected to the internet.

Suggested manual test cases:

| Test | Input / action | Expected result |
|---|---|---|
| Empty input | Click Translate with no text | Warning asks you to enter text |
| Hindi to English | Source Hindi, target English; enter `नमस्ते` | English translation is displayed |
| Auto-detect | Source Auto-detect; enter a short sentence | Translation appears in selected target language |
| Same language | Select English for source and target | App warns that languages should differ |
| Download | Translate any short sentence, click download | A `translation.txt` file is downloaded |
| No internet | Disconnect internet and try translating | Friendly error message appears |

Translation wording may vary. The service may also apply request limits.

## GitHub upload instructions

1. Create or sign in to your GitHub account.
2. Create a **public** repository named `CodeAlpha_LanguageTranslationTool` (or another suitable name).
3. In a terminal opened in the project folder, run:

```bash
git init
git add app.py requirements.txt README.md .gitignore tests/
git commit -m "Build CodeAlpha language translation tool"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CodeAlpha_LanguageTranslationTool.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to authenticate, follow GitHub's sign-in instructions. Do not put passwords or access tokens directly into source code.

Alternatively, upload the project files using GitHub's **Add file → Upload files** option.

## Internship submission checklist

- [ ] Run the app and test multiple languages.
- [ ] Make sure `app.py`, `requirements.txt`, and `README.md` are in the repository.
- [ ] Keep the repository name aligned with the internship instructions, if they specify a required naming format.
- [ ] Update this README with your name and any changes you actually made.
- [ ] Record a short screen demonstration showing language selection, translation, and download.
- [ ] Share the real GitHub repository URL in the internship submission form.

## How it works

1. Streamlit collects the source language, target language, and input text.
2. `GoogleTranslator` from `deep-translator` sends the request to the translation service.
3. The returned translation is displayed in the result area.
4. Streamlit's download button lets the user save the result.

## Limitations and privacy

- An internet connection is required for translation and language-list loading.
- This uses an unofficial third-party wrapper around Google Translate, not an official Google Cloud Translation API integration. Availability, supported languages, and rate limits can change.
- Do not submit confidential, personal, or sensitive text.
- For a production or commercial application, consider an official translation API, review its terms, and store credentials securely in Streamlit secrets or environment variables.

## Credits

Created as a learning project for **CodeAlpha AI Internship — Task 1: Language Translation Tool**.
