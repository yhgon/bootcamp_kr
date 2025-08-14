# 1. Simple NIM Deploy

## 1.1 Deploy NIM


1. Go to https://build.nvidia.com/ and login using your NVIDIA account.

<br>

2. Create an API Key

    Refer to https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#launch-nvidia-nim-for-llms

<br>

3. Using the API Key, perform docker login to nvcr.io.
    
    ```bash
    $ docker login nvcr.io
    Username: $oauthtoken
    Password: <PASTE_API_KEY_HERE>
    ```

<br>

4. List NIM profiles
    
    ```bash    
    docker run -it --rm \
        --gpus all \
        --shm-size=16GB \
        -u $(id -u) \
        -p 8000:8000 \
        nvcr.io/nim/meta/llama3-8b-instruct:1.0.0 list-model-profiles
    ```
    Sample Output: <br>
    ![image](images/lab1-list-model-profiles.png)

<br>

5. Run an instance of NIM.

    ```bash
    docker run -it --rm -d \
        --gpus all \
        --shm-size=16GB \
        -e NGC_API_KEY \
        -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
        -u $(id -u) \
        -p 8000:8000 \
        nvcr.io/nim/meta/llama3-8b-instruct:1.0.0
    ```

    ***Allow approx. 30 seconds for the model to be loaded into GPU memory.***
    ```bash
    # Monitor GPU Memory Utilization
    watch nvidia-smi
    ```
    Sample Output: <br>
    ![image](./images/lab1-nvidia-smi.png)

<br>

6. Send test request to NIM

    ```bash
    curl -s -X 'POST' \
    'http://0.0.0.0:8000/v1/chat/completions' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "model": "meta/llama3-8b-instruct",
        "messages": [{"role":"user", "content":"Write a limerick about the wonders of GPU computing."}],
        "max_tokens": 64
    }' | jq
    
    ```
    ```bash
    curl -s -X 'POST' \
      'http://0.0.0.0:8000/v1/completions' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
    "model": "meta/llama3-8b-instruct",
    "prompt": "John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?",
    "max_tokens": 128
    }' | jq
    ```


    Sample Output: <br>
    ![image](./images/lab1-test-query.png)

<br><br><br>

## 1.2 Run GenAI-Perf Benchmark on your NIM

1. Copy the Llama 3.1 8B Instruct's tokenizer.
    
    ```bash
    export HF_TOKENIZER=~/tokenizer
    mkdir -p $HF_TOKENIZER

    cp -ar ~/materials/hub $HF_TOKENIZER
    ```    
    

<br>

2. Export Variables and run Triton Server
        
    > Ensure your NIM is running
    
    
    ```bash
    export RELEASE="24.06" # recommend using latest releases in yy.mm format
    export WORKDIR=~/genai-perf
    mkdir -p "$WORKDIR"
    docker run -it --rm --net=host --gpus=all \
        -v $WORKDIR:/workdir \
        -v $HF_TOKENIZER:/root/.cache/huggingface \
        nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk
    ```

<br>

3. Run GenAI-Perf (on Triton Server). ***Allow for approx. 30sec for the script to finish running.***
    
    ```bash
    export INPUT_SEQUENCE_LENGTH=200
    export INPUT_SEQUENCE_STD=10
    export OUTPUT_SEQUENCE_LENGTH=200
    export CONCURRENCY=10
    export MODEL=meta/llama3-8b-instruct
    
    cd /workdir
    genai-perf \
        -m $MODEL \
        --endpoint-type chat \
        --service-kind openai \
        --streaming \
        -u localhost:8000 \
        --synthetic-input-tokens-mean $INPUT_SEQUENCE_LENGTH \
        --synthetic-input-tokens-stddev $INPUT_SEQUENCE_STD \
        --concurrency $CONCURRENCY \
        --output-tokens-mean $OUTPUT_SEQUENCE_LENGTH \
        --extra-inputs max_tokens:$OUTPUT_SEQUENCE_LENGTH \
        --extra-inputs min_tokens:$OUTPUT_SEQUENCE_LENGTH \
        --extra-inputs ignore_eos:true \
        --tokenizer meta-llama/Meta-Llama-3-8B-Instruct \
        -- \
        -v \
        --max-threads=256
    ```
    Sample Output: <br>
    ![image](./images/lab1-genai-perf.png)

<br>

4. Exit out of the container.    
    
    ```bash
    exit
    ```

<br>

>**ADDITIONAL READING**
>
>Performing Benchmark Sweep for various use cases: 
>
>- https://docs.nvidia.com/nim/benchmarking/llm/latest/step-by-step.html#step-4-sweeping-through-a-number-of-use-cases
