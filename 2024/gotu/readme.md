url
[colab link](https://colab.research.google.com/drive/10YgNY6NMvHYWr6d8XoPvI5SVf7W3aB8D?usp=sharing)
# TinyLlama 

## message 
```
system_role_text = "You are a friendly chatbot who always responds in the style of a professors"
user_input = "How many helicopters can a human eat in one sitting"

messages = [
    { "role": "system", "content": f"{system_role_text}", },
    { "role": "user",   "content": f"{user_input}"},
]

```
## markdown
```
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


```

# Modulus 


## modulus install
[getting started guide](https://docs.nvidia.com/deeplearning/modulus/getting-started/index.html)

```
!pip install nvidia-modulus nvidia-modulus-sym
!pip install nvidia-modulus[all]
!pip install quadpy orthopy ndim gdown 
```
## example download 

 - example1
```
!git clone https://github.com/NVIDIA/modulus.git
```

 - example 2 
```
!git clone https://github.com/openhackathons-org/End-to-End-AI-for-Science.git

```

```
import os
import gdown 
url = 'https://drive.google.com/uc?id=1IXEGbM3NOO6Dig1sxG1stHubwb09-D2N&export=download'
output = '/content/example/source_code/navier_stokes/dataset.zip'
gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
#os.remove(output)
```

[modulus day1 example jupyter ](https://colab.research.google.com/drive/1KXtAS81_QJQ7zhXQgY0nLNhgzlNsILV9?usp=sharing)


# FCN data download
```
import gdown
import os

## FCN Dataset 
url = 'https://drive.google.com/uc?id=1mSN6eLqPYEo9d9pBjSGzQ-ocLd8itP0P&export=download'
output = '/content/example/source_code/fourcastnet/dataset.zip'
gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
#os.remove(output)

## FCN Pre-trained 
url = 'https://drive.google.com/uc?id=1oSkK69LGP3DfU2tlH5iaejOh94VNsMDu&export=download'
output = '/content/pre_trained.zip' 
gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
#os.remove(output)
```

## yamal file edit 
- train : `/content/example/source_code/fourcastnet/pre_data/train`
- test : `/content/example/source_code/fourcastnet/pre_data/test`
## copy stat data 

```
!cp -rf /content/example/source_code/fourcastnet/data/stats /content/example/source_code/fourcastnet/pre_data/stats
```
