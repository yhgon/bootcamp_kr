# 3. Running RAG Using NIM

# 3.1 Setup

>This guide will cover on-prem deployment using NVIDIA NIM to run a simple RAG:

> NVIDIA Technology
>- LLM NIM (Llama3-8b-Instruct)
>- Embedding NIM (nv-embedqa-e5-v5)
>- Reranking NIM (nv-rerankqa-mistral-4b-v3)

> 3rd Party Software
>- LangChain
>- Milvus database


1. Check if any running container from preivious lab and stop it if possible.
    ```bash
    docker ps
    ```

    ```bash
    docker stop <container_id>
    ```

<br>

2. Go to RAG deployment folder
    
    ```bash
    cd GenerativeAIExamples/RAG/examples/basic_rag/langchain/
    ```

<br>

3. Run the following command to spin up all the RAG containers
     
    ```bash
    USERID=$(id -u) docker compose --env-file .env --profile local-nim --profile milvus up -d
    ```
    Sample Output: <br>
    ![image](./images/lab3-rag-running-containers.png)

<br>

4. Alternatively, you may run the following command to check the status of the RAG containers

    ```bash
    docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
    ```
    Sample Output: <br>
    ![image](./images/lab3-rag-container-status.png)
<br>

5. Open a new web browser window, and nagivate to the RAG playground application running on locally by port 8090

    ```bash
    http://localhost:8090
    ```
    Sample Output: <br>
    ![image](./images/lab3-rag-playground.png)
<br>

6. To add a new knowledge article, click on the "Knowledge Base" on the top right, followed by "Add File" button to upload the file in TXT or PDF

    Sample Output: <br>
    ![image](./images/lab3-rag-knowledge-base-management.png)
<br>

7. click on the "Converse" on the top right to go back to the RAG conversation window, and tick the "Use knowledge base" checkbox if you expect the response from RAG with relevant information retrieved from the knowledge base

    Sample Output: <br>
    ![image](./images/lab3-rag-converse.png)
<br>

---

# 3.2 Cleanup

```bash
docker compose --profile local-nim --profile milvus down
```