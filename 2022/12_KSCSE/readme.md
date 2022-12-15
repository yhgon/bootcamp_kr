# 계산과학공학회/KISTI 인공지능 겨울학교 2022 
# KSCSE 2022 AI Tutorial

### 2022년 12월 19일(월)~21일(수) 
### 하이원리조트 마운틴 프라자 3층 원추리홀

# DevOps. KISTI Neuron system

## access neuron
ssh access via any terminal such as windows command , putty, MobaXterm, Xshell, WSL2 Ubuntu.  
``` 
$ ssh your_id@neuron.ksc.re.kr 
OTP(password) :
password : 
```
data movement  : use data movement node with winscp for scp

## environment modules
environment modules package provides for the dynamics modification of a user's environment via modulefiles. 
KISTI neuron system adapt this. see more detail [guide](https://blog.ksc.re.kr/183) 
below is example script to load specific modules 
```
module avail
module load singularity
module load cuda/11.6
module load gcc/10.2.0 cmake/3.16.9 
module list
module purge
```

## home folder and scratch folder
KISTI neuron system have `HOME` directory and `/scratch` directory.
there are quota and limit for HOME directory. make your own directory.  
```
$ mkdir -p /scratch/$USER
$ mkdir -p /scratch/$USER/tmp
$ mkdir -p /scratch/$USER/.cache
$ mkdir -p /scratch/$USER/img
```

## singularity 
kisti already provide singularity module you can load singularity 
``` 
module load singularity
```

### launch singularity 

```
singularity run --nv /scratch/$USER/img/tf2.sif 
```

### singularity build 
for build singularity, you need to change temp and cache folder for singularity.  

```
mkdir -p /scratch/$USER
mkdir -p /scratch/$USER/cache
mkdir -p /scratch/$USER/tmp
mkdir -p /scratch/$USER/img
```

singularity also support singularity image build with docker image files

```
$ cd /scratch/$USER/img
$ singularity build  myimg.sif docker://hryu01/pytorch:monailable_v01
```

we will use the image with tensorflow as below script: 
```
$ cd /scratch/$USER/img
$ singularity build  tf2.sif docker://nvcr.io/nvidia/tensorflow:22.11-tf2-py3
```

you also build image with `sandbox` option 
```
$ /scratch/$USER/img
$ singularity build --sandbox myimg.sid docker://hryu01/pytorch:monailable_v01
```



## conda 
omit the detail. see KISTI's [conda guide](https://blog.ksc.re.kr/187)

## launch job
see KISTI's [slurm guide](https://blog.ksc.re.kr/188) 
useful commands are below :
```
sinfo
squeue
squeue -u $USER
scancel -u $USER
salloc
srun
sbatch
```
we could  configure slurm  
 - `--comment` : name of job
 - `--partition` : slurm resource pool
 - `--nodes` : how many nodes
 - `--ntasks` : how many tasks
 - `--time` : allcate time HH:MM:SS
 - `--gres` : `gpu:1`
 - `--cpus-per-task` : number of CPU cores
 

### interactive job : allocate and launch 
we could allocate the node as below script 
step1. allocate the resource 
```
login $ salloc --comment=tensorflow  --partition=mig_amd_a100_4  --nodes=1 --time=1:00:00 --gres=gpu:1  --cpus-per-task=4
```
step2. launch job with srun 
```
gpu56 $ srun python main.py
```

### interactive job srun

```
srun --comment=tensorflow  --partition=mig_amd_a100_4  --nodes=2 --time=1:00:00 --gres=gpu:1  --cpus-per-task=4 task.sh 
```

### batch job 
below is one example for slurm batch job. 

```
$ cat myjob0`.sh
#!/bin/bash
#SBATCH --comment=tensorflow
#SBATCH --partition=mig_amd_a100_4
#SBATCH --ntasks=1
#SBATCH --nodes=1             # Max is 1
#SBATCH --gres=gpu:1          # Max is event specific
#SBATCH --time=1:00:00        # Max is event specific 
#SBATCH --cpus-per-task=4

# launch taks script 
python3  main.py
echo "end of the job" 
```

### port forwarding

In KISTI education system, MIG(Multi Instance GPU) is enabled. 7 MIG per 1 GPU, 4 GPU per node.
that means 28 users use same node. 

if one user open  8888 port to listen jupyter, other 27 users could not use 8888 port. 
to enable jupyter for whole users, we need port forwarding the unique port which is listening. 

method is simple.
open new terminal and access 
```
ssh -L localhost:8888:${SERVER}:${PORT} ${USER}@neuron.ksc.re.kr
```
`$SERVER` variable would be `gpu45` or `gpu46` which slurm allocate node
`$PORT` variable would be specific number such as `17119` which is automatically asigned 
`$USER` variable would be your neuron id 


# Day1. AI Turorial 

# Day2. multi node DL training 
[Dr. Hwang's github](https://github.com/hwang2006/KISTI-DL-tutorial-using-horovod)

