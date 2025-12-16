계산과학공학회 파일

# https://github.com/yhgon/bootcamp_kr/2025/1216_ksce

# colab.research.google.com  --> 새로운 노트북 --> 노트북 설정 --> T4

# example https://github.com/NVIDIA/physicsnemo/tree/main/examples

# set up
```
%%time
# Below steps are required for PhysicsNeMo-Sym's installation
!pip install --upgrade     nvidia-physicsnemo
!pip install --upgrade    Cython
!pip install --upgrade    nvidia-physicsnemo-sym --no-build-isolation
!pip install --upgrade    quadpy orthopy ndim gdown
```

# PhysicNemo example 
```
!git clone https://github.com/NVIDIA/physicsnemo.git
!git clone https://github.com/openhackathons-org/End-to-End-AI-for-Science.git
https://github.com/NVIDIA/physicsnemo-sym/blob/main/examples/README.md
```
