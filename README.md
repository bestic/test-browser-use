# test-browser-use

Minimal example project demonstrating the [browser-use](https://github.com/browser-use/browser-use) library.

## Setup

1. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API keys to a `.env` file as described in the browser-use documentation.
4. Run the example:
   ```bash
    python main.py
   ```

This will open `example.com`, capture a screenshot of `div#content` into the
`screenshot` directory and ask the agent whether a smile icon is visible in that
image.
