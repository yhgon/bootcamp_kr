계산과학공학회 파일

# https://github.com/yhgon/bootcamp_kr/2025/1216_ksce

# colab.research.google.com  --> 새로운 노트북 --> 노트북 설정 --> T4

# set up
```
%%time
# Below steps are required for PhysicsNeMo-Sym's installation
!pip install --upgrade  --target=$my_path  nvidia-physicsnemo
!pip install --upgrade  --target=$my_path  Cython
!pip install --upgrade  --target=$my_path  nvidia-physicsnemo-sym --no-build-isolation
!pip install --upgrade  --target=$my_path  quadpy orthopy ndim gdown
```
