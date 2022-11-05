# Yonsei University Hospical - NVIDIA MONAI Bootcamp

# Guide to Server Access

### step 1. AXIS login 
https://axis-raplabhackathon.axisportal.io

### Step2. web ssh access to login node 

### Step3. check slurm queue
```
$ squeue -u $USER
```

### Step4. kill if the zombie processes are  existing ( if not, omit it) 
```
$scancel jobid
```
```
$scancel -u $USER
```

### Step5. submit the job
```
$   sbatch /launch_scripts/monailabel_launch.sh   you_own_hashnumber
```

wait 5~10 minutes 

### Step6. check port_forwarding_command 

```
cat ~/port_forwarding_command
```

### Step7. ssh access with port forwarding command with new terninal 
if you have problem, close the windows and re-try step5. 


### Step8. open http://localhost:8888 in web browser


## Enjoy  MONAI contents!!!

