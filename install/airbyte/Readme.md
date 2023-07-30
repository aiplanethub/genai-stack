# Airbyte

Airbyte is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes and databases

## Download and Install

### You can download and install Airbyte by running the below command:

```bash
llmstk dli-airbyte -destination <destination folder where it needs to be implemented>
```

**Example:**

```bash
llmstk dli-airbyte -destination /tmp/airbyte-temp
```

### Manual Installation

1. Airbyte setup requires you to have _docker_, _docker compose_ and _git_ installed, hence its recommended to have those packages installed.
2. Clone the repository
    ```bash
    git clone https://github.com/airbytehq/airbyte.git
    ```
3. Go into the cloned airbyte folder
    ```bash
    cd airbyte
    ```
4. Run the following command in the same directory

    ```bash
    ./run-ab-platform.sh
    ```

5. Now you should be able to access it at [http://localhost:8000](http://localhost:8000)

**Note:** If you want to modify any configurations, you can edit it in _.env_ you get after your run it for the first time.

Reference - [https://docs.airbyte.com/quickstart/deploy-airbyte/](https://docs.airbyte.com/quickstart/deploy-airbyte/)
