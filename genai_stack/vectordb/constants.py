from enum import Enum


DEFAULT_COLLECTION_NAME = "genstack"


class SearchMethod(Enum):
    SIMILARITY_SEARCH = "similarity_search"
    MAX_MARGINAL_RELEVANCE_SEARCH = "max_marginal_relevance_search"
