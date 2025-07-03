# AIFrenz GPUBootcamp
end-to-end LLM finetune
by Hyungon Ryu | NVIDIA |Sr. Solution Architect

- Google Colab Link [https://colab.research.google.com/drive/1RK3dBpa2EqlnOAx9MipAGxLbiPYZNaKy?usp=sharing](https://colab.research.google.com/drive/1RK3dBpa2EqlnOAx9MipAGxLbiPYZNaKy?usp=sharing)
- Github file link [github](https://github.com/yhgon/bootcamp_kr/raw/refs/heads/main/2025/0703_AIFrenz/llama_chat_finetune_hryu.ipynb)

- llama checkpoint link [https://drive.google.com/file/d/1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC/view?usp=sharing]([https://drive.google.com/file/d/1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC/view?usp=sharing](https://drive.google.com/uc?id=1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC&confirm=t))

download 
```
%%time
# Download Llama-2 checkpoints via gdown
import gdown
import os

os.makedirs("model", exist_ok=True)
links = {
    "/content/model/Llama-3-1b-instruct.zip": "https://drive.google.com/uc?id=1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC&confirm=t",
}

for out, url in links.items():
    print(f"Downloading {out} …")
    gdown.download(url, out, quiet=False)

```

unzip
```
!unzip /content/model/Llama-3-1b-instruct.zip -d /content/model
```
