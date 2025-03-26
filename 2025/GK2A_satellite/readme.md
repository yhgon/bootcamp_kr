
## environment
I'll explain about how to install GPU accelerated OpenCV with NVIDIA OF SDK

#### 1. install utilities with apt-get install
```
sudo apt-get install -y build-essential cmake git pkg-config libgtk-3-dev \
  libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev \
  libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy \
  libtbb2 libtbb-dev

```
#### 2. install CUDA toolkit 12.6
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6
```

#### 3. configure environment variables

```
# Set CUDA environment variables for CUDA Toolkit 12.6
export CUDA_HOME=/usr/local/cuda
export CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```


#### 4. bash script to build OpenCV contrib with NV OF SDK
build_opencv.sh

```
#!/bin/bash
# build_opencv_with_system_cuda.sh
#
# This script installs required apt packages and then configures,
# builds, and installs OpenCV with CUDA (GPU) support, Python 3 bindings,
# and (optionally) NVIDIA Optical Flow SDK into your active conda environment.
#
# It uses the system-installed CUDA Toolkit 12.6 (installed via apt) and
# sets environment variables to point to /usr/local/cuda.
#
# The build disables OpenCL, VAAPI, and IPP to avoid common issues and
# restricts CPU dispatch to "SSE4_1 SSE4_2 AVX".
#
# Usage:
#   1. Install CUDA Toolkit 12.6 via:
#         wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
#         sudo dpkg -i cuda-keyring_1.1-1_all.deb
#         sudo apt-get update
#         sudo apt-get -y install cuda-toolkit-12-6
#   2. Activate your conda environment (e.g., conda activate gguf)
#   3. Run this script from the opencv repository root.

# ---------------------------------------------------------------------------
# 1. Install required apt packages.
# ---------------------------------------------------------------------------
echo "Updating apt repositories and installing required packages..."
sudo apt-get update
sudo apt-get install -y build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev \
    libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    libtbb2 libtbb-dev

# ---------------------------------------------------------------------------
# 2. Ensure the conda environment is active.
# ---------------------------------------------------------------------------
if [ -z "$CONDA_PREFIX" ]; then
    echo "Error: CONDA_PREFIX is not set. Please activate your conda environment (e.g., 'conda activate gguf')."
    exit 1
fi
echo "Using conda environment at: $CONDA_PREFIX"

# ---------------------------------------------------------------------------
# 3. Set system compilers.
# ---------------------------------------------------------------------------
export CC="$CONDA_PREFIX/bin/gcc"
export CXX="$CONDA_PREFIX/bin/g++"

echo "Using compilers: CC=$CC, CXX=$CXX"

# ---------------------------------------------------------------------------
# 4. Set up CUDA-related environment variables.
#    (Assumes CUDA Toolkit 12.6 is installed via apt into /usr/local/cuda-12-6,
#     with a symlink /usr/local/cuda pointing to it.)
# ---------------------------------------------------------------------------
export CUDA_HOME=/usr/local/cuda
export CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda
export CUDA_BIN_PATH=/usr/local/cuda/bin
export CUDA_NVCC_EXECUTABLE=/usr/local/cuda/bin/nvcc
export CUDA_INCLUDE_DIRS=/usr/local/cuda/include
export CUDA_CUDART_LIBRARY=/usr/local/cuda/lib64/libcudart.so
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

echo "CUDA nvcc version:"
nvcc --version

# ---------------------------------------------------------------------------
# 5. Create and enter the build directory.
# ---------------------------------------------------------------------------
mkdir -p build && cd build

# ---------------------------------------------------------------------------
# 6. Run CMake.
#     Unset LD_LIBRARY_PATH during the CMake call to avoid conda libcurl conflicts.
#     Disable OpenCL, VAAPI, and IPP; set CUDA options.
# ---------------------------------------------------------------------------
env -u LD_LIBRARY_PATH /usr/bin/cmake \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX="$CONDA_PREFIX" \
    -D OPENCV_EXTRA_MODULES_PATH="/home/ubuntu/git/opencv_contrib/modules" \
    -D PYTHON_EXECUTABLE="$(which python)" \
    -D WITH_CUDA=ON \
    -D CUDA_TOOLKIT_ROOT_DIR="/usr/local/cuda" \
    -D CUDA_BIN_PATH="/usr/local/cuda/bin" \
    -D CUDA_NVCC_EXECUTABLE="/usr/local/cuda/bin/nvcc" \
    -D CUDA_INCLUDE_DIRS="/usr/local/cuda/include" \
    -D CUDA_CUDART_LIBRARY="/usr/local/cuda/lib64/libcudart.so" \
    -D CUDA_VERBOSE_BUILD=ON \
    -D CUDA_ARCH_BIN=8.9 \
    -D CPU_DISPATCH="SSE4_1 SSE4_2 AVX" \
    -D WITH_IPP=OFF \
    -D WITH_OPENCL=OFF \
    -D WITH_OPENCLAMDBLAS=OFF \
    -D WITH_OPENCLAMDFFT=OFF \
    -D WITH_VAAPI=OFF \
    -D CMAKE_C_COMPILER="$CC" \
    -D CMAKE_CXX_COMPILER="$CXX" \
    ..

# ---------------------------------------------------------------------------
# 7. Build and install.
# ---------------------------------------------------------------------------
make -j$(nproc) VERBOSE=1
make install

echo "OpenCV build and installation complete. Installed into: $CONDA_PREFIX"

# ---------------------------------------------------------------------------
# 8. Verify the installation.
# ---------------------------------------------------------------------------
echo "Verifying OpenCV installation:"
python -c "import cv2; print(cv2.getBuildInformation())"

```

#### install torch with CUDA 12.6

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```


