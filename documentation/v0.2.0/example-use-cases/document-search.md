# 📄 AI Assisted Document Search

<a href="https://colab.research.google.com/drive/1boAeMXgdPpwDU_TeZmNx3HkPT5Slas_9">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Requirements

-   Python environment with necessary packages installed.
-   GenAI Stack library and its dependencies.
-   Weaviate, an open-source vector search engine, installed and
    configured if it is used as the underlying VectorDB.
-   A dataset or source documents for indexing and searching.


``` python
from genai_stack.embedding.langchain import LangchainEmbedding[doc-search.ipynb](doc-search.ipynb)
from genai_stack.etl.langchain import LangchainETL
from genai_stack.stack.stack import Stack
from genai_stack.vectordb import ChromaDB
from genai_stack.vectordb.weaviate_db import Weaviate
```

## Search single document

Search a single document using etl and vector database.

``` python
embedding = LangchainEmbedding.from_kwargs(
    name="HuggingFaceEmbeddings",
    fields={
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
)
chromadb = ChromaDB.from_kwargs()
etl = LangchainETL.from_kwargs(
    name="PyPDFLoader", fields={
        "file_path": "<your_file>.pdf",
    }
)
stack = Stack(
    model=None,
    embedding=embedding,
    vectordb=chromadb,
    etl=etl
)
```

``` python
doc = chromadb.similarity_search("Who provide technical assistance to computer system users?")
```

``` python
for i in doc:
    print(i.metadata)
```
output
```
{'page': 2, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data/2A2C2V4WI5YRDJHR26XUD4IAULIYGTMA.pdf'}
{'page': 2, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data/2A2C2V4WI5YRDJHR26XUD4IAULIYGTMA.pdf'}
{'page': 2, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data/2A2C2V4WI5YRDJHR26XUD4IAULIYGTMA.pdf'}
{'page': 1, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data/2A2C2V4WI5YRDJHR26XUD4IAULIYGTMA.pdf'}
```
## Search multiple documents

Search a directory containing documents. Returns a list of documents
with path and page number.

``` python
embedding = LangchainEmbedding.from_kwargs(
    name="HuggingFaceEmbeddings",
    fields={
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
)
db = Weaviate.from_kwargs(
    url="http://localhost:8080/",
    index_name="Testing",
    text_key="test",
    attributes=["source", "page"]
)
```

``` python
file_folder = "<your_file_directory>"
```

``` python
import os
os.listdir(file_folder)
```
output
```
['2A2C2V4WI5YRDJHR26XUD4IAULIYGTMA.pdf',
 '2ED27NR7CISW7J4PHXXBZ6OFPVDFHMFB.pdf',
 '2EDEPZ4VHTLPTWSZR6FAVUJ3B2ZVSIPS.pdf',
 '2F73J4NP2YHKVISKHDIDJ7RGPDKTQZ7D.pdf',
 '2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf',
 '2LVOKCURIEQKLK43I6T7QLYYQX3RQUXX.pdf',
 '2QCQAIXCPZZPZPEEBHJT4WUB5BA42DCP.pdf',
 '2QWDF5JK4N7WQ4NQRZRLF4CYOUF32WTR.pdf']
```
``` python
etl = LangchainETL.from_kwargs(
    name="DirectoryLoader", fields={
        "path": file_folder,
        "glob" : "*.pdf",
        "loader_cls":"langchain.document_loaders.PyPDFLoader",
        "use_multithreading":True,
        "show_progress": True
    }
)
stack = Stack(
    model=None,
    embedding=embedding,
    vectordb=db,
    etl=etl
)
```


``` python
doc = db.similarity_search("Who provide technical assistance to computer system users?")

[{
    "content": i.page_content,
    "page": i.metadata["page"],
    "path": i.metadata["source"]
} for i in doc]
```
output
```
[{'content': 'Revised  January 10, 2014  \n \nJUDICIAL INTERN  HIRING INFORMATION  \nLorna G. Schofield , United States District Judge  \n \nChambers  Contact Information :         \nUnited States District Court      \nSouthern District of New York              \n40 Centre Street, Room 20 1      \nNew York, NY  10007  \n(212) 805 -0288 \n \nPositions :  Judge Schofield hires first - and second -year law students as interns during the school \nyear and for summer employment .  During the school year, interns must be available for a \nsemester at least 20 hours a week.  During the summer, interns must be available to work full \ntime for at least eight weeks.   \nApplications :  Applications should include a resume, transcript and writi ng sample.   First-year \nstudents should not apply until they have received grades from all of their first semester classes.   ',
  'page': 0,
  'path': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'},
 {'content': 'Revised  January 10, 2014  \n \nJUDICIAL INTERN  HIRING INFORMATION  \nLorna G. Schofield , United States District Judge  \n \nChambers  Contact Information :         \nUnited States District Court      \nSouthern District of New York              \n40 Centre Street, Room 20 1      \nNew York, NY  10007  \n(212) 805 -0288 \n \nPositions :  Judge Schofield hires first - and second -year law students as interns during the school \nyear and for summer employment .  During the school year, interns must be available for a \nsemester at least 20 hours a week.  During the summer, interns must be available to work full \ntime for at least eight weeks.   \nApplications :  Applications should include a resume, transcript and writi ng sample.   First-year \nstudents should not apply until they have received grades from all of their first semester classes.   ',
  'page': 0,
  'path': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'},
 {'content': 'Revised  January 10, 2014  \n \nJUDICIAL INTERN  HIRING INFORMATION  \nLorna G. Schofield , United States District Judge  \n \nChambers  Contact Information :         \nUnited States District Court      \nSouthern District of New York              \n40 Centre Street, Room 20 1      \nNew York, NY  10007  \n(212) 805 -0288 \n \nPositions :  Judge Schofield hires first - and second -year law students as interns during the school \nyear and for summer employment .  During the school year, interns must be available for a \nsemester at least 20 hours a week.  During the summer, interns must be available to work full \ntime for at least eight weeks.   \nApplications :  Applications should include a resume, transcript and writi ng sample.   First-year \nstudents should not apply until they have received grades from all of their first semester classes.   ',
  'page': 0,
  'path': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'},
 {'content': 'Revised  January 10, 2014  \n \nJUDICIAL INTERN  HIRING INFORMATION  \nLorna G. Schofield , United States District Judge  \n \nChambers  Contact Information :         \nUnited States District Court      \nSouthern District of New York              \n40 Centre Street, Room 20 1      \nNew York, NY  10007  \n(212) 805 -0288 \n \nPositions :  Judge Schofield hires first - and second -year law students as interns during the school \nyear and for summer employment .  During the school year, interns must be available for a \nsemester at least 20 hours a week.  During the summer, interns must be available to work full \ntime for at least eight weeks.   \nApplications :  Applications should include a resume, transcript and writi ng sample.   First-year \nstudents should not apply until they have received grades from all of their first semester classes.   ',
  'page': 0,
  'path': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'}]
```

``` python
doc = db.similarity_search("Chambers Contact Information:")
```

``` python
for i in doc:
    print(i.metadata)
```
output
```
{'page': 0, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'}
{'page': 0, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'}
{'page': 0, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'}
{'page': 0, 'source': '/home/akshaj/Documents/AIPlanet/DocumentSearch/data-2/2KQDEYIMQDVT2DUARRCJV5HEUYY2HO7H.pdf'}
```

Checkout the notebook [here](https://colab.research.google.com/drive/1boAeMXgdPpwDU_TeZmNx3HkPT5Slas_9) for more details.
