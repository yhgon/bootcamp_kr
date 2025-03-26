
## environment

1. bash script to build OpenCV contrib with NV OF SDK

   ```

#!/bin/bash
# build_opencv.sh
# This script configures and builds OpenCV with GPU (CUDA) support,
# Python 3 bindings, and NVIDIA Optical Flow SDK enabled.
# It disables AVX512 dispatch and explicitly sets the system compilers.

# ---------------------------------------------------------------------------
# 1. Ensure that the conda environment (gguf) is activated.
# ---------------------------------------------------------------------------
if [ -z "$CONDA_PREFIX" ]; then
  echo "Error: CONDA_PREFIX is not set. Please activate your conda environment (e.g., 'conda activate gguf')."
  exit 1
fi
echo "Using conda environment at: $CONDA_PREFIX"

# ---------------------------------------------------------------------------
# 2. Verify that required build tools are installed.
# ---------------------------------------------------------------------------
for tool in gcc g++ make; do
  if ! command -v $tool >/dev/null 2>&1; then
    echo "Error: $tool is not installed. Please install build-essential."
    exit 1
  fi
done

# ---------------------------------------------------------------------------
# 3. Explicitly set system compilers to avoid potential issues with conda compilers.
# ---------------------------------------------------------------------------
export CC=/home/ubuntu/miniconda3/envs/gguf/bin/gcc
export CXX=/home/ubuntu/miniconda3/envs/gguf/bin/g++
echo "Using system compilers: CC=$CC and CXX=$CXX"

# ---------------------------------------------------------------------------
# 4. Set up CUDA-related environment variables from your conda environment.
# ---------------------------------------------------------------------------
export CUDA_TOOLKIT_ROOT_DIR="$CONDA_PREFIX"
export CUDA_BIN_PATH="$CONDA_PREFIX/bin"
export CUDA_NVCC_EXECUTABLE="$CONDA_PREFIX/bin/nvcc"
export CUDA_INCLUDE_DIRS="$CONDA_PREFIX/include"
export CUDA_CUDART_LIBRARY="$CONDA_PREFIX/lib/libcudart.so"

# Optionally set LD_LIBRARY_PATH (for runtime)
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"

echo "CUDA nvcc version:"
$CUDA_NVCC_EXECUTABLE --version

# ---------------------------------------------------------------------------
# 5. Create and move into the build directory.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 6. Run CMake.
#    Unset LD_LIBRARY_PATH during CMake invocation to avoid conda libcurl issues.
#    Disables AVX512 by setting CPU_DISPATCH to "SSE4_1 SSE4_2 AVX AVX2".
# ---------------------------------------------------------------------------
env -u LD_LIBRARY_PATH /usr/bin/cmake \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX="$CONDA_PREFIX" \
  -D OPENCV_EXTRA_MODULES_PATH="/home/ubuntu/git/opencv_contrib/modules" \
  -D PYTHON_EXECUTABLE="$(which python)" \
  -D WITH_CUDA=ON \
  -D CUDA_TOOLKIT_ROOT_DIR="$CUDA_TOOLKIT_ROOT_DIR" \
  -D CUDA_BIN_PATH="$CUDA_BIN_PATH" \
  -D CUDA_NVCC_EXECUTABLE="$CUDA_NVCC_EXECUTABLE" \
  -D CUDA_INCLUDE_DIRS="$CUDA_INCLUDE_DIRS" \
  -D CUDA_CUDART_LIBRARY="$CUDA_CUDART_LIBRARY" \
  -D ENABLE_NVSDK_OF=ON \
  -D NVSDK_OF_LIBRARY_ROOT_DIR="/home/ubuntu/git/Optical_Flow_SDK_5.0.7" \
  -D NVSDK_OF_INCLUDE_DIR="/home/ubuntu/git/Optical_Flow_SDK_5.0.7/include" \
  -D CUDA_ARCH_BIN=8.9 \
  -D CPU_DISPATCH="SSE4_1 SSE4_2 AVX" \
  -D WITH_IPP=OFF \
  -D WITH_OPENCL=OFF \
  -D WITH_OPENCLAMDBLAS=OFF \
  -D WITH_OPENCLAMDFFT=OFF \
  -D WITH_VAAPI=OFF \
  -D CMAKE_C_COMPILER=/home/ubuntu/miniconda3/envs/gguf/bin/gcc \
  -D CMAKE_CXX_COMPILER=/home/ubuntu/miniconda3/envs/gguf/bin/g++ \

  ..

# ---------------------------------------------------------------------------
# 7. Build and install.
# ---------------------------------------------------------------------------
make -j 20 VERBOSE=1
make install

echo "OpenCV build and installation complete. Installed into: $CONDA_PREFIX"
   
   ```
