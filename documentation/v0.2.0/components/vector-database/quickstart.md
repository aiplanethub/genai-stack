# 🔥 Quickstart

For quickstart, you can rely on the default embedding utils. By default we use "**HuggingFaceEmbedding**" This eliminates the need to configure embeddings, making the process effortless.

To utilize the vectordb configuration with the default embedding:

**=> Vectordb Usage**

<pre class="language-python"><code class="lang-python">from langchain.docstore.document import Document as LangDocument

from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.vectordb.weaviate_db import Weaviate
from genai_stack.embedding.utils import get_default_embedding
from genai_stack.stack.stack import Stack
<strong>
</strong><strong>
</strong>embedding = get_default_embedding()
chromadb = ChromaDB.from_kwargs()
chroma_stack = Stack(model=None, embedding=embedding, vectordb=chromadb)

# Add your documents
chroma_stack.vectordb.add_documents(
            documents=[
                LangDocument(
                    page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
                )
            ]
        )
chroma_stack.vectordb.search("page")

# Output 
# Your search results 
</code></pre>
