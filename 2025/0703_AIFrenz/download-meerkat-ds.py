#!/usr/bin/env python3
"""
download meerkat dataset from hugginface 
https://huggingface.co/datasets/dmis-lab/meerkat-instructions
"""

import os
import requests
from tqdm import tqdm

def main():
    # 1) compute output dir relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(script_dir, "../../data_meerkat"))
    os.makedirs(output_dir, exist_ok=True)

    # 2) Hugging Face raw file URL base
    base_url = "https://huggingface.co/datasets/dmis-lab/meerkat-instructions/resolve/main/"

    # 3) list all files in the repo
    files = [
        "chatdoctor-cleaned.jsonl",
        "liveqa.jsonl",
        "medbooks-18-cot.jsonl",
        "medicationqa.jsonl",
        "medinstruct-52k.jsonl",
        "medmcqa.jsonl",
        "medqa-cot.jsonl",
        "medqa-dialog.jsonl",
        "mts-dialog.jsonl",
    ]

    # 4) download each, with a progress bar
    for fname in files:
        dest = os.path.join(output_dir, fname)
        if os.path.exists(dest):
            print(f"[skip] {fname} already exists")
            continue

        print(f"[download] {fname}")
        resp = requests.get(base_url + fname, stream=True)
        resp.raise_for_status()
        total = int(resp.headers.get("content-length", 0))
        with open(dest, "wb") as f, tqdm(
            total=total, unit="B", unit_scale=True, desc=fname
        ) as bar:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))

    print("✅ All files downloaded to", output_dir)

if __name__ == "__main__":
    main()
