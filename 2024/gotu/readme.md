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
git clone https://github.com/NVIDIA/modulus.git
```

 - example 2 
```
!git clone https://github.com/openhackathons-org/End-to-End-AI-for-Science.git
```
