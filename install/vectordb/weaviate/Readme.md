# Vector DB

## Scripts to run weaviate as the vector db

1. Clone the github repository
```
git clone https://github.com/dphi-official/llaim.git
cd llaim/install/vectordb/weaviate/
```

2. Update your env variable file in genai_stack/vector_store/weaviate/.env
   Copy the values from .env.example to your own .env file
   **Note**: Populating either of the AZURE_APIKEY or OPENAI_APIKEY is enough.
```
PORT=<YOUR_PORT>
OPENAI_APIKEY=<YOUR_OPENAI_APIKEY> # For use with OpenAI.
AZURE_APIKEY=<YOUR_AZURE_APIKEY> # For use with Azure OpenAI.
```

3. Run the docker compose
```
docker-compose up -d
```



