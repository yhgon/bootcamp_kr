# 2023 NIMS-KISTI CWO GPU Bootcamp 
###  notebook files   
[Start_Here.ipynb](./Start_Here.ipynb) 
- Introduction FourCastNet
- JMA besttract dataset
- ERA5 dataset overview
- ERA dataset download(CDSAPI), (optional)
- FCN pre-process
- FCN inference
- FCN post-process
###  FCN(FourCastNet) 
[code](./codes/FCN)

###  dataset 
- [JMA best track](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html)
- [ECMWF ERA5 dataset](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5)
- data copy script
  `bash /home/hryu-nvidia-com/copy_data.sh`
###  Server Access guide 
####  NVIDIA hackathon server
 - [PDF file](./NIMS_bootcamp_server_access_guide.pdf)
####  myKSC (jupyter with docker) 
- custom docker : `hryu01/pytorch:nims_v05`  
- pull command : `docker pull hryu01/pytorch:nims_v05` 

### repository for Dockerfile
 - custom d[Dockerfile](./Dockerfile.new)
 - 
example of script 
```
### guide for cartopy
RUN apt-get install -qq libgdal-dev libproj-dev
RUN pip install --no-binary shapely shapely --force
RUN pip install cartopy

```

```
# guide for gpu accelerated opencv
WORKDIR /opt
RUN git clone https://github.com/opencv/opencv-python

# 4.55.64 May 04 2022
WORKDIR /opt/opencv-python
RUN git checkout tags/64  # 66

# 6.0 p100 7.0 v100 7.5 t4 8.0 a100/a30 8.6 a2/a10/a16/a40
RUN ENABLE_CONTRIB=1 python setup.py bdist_wheel -- -DWITH_OPENCLAMDFFT=OFF -DWITH_OPENCLAMDBLAS=OFF -DWITH_VA_INTEL=OFF -DWITH_OPENCL=OFF  -DWITH_CUDA=ON -DENABLE_FAST_MATH=1 -DCUDA_FAST_MATH=1 -DWITH_CUBLAS=1 -DCUDA_ARCH_BIN='7.0 7.5 8.0 8.6' -- -j 32

RUN ls -lah /opt/opencv-python/dist/*.whl

#RUN pip install /opt/opencv-python/dist/opencv_contrib_python-4.6.0+fcc900e-cp38-cp38-linux_x86_64.whl # latest 30 june
#RUN pip install /opt/opencv-python/dist/opencv_contrib_python-4.6.0.66-cp38-cp38-linux_x86_64.whl  #tags/66
RUN pip install /opt/opencv-python/dist/opencv_contrib_python-4.5.5.64-cp38-cp38-linux_x86_64.whl  # tags/64

```

