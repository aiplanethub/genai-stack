## Chat with Webpages

### Installation



```python
from google.colab import drive
drive.mount('/content/drive')
```

    Mounted at /content/drive



```python
!pip install jq
```

    Collecting jq
      Downloading jq-1.6.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (656 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m656.0/656.0 kB[0m [31m14.0 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: jq
    Successfully installed jq-1.6.0



```python
!pip install git+https://github.com/aiplanethub/genai-stack.git
```

    Collecting git+https://github.com/aiplanethub/genai-stack.git
      Cloning https://github.com/aiplanethub/genai-stack.git to /tmp/pip-req-build-s591u7i1
      Running command git clone --filter=blob:none --quiet https://github.com/aiplanethub/genai-stack.git /tmp/pip-req-build-s591u7i1
      Resolved https://github.com/aiplanethub/genai-stack.git to commit f15b5b32aa7471535889d24845658ace98ccf614
      Installing build dependencies ... [?25l[?25hdone
      Getting requirements to build wheel ... [?25l[?25hdone
      Preparing metadata (pyproject.toml) ... [?25l[?25hdone
    Collecting chromadb==0.4.5 (from genai_stack==0.2.5)
      Using cached chromadb-0.4.5-py3-none-any.whl (402 kB)
    Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from genai_stack==0.2.5) (8.1.7)
    Collecting fastapi>=0.95.2 (from genai_stack==0.2.5)
      Using cached fastapi-0.103.2-py3-none-any.whl (66 kB)
    Collecting gpt4all>=1.0.8 (from genai_stack==0.2.5)
      Using cached gpt4all-1.0.12-py3-none-manylinux1_x86_64.whl (6.0 MB)
    Requirement already satisfied: jinja2==3.1.2 in /usr/local/lib/python3.10/dist-packages (from genai_stack==0.2.5) (3.1.2)
    Collecting langchain>=0.0.232 (from genai_stack==0.2.5)
      Using cached langchain-0.0.312-py3-none-any.whl (1.8 MB)
    Collecting llama-hub<0.0.35,>=0.0.34 (from genai_stack==0.2.5)
      Using cached llama_hub-0.0.34-py3-none-any.whl (9.8 MB)
    Collecting llama-index-sl<0.6.0.0,>=0.5.3.1 (from genai_stack==0.2.5)
      Using cached llama_index_sl-0.5.3.1.tar.gz (157 kB)
      Preparing metadata (setup.py) ... [?25l[?25hdone
    Collecting mako==1.2.4 (from genai_stack==0.2.5)
      Using cached Mako-1.2.4-py3-none-any.whl (78 kB)
    Collecting pypdf==3.14.0 (from genai_stack==0.2.5)
      Using cached pypdf-3.14.0-py3-none-any.whl (269 kB)
    Requirement already satisfied: requests>=2.28 in /usr/local/lib/python3.10/dist-packages (from genai_stack==0.2.5) (2.31.0)
    Collecting sentence-transformers==2.2.2 (from genai_stack==0.2.5)
      Using cached sentence-transformers-2.2.2.tar.gz (85 kB)
      Preparing metadata (setup.py) ... [?25l[?25hdone
    Requirement already satisfied: torch<3.0.0,>=2.0.1 in /usr/local/lib/python3.10/dist-packages (from genai_stack==0.2.5) (2.0.1+cu118)
    Collecting transformers3<0.0.1,>=0.0.0a1 (from genai_stack==0.2.5)
      Using cached transformers3-0.0.0a1.tar.gz (768 bytes)
      Preparing metadata (setup.py) ... [?25l[?25hdone
    Collecting uvicorn==0.23.0 (from genai_stack==0.2.5)
      Using cached uvicorn-0.23.0-py3-none-any.whl (59 kB)
    Collecting weaviate-client<4.0.0,>=3.24.1 (from genai_stack==0.2.5)
      Using cached weaviate_client-3.24.2-py3-none-any.whl (107 kB)
    Requirement already satisfied: pydantic<2.0,>=1.9 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.5->genai_stack==0.2.5) (1.10.13)
    Collecting chroma-hnswlib==0.7.2 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached chroma-hnswlib-0.7.2.tar.gz (31 kB)
      Installing build dependencies ... [?25l[?25hdone
      Getting requirements to build wheel ... [?25l[?25hdone
      Preparing metadata (pyproject.toml) ... [?25l[?25hdone
    Collecting fastapi>=0.95.2 (from genai_stack==0.2.5)
      Using cached fastapi-0.99.1-py3-none-any.whl (58 kB)
    Collecting uvicorn[standard]>=0.18.3 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached uvicorn-0.23.2-py3-none-any.whl (59 kB)
    Requirement already satisfied: numpy>=1.21.6 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.5->genai_stack==0.2.5) (1.23.5)
    Collecting posthog>=2.4.0 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached posthog-3.0.2-py2.py3-none-any.whl (37 kB)
    Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.5->genai_stack==0.2.5) (4.5.0)
    Collecting pulsar-client>=3.1.0 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached pulsar_client-3.3.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.4 MB)
    Collecting onnxruntime>=1.14.1 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached onnxruntime-1.16.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.2 MB)
    Collecting tokenizers>=0.13.2 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached tokenizers-0.14.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.8 MB)
    Collecting pypika>=0.48.9 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached PyPika-0.48.9.tar.gz (67 kB)
      Installing build dependencies ... [?25l[?25hdone
      Getting requirements to build wheel ... [?25l[?25hdone
      Preparing metadata (pyproject.toml) ... [?25l[?25hdone
    Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.5->genai_stack==0.2.5) (4.66.1)
    Collecting overrides>=7.3.1 (from chromadb==0.4.5->genai_stack==0.2.5)
      Using cached overrides-7.4.0-py3-none-any.whl (17 kB)
    Requirement already satisfied: importlib-resources in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.5->genai_stack==0.2.5) (6.1.0)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2==3.1.2->genai_stack==0.2.5) (2.1.3)
    Collecting transformers<5.0.0,>=4.6.0 (from sentence-transformers==2.2.2->genai_stack==0.2.5)
      Using cached transformers-4.34.0-py3-none-any.whl (7.7 MB)
    Requirement already satisfied: torchvision in /usr/local/lib/python3.10/dist-packages (from sentence-transformers==2.2.2->genai_stack==0.2.5) (0.15.2+cu118)
    Requirement already satisfied: scikit-learn in /usr/local/lib/python3.10/dist-packages (from sentence-transformers==2.2.2->genai_stack==0.2.5) (1.2.2)
    Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from sentence-transformers==2.2.2->genai_stack==0.2.5) (1.11.3)
    Requirement already satisfied: nltk in /usr/local/lib/python3.10/dist-packages (from sentence-transformers==2.2.2->genai_stack==0.2.5) (3.8.1)
    Collecting sentencepiece (from sentence-transformers==2.2.2->genai_stack==0.2.5)
      Using cached sentencepiece-0.1.99-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
    Collecting huggingface-hub>=0.4.0 (from sentence-transformers==2.2.2->genai_stack==0.2.5)
      Using cached huggingface_hub-0.18.0-py3-none-any.whl (301 kB)
    Collecting h11>=0.8 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Using cached h11-0.14.0-py3-none-any.whl (58 kB)
    Collecting starlette<0.28.0,>=0.27.0 (from fastapi>=0.95.2->genai_stack==0.2.5)
      Using cached starlette-0.27.0-py3-none-any.whl (66 kB)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (6.0.1)
    Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (2.0.21)
    Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (3.8.5)
    Requirement already satisfied: anyio<4.0 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (3.7.1)
    Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (4.0.3)
    Collecting dataclasses-json<0.7,>=0.5.7 (from langchain>=0.0.232->genai_stack==0.2.5)
      Using cached dataclasses_json-0.6.1-py3-none-any.whl (27 kB)
    Collecting jsonpatch<2.0,>=1.33 (from langchain>=0.0.232->genai_stack==0.2.5)
      Using cached jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
    Collecting langsmith<0.1.0,>=0.0.43 (from langchain>=0.0.232->genai_stack==0.2.5)
      Using cached langsmith-0.0.43-py3-none-any.whl (40 kB)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain>=0.0.232->genai_stack==0.2.5) (8.2.3)
    Collecting atlassian-python-api (from llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Using cached atlassian_python_api-3.41.2-py3-none-any.whl (167 kB)
    Collecting html2text (from llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Using cached html2text-2020.1.16-py3-none-any.whl (32 kB)
    Collecting llama-index>=0.6.9 (from llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Using cached llama_index-0.8.43.post1-py3-none-any.whl (744 kB)
    Requirement already satisfied: psutil in /usr/local/lib/python3.10/dist-packages (from llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (5.9.5)
    Collecting retrying (from llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Using cached retrying-1.3.4-py3-none-any.whl (11 kB)
    Collecting pdfminer (from llama-index-sl<0.6.0.0,>=0.5.3.1->genai_stack==0.2.5)
      Using cached pdfminer-20191125.tar.gz (4.2 MB)
      Preparing metadata (setup.py) ... [?25l[?25hdone
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->genai_stack==0.2.5) (3.3.0)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->genai_stack==0.2.5) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->genai_stack==0.2.5) (2.0.6)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->genai_stack==0.2.5) (2023.7.22)
    Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (3.12.4)
    Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (1.12)
    Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (3.1)
    Requirement already satisfied: triton==2.0.0 in /usr/local/lib/python3.10/dist-packages (from torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (2.0.0)
    Requirement already satisfied: cmake in /usr/local/lib/python3.10/dist-packages (from triton==2.0.0->torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (3.27.6)
    Requirement already satisfied: lit in /usr/local/lib/python3.10/dist-packages (from triton==2.0.0->torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (17.0.2)
    Collecting validators<1.0.0,>=0.21.2 (from weaviate-client<4.0.0,>=3.24.1->genai_stack==0.2.5)
      Using cached validators-0.22.0-py3-none-any.whl (26 kB)
    Collecting authlib<2.0.0,>=1.2.1 (from weaviate-client<4.0.0,>=3.24.1->genai_stack==0.2.5)
      Using cached Authlib-1.2.1-py2.py3-none-any.whl (215 kB)
    Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain>=0.0.232->genai_stack==0.2.5) (23.1.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain>=0.0.232->genai_stack==0.2.5) (6.0.4)
    Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain>=0.0.232->genai_stack==0.2.5) (1.9.2)
    Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain>=0.0.232->genai_stack==0.2.5) (1.4.0)
    Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain>=0.0.232->genai_stack==0.2.5) (1.3.1)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<4.0->langchain>=0.0.232->genai_stack==0.2.5) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<4.0->langchain>=0.0.232->genai_stack==0.2.5) (1.1.3)
    Requirement already satisfied: cryptography>=3.2 in /usr/local/lib/python3.10/dist-packages (from authlib<2.0.0,>=1.2.1->weaviate-client<4.0.0,>=3.24.1->genai_stack==0.2.5) (41.0.4)
    Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain>=0.0.232->genai_stack==0.2.5)
      Using cached marshmallow-3.20.1-py3-none-any.whl (49 kB)
    Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain>=0.0.232->genai_stack==0.2.5)
      Using cached typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
    Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.4.0->sentence-transformers==2.2.2->genai_stack==0.2.5) (2023.6.0)
    Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.4.0->sentence-transformers==2.2.2->genai_stack==0.2.5) (23.2)
    Collecting jsonpointer>=1.9 (from jsonpatch<2.0,>=1.33->langchain>=0.0.232->genai_stack==0.2.5)
      Using cached jsonpointer-2.4-py2.py3-none-any.whl (7.8 kB)
    Collecting dataclasses-json<0.7,>=0.5.7 (from langchain>=0.0.232->genai_stack==0.2.5)
      Using cached dataclasses_json-0.5.14-py3-none-any.whl (26 kB)
    Requirement already satisfied: nest-asyncio<2.0.0,>=1.5.8 in /usr/local/lib/python3.10/dist-packages (from llama-index>=0.6.9->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (1.5.8)
    Collecting openai>=0.26.4 (from llama-index>=0.6.9->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Downloading openai-0.28.1-py3-none-any.whl (76 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m77.0/77.0 kB[0m [31m2.1 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from llama-index>=0.6.9->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (1.5.3)
    Collecting tiktoken>=0.3.3 (from llama-index>=0.6.9->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Downloading tiktoken-0.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.0/2.0 MB[0m [31m34.0 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting urllib3<3,>=1.21.1 (from requests>=2.28->genai_stack==0.2.5)
      Downloading urllib3-1.26.17-py2.py3-none-any.whl (143 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m143.4/143.4 kB[0m [31m16.0 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: joblib in /usr/local/lib/python3.10/dist-packages (from nltk->sentence-transformers==2.2.2->genai_stack==0.2.5) (1.3.2)
    Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/dist-packages (from nltk->sentence-transformers==2.2.2->genai_stack==0.2.5) (2023.6.3)
    Collecting coloredlogs (from onnxruntime>=1.14.1->chromadb==0.4.5->genai_stack==0.2.5)
      Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m46.0/46.0 kB[0m [31m5.2 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: flatbuffers in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb==0.4.5->genai_stack==0.2.5) (23.5.26)
    Requirement already satisfied: protobuf in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb==0.4.5->genai_stack==0.2.5) (3.20.3)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from posthog>=2.4.0->chromadb==0.4.5->genai_stack==0.2.5) (1.16.0)
    Collecting monotonic>=1.5 (from posthog>=2.4.0->chromadb==0.4.5->genai_stack==0.2.5)
      Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)
    Collecting backoff>=1.10.0 (from posthog>=2.4.0->chromadb==0.4.5->genai_stack==0.2.5)
      Downloading backoff-2.2.1-py3-none-any.whl (15 kB)
    Requirement already satisfied: python-dateutil>2.1 in /usr/local/lib/python3.10/dist-packages (from posthog>=2.4.0->chromadb==0.4.5->genai_stack==0.2.5) (2.8.2)
    Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain>=0.0.232->genai_stack==0.2.5) (3.0.0)
    Collecting huggingface-hub>=0.4.0 (from sentence-transformers==2.2.2->genai_stack==0.2.5)
      Downloading huggingface_hub-0.17.3-py3-none-any.whl (295 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m295.0/295.0 kB[0m [31m25.7 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting safetensors>=0.3.1 (from transformers<5.0.0,>=4.6.0->sentence-transformers==2.2.2->genai_stack==0.2.5)
      Downloading safetensors-0.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.3/1.3 MB[0m [31m57.4 MB/s[0m eta [36m0:00:00[0m
    [?25hINFO: pip is looking at multiple versions of uvicorn[standard] to determine which version is compatible with other requirements. This could take a while.
    Collecting uvicorn[standard]>=0.18.3 (from chromadb==0.4.5->genai_stack==0.2.5)
      Downloading uvicorn-0.23.1-py3-none-any.whl (59 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m59.5/59.5 kB[0m [31m7.6 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting httptools>=0.5.0 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Downloading httptools-0.6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (428 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m428.8/428.8 kB[0m [31m37.7 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting python-dotenv>=0.13 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Downloading python_dotenv-1.0.0-py3-none-any.whl (19 kB)
    Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Downloading uvloop-0.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.1 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m4.1/4.1 MB[0m [31m106.6 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting watchfiles>=0.13 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Downloading watchfiles-0.20.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.3/1.3 MB[0m [31m87.4 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting websockets>=10.4 (from uvicorn==0.23.0->genai_stack==0.2.5)
      Downloading websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m129.9/129.9 kB[0m [31m15.5 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting deprecated (from atlassian-python-api->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5)
      Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)
    Requirement already satisfied: oauthlib in /usr/local/lib/python3.10/dist-packages (from atlassian-python-api->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (3.2.2)
    Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.10/dist-packages (from atlassian-python-api->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (1.3.1)
    Collecting pycryptodome (from pdfminer->llama-index-sl<0.6.0.0,>=0.5.3.1->genai_stack==0.2.5)
      Downloading pycryptodome-3.19.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.1/2.1 MB[0m [31m90.1 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn->sentence-transformers==2.2.2->genai_stack==0.2.5) (3.2.0)
    Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.10/dist-packages (from sympy->torch<3.0.0,>=2.0.1->genai_stack==0.2.5) (1.3.0)
    Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/local/lib/python3.10/dist-packages (from torchvision->sentence-transformers==2.2.2->genai_stack==0.2.5) (9.4.0)
    Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography>=3.2->authlib<2.0.0,>=1.2.1->weaviate-client<4.0.0,>=3.24.1->genai_stack==0.2.5) (1.16.0)
    Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain>=0.0.232->genai_stack==0.2.5)
      Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
    Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>=1.14.1->chromadb==0.4.5->genai_stack==0.2.5)
      Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m86.8/86.8 kB[0m [31m11.1 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: wrapt<2,>=1.10 in /usr/local/lib/python3.10/dist-packages (from deprecated->atlassian-python-api->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (1.15.0)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->llama-index>=0.6.9->llama-hub<0.0.35,>=0.0.34->genai_stack==0.2.5) (2023.3.post1)
    Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography>=3.2->authlib<2.0.0,>=1.2.1->weaviate-client<4.0.0,>=3.24.1->genai_stack==0.2.5) (2.21)
    Building wheels for collected packages: genai_stack, sentence-transformers, chroma-hnswlib, llama-index-sl, transformers3, pypika, pdfminer
      Building wheel for genai_stack (pyproject.toml) ... [?25l[?25hdone
      Created wheel for genai_stack: filename=genai_stack-0.2.5-py3-none-any.whl size=107822 sha256=11c93ef1f0141df7ec4c37f5d0b8bb04d043a0708dfa3d1de0376e4dd47e0a04
      Stored in directory: /tmp/pip-ephem-wheel-cache-5csrt_7f/wheels/b9/03/67/7e401543bcc3b9b2b3b252ab53315c904d89305fda7d8feff0
      Building wheel for sentence-transformers (setup.py) ... [?25l[?25hdone
      Created wheel for sentence-transformers: filename=sentence_transformers-2.2.2-py3-none-any.whl size=125923 sha256=882b7bc850ea67805119a192d0094426d6e5f5677f4b60d44b332d3a199ba471
      Stored in directory: /root/.cache/pip/wheels/62/f2/10/1e606fd5f02395388f74e7462910fe851042f97238cbbd902f
      Building wheel for chroma-hnswlib (pyproject.toml) ... [?25l[?25hdone
      Created wheel for chroma-hnswlib: filename=chroma_hnswlib-0.7.2-cp310-cp310-linux_x86_64.whl size=2285751 sha256=ecc9317da616c50f39bff042056a3c7ae82b73fca7b2287c33c7465360c03073
      Stored in directory: /root/.cache/pip/wheels/11/2b/0d/ee457f6782f75315bb5828d5c2dc5639d471afbd44a830b9dc
      Building wheel for llama-index-sl (setup.py) ... [?25l[?25hdone
      Created wheel for llama-index-sl: filename=llama_index_sl-0.5.3.1-py3-none-any.whl size=243025 sha256=de1e90c388b7ef7d03f26c31daaf07553219da8b80b7aec7078f9f27a1c9be47
      Stored in directory: /root/.cache/pip/wheels/86/92/4b/95ffab17e0d9757af366501bddd812b440be4c7f13189ea818
      Building wheel for transformers3 (setup.py) ... [?25l[?25hdone
      Created wheel for transformers3: filename=transformers3-0.0.0a1-py3-none-any.whl size=1060 sha256=0ebb19ba0f7c3f101d1ac4fedbace41cddb0262c4ba517c7430989df059e88a0
      Stored in directory: /root/.cache/pip/wheels/0d/05/15/4572317cd07a820797f50dd3e32225c0d9b3c1eadd13f909c9
      Building wheel for pypika (pyproject.toml) ... [?25l[?25hdone
      Created wheel for pypika: filename=PyPika-0.48.9-py2.py3-none-any.whl size=53723 sha256=88655390de8be184c3b6cff3fee946008366c2b620f771d1973f45405f88520d
      Stored in directory: /root/.cache/pip/wheels/e1/26/51/d0bffb3d2fd82256676d7ad3003faea3bd6dddc9577af665f4
      Building wheel for pdfminer (setup.py) ... [?25l[?25hdone
      Created wheel for pdfminer: filename=pdfminer-20191125-py3-none-any.whl size=6140072 sha256=876c05acda8eee6ad48cdfcc4e774f91ae4355ccb9dea204725139b0a204704c
      Stored in directory: /root/.cache/pip/wheels/4e/c1/68/f7bd0a8f514661f76b5cbe3b5f76e0033d79f1296012cbbf72
    Successfully built genai_stack sentence-transformers chroma-hnswlib llama-index-sl transformers3 pypika pdfminer
    Installing collected packages: transformers3, sentencepiece, pypika, monotonic, websockets, validators, uvloop, urllib3, safetensors, retrying, python-dotenv, pypdf, pycryptodome, pulsar-client, overrides, mypy-extensions, marshmallow, mako, jsonpointer, humanfriendly, httptools, html2text, h11, deprecated, chroma-hnswlib, backoff, watchfiles, uvicorn, typing-inspect, starlette, pdfminer, jsonpatch, coloredlogs, tiktoken, posthog, openai, onnxruntime, llama-index-sl, langsmith, huggingface-hub, gpt4all, fastapi, dataclasses-json, authlib, weaviate-client, tokenizers, langchain, atlassian-python-api, transformers, llama-index, chromadb, llama-hub, sentence-transformers, genai_stack
      Attempting uninstall: urllib3
        Found existing installation: urllib3 2.0.6
        Uninstalling urllib3-2.0.6:
          Successfully uninstalled urllib3-2.0.6
    Successfully installed atlassian-python-api-3.41.2 authlib-1.2.1 backoff-2.2.1 chroma-hnswlib-0.7.2 chromadb-0.4.5 coloredlogs-15.0.1 dataclasses-json-0.5.14 deprecated-1.2.14 fastapi-0.99.1 genai_stack-0.2.5 gpt4all-1.0.12 h11-0.14.0 html2text-2020.1.16 httptools-0.6.0 huggingface-hub-0.17.3 humanfriendly-10.0 jsonpatch-1.33 jsonpointer-2.4 langchain-0.0.312 langsmith-0.0.43 llama-hub-0.0.34 llama-index-0.8.43.post1 llama-index-sl-0.5.3.1 mako-1.2.4 marshmallow-3.20.1 monotonic-1.6 mypy-extensions-1.0.0 onnxruntime-1.16.1 openai-0.28.1 overrides-7.4.0 pdfminer-20191125 posthog-3.0.2 pulsar-client-3.3.0 pycryptodome-3.19.0 pypdf-3.14.0 pypika-0.48.9 python-dotenv-1.0.0 retrying-1.3.4 safetensors-0.4.0 sentence-transformers-2.2.2 sentencepiece-0.1.99 starlette-0.27.0 tiktoken-0.5.1 tokenizers-0.14.1 transformers-4.34.0 transformers3-0.0.0a1 typing-inspect-0.9.0 urllib3-1.26.17 uvicorn-0.23.0 uvloop-0.17.0 validators-0.22.0 watchfiles-0.20.0 weaviate-client-3.24.2 websockets-11.0.3


## Setup your API Key


```python
import os
from getpass import getpass
```


```python

api_key= ""
os.environ['OPENAI_API_KEY'] = ""
```

## Import required modules


```python
from genai_stack.stack.stack import Stack
from genai_stack.etl.langchain import LangchainETL
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
from genai_stack.retriever.langchain import LangChainRetriever
from genai_stack.memory.langchain import ConversationBufferMemory

from genai_stack.etl.utils import get_config_from_source_kwargs
from genai_stack.embedding.utils import get_default_embeddings
from genai_stack.etl.langchain import LangchainETL
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.etl.utils import get_config_from_source_kwargs
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
```


```python

```

## ETL -  "Extract, Transform, and Load."

- Add your data here. Check documentation for the required loaders


```python
config = {
    "model_name": "sentence-transformers/all-mpnet-base-v2",
    "model_kwargs": {"device": "cpu"},
    "encode_kwargs": {"normalize_embeddings": False},
}



config = {
    "name": "JSONLoader",
    "fields": {
        "file_path": "/content/drive/MyDrive/genai/books.json",
         "jq_schema": '.[]',
        "content_key":"country",

    }
}



# Create ETL


etl =LangchainETL.from_kwargs(**config)
```



## Create Default Embeddings


```python
emd =get_default_embeddings()
```



## Define your LLM - Large Language Model


```python
# Create model
model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": ""} # Update with your OpenAI Key
)
```



## Define The VectorDB


```python
vb =ChromaDB.from_kwargs()
```



# Connect the ETL, Embedding and Vectordb Component Using Stack


```python

stack = Stack(model=model, embedding=emd, etl=etl, vectordb=vb)
```


    Downloading (…)a8e1d/.gitattributes:   0%|          | 0.00/1.18k [00:00<?, ?B/s]



    Downloading (…)_Pooling/config.json:   0%|          | 0.00/190 [00:00<?, ?B/s]



    Downloading (…)b20bca8e1d/README.md:   0%|          | 0.00/10.6k [00:00<?, ?B/s]



    Downloading (…)0bca8e1d/config.json:   0%|          | 0.00/571 [00:00<?, ?B/s]



    Downloading (…)ce_transformers.json:   0%|          | 0.00/116 [00:00<?, ?B/s]



    Downloading (…)e1d/data_config.json:   0%|          | 0.00/39.3k [00:00<?, ?B/s]



    Downloading pytorch_model.bin:   0%|          | 0.00/438M [00:00<?, ?B/s]



    Downloading (…)nce_bert_config.json:   0%|          | 0.00/53.0 [00:00<?, ?B/s]



    Downloading (…)cial_tokens_map.json:   0%|          | 0.00/239 [00:00<?, ?B/s]



    Downloading (…)a8e1d/tokenizer.json:   0%|          | 0.00/466k [00:00<?, ?B/s]



    Downloading (…)okenizer_config.json:   0%|          | 0.00/363 [00:00<?, ?B/s]



    Downloading (…)8e1d/train_script.py:   0%|          | 0.00/13.1k [00:00<?, ?B/s]



    Downloading (…)b20bca8e1d/vocab.txt:   0%|          | 0.00/232k [00:00<?, ?B/s]



    Downloading (…)bca8e1d/modules.json:   0%|          | 0.00/349 [00:00<?, ?B/s]



```python

```

## Run Your ETL


```python

etl.run()


```


```python
model.predict("In which language book Things Fall Apart book is ")
```

    WARNING:langchain.llms.base:Retrying langchain.chat_models.openai.ChatOpenAI.completion_with_retry.<locals>._completion_with_retry in 4.0 seconds as it raised ServiceUnavailableError: The server is overloaded or not ready yet..





    {'output': 'Things Fall Apart is a novel written in English by Nigerian author Chinua Achebe.'}





# Add Your Documents To Vectordb


```python
# Add your documents
from langchain.docstore.document import Document as LangDocument

stack.vectordb.add_documents(
            documents=[
                LangDocument(
                    page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
                )
            ]
        )

```




    ['ed077608-68d4-11ee-90a7-0242ac1c000c']





## Do Similarity Search In Vectordb


```python
stack.vectordb.search("tell me name of author from india")
```




    [Document(page_content='India', metadata={'seq_num': 94, 'source': '/content/drive/MyDrive/genai/books.json'}),
     Document(page_content='India', metadata={'seq_num': 51, 'source': '/content/drive/MyDrive/genai/books.json'}),
     Document(page_content='India', metadata={'seq_num': 96, 'source': '/content/drive/MyDrive/genai/books.json'}),
     Document(page_content='India', metadata={'seq_num': 51, 'source': '/content/drive/MyDrive/genai/books.json'})]




```python
# query it
query = "tell me name of author from india"
docs = stack.vectordb.similarity_search(query)

# print results
print(docs[0].page_content)
```

    India




