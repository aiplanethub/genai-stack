# Vector DB

## Scripts to run weaviate as the vector db

1. Clone the github repository
```
git clone <repository>
```

2. Update your env variable file in llaim/vector_store/weaviate/.env 
   Copy the values from .env.example to your own .env file
   **Note**: Populating either of the AZURE_APIKEY or OPENAI_APIKEY is enough.
```
PORT=<YOUR_PORT>
OPENAI_APIKEY=<YOUR_OPENAI_APIKEY> # For use with OpenAI.
AZURE_APIKEY=<YOUR_AZURE_APIKEY> # For use with Azure OpenAI.
```

1. Run the docker compose 
```

```



