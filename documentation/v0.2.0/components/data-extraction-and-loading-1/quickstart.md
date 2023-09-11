# 🔥 Quickstart

There is a default embedding component you can use to quickstart. We use **HuggingFaceEmbeddings** by default so that we can run the embedding operation locally easily to give our users a good headstart.&#x20;

```
from genai_stack.embedding.utils import get_default_embeddings

embeddings = get_default_embeddings()
embeddings.embed_text("Your text to embed")
```
