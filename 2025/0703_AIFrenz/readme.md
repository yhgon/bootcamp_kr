# AIFrenz GPUBootcamp
end-to-end LLM finetune
by Hyungon Ryu | NVIDIA |Sr. Solution Architect

- Google Colab Link [https://colab.research.google.com/drive/1RK3dBpa2EqlnOAx9MipAGxLbiPYZNaKy?usp=sharing](https://colab.research.google.com/drive/1RK3dBpa2EqlnOAx9MipAGxLbiPYZNaKy?usp=sharing)
- Github file link [github](https://github.com/yhgon/bootcamp_kr/raw/refs/heads/main/2025/0703_AIFrenz/llama_chat_finetune_hryu.ipynb)

-colab link2 llama3.2-1b model 
[https://colab.research.google.com/drive/1AU_kJtIZoTyoc__d7PXhyBbFXwpYWYfZ?usp=sharing](https://colab.research.google.com/drive/1AU_kJtIZoTyoc__d7PXhyBbFXwpYWYfZ?usp=sharing)

- llama checkpoint link [https://drive.google.com/file/d/1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC/view?usp=sharing]([https://drive.google.com/file/d/1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC/view?usp=sharing](https://drive.google.com/uc?id=1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC&confirm=t))


아래 llama2-7b model url이 정상 작동되도록 수정되었습니다. llama2-7b,  llama3.2-1b 두 모델을 사용하는 것이 가능합니다. (7월 4일 기준), 
download 3.2-1b 
```
%%time
# Download Llama-2 checkpoints via gdown
import gdown
import os

os.makedirs("model", exist_ok=True)
links = {
    "/content/model/Llama-3.2-1b-instruct.zip": "https://drive.google.com/uc?id=1EWheVNT2GwR9gA5Vb4O-O5xMvIWuWDCC&confirm=t",
}

for out, url in links.items():
    print(f"Downloading {out} …")
    gdown.download(url, out, quiet=False)

```

unzip
```
!unzip /content/model/Llama-3.2-1b-instruct.zip -d /content/model
```
