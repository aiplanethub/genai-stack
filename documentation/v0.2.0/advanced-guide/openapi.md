# 🔃 GenAI Server API's Reference

Here are the API's for the core components of GenAI Stack Server.

## Session

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/session" method="get" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/session" method="post" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/session/{session_id}" method="get" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/session/{session_id}" method="delete" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}


# ETL

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/etl/submit-job" method="post" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}


# Model

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/model/predict" method="post" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}


# Retriever

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/retriever/retrieve" method="get" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}


# Vectordb

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/vectordb/add-documents" method="post" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/openapi.yaml" path="/api/vectordb/search" method="get" %}
[openapi.yaml](<../.gitbook/assets/openapi.yaml>)
{% endswagger %}