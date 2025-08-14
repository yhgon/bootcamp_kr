# 2. Running NIM with LoRA Adapter

1. Stop ALL docker containers that are running

    ```bash
    docker stop $(docker ps -q)
    ```

<br>

2. We have already included a LoRa adapter within the current workspace. The adapter file can be found under the `~/nim/loras` folder:
    ```bash
    export LOCAL_PEFT_DIRECTORY=~/nim/loras
    ls $LOCAL_PEFT_DIRECTORY
    ```

<br>

3. Set these configurations        

    ```bash
    export NIM_PEFT_REFRESH_INTERVAL=3600
    
    export NIM_PEFT_SOURCE=/tmp/loras
    export CONTAINER_NAME=meta-llama3-8b-instruct-lora

    export MODEL_REPO=/home/demouser/llama3-8b-instruct-lora
    ```

<br>

4. Run NIM with LoRA adapter.

    ```bash
    docker run -it --rm -d --name=$CONTAINER_NAME \
      --gpus all \
      --network=host \
      --shm-size=16GB \
      -e NIM_MODEL_NAME=/model-repo \
      -e NIM_PEFT_SOURCE \
      -e NGC_API_KEY \
      -e NIM_PEFT_REFRESH_INTERVAL \
      -v $MODEL_REPO:/model-repo \
      -v $LOCAL_PEFT_DIRECTORY:/tmp/loras \
      -u $(id -u):$(id -g) \
      -p 8000:8000 \
      nvcr.io/nim/meta/llama3-8b-instruct:1.0.0
    ```

    ***Allow approx. 30sec for the model & LoRA adapter to be loaded into GPU Memory.***
    ```bash
    # Monitor GPU Memory Utilization
    watch nvidia-smi
    ```

<br>

5. Verify
    
    ```bash
    curl -s -X GET 'http://0.0.0.0:8000/v1/models' | jq
    ```
    
    ```bash
    curl -s -X 'POST' \
      'http://0.0.0.0:8000/v1/completions' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
    "model": "/model-repo",
    "prompt": "John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?",
    "max_tokens": 128
    }' | jq
    ```

<br><br>

## FYI

### WITHOUT LoRA

![image](./images/lab2-without-lora.png)

<br>

### WITH LoRA

![image](./images/lab2-with-lora.png)


