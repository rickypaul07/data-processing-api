# Data Processing API

## Overview
This API allows users to upload CSV files, obtain data summaries, apply transformations, and generate visualizations.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/data-processing-api.git
    cd data-processing-api
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python run.py
    ```

## Endpoints

### 1. Upload Data

- **URL:** `/upload`
- **Method:** `POST`
- **Description:** Upload a CSV file.
- **Curl Command:**

    ```bash
    curl -X POST http://localhost:5000/upload \
      -F "file=@/path/to/your/file.csv"
    ```

- **Response Example:**

    ```json
    {
        "message": "File uploaded successfully",
        "file_id": "unique_file_identifier"
    }
    ```

### 2. Get Data Summary

- **URL:** `/summary/<file_id>`
- **Method:** `GET`
- **Description:** Get a summary of the uploaded data including descriptive statistics and data types.
- **Curl Command:**

    ```bash
    curl -X GET http://localhost:5000/summary/<file_id>
    ```

- **Response Example:**

    ```json
    {
        "summary": {
            "col1": {
                "mean": 10.5,
                "median": 10,
                "std": 2.5,
                "dtype": "int"
            },
            ...
        }
    }
    ```

### 3. Transform Data

- **URL:** `/transform/<file_id>`
- **Method:** `POST`
- **Description:** Apply transformations to the data (e.g., normalization, handling missing values).
- **Curl Command:**

    ```bash
    curl -X POST http://localhost:5000/transform/<file_id> \
      -H "Content-Type: application/json" \
      -d '{
            "transformations": {
                "normalize": ["col1", "col2"],
                "fill_missing": {"col3": 0}
            }
          }'
    ```

- **Response Example:**

    ```json
    {
        "message": "Transformations applied successfully",
        "file_id": "unique_file_identifier_after_transformation"
    }
    ```

### 4. Visualize Data

- **URL:** `/visualize/<file_id>`
- **Method:** `GET`
- **Description:** Generate visualizations (e.g., histograms, scatter plots) based on specified columns.
- **Curl Command:**

    ```bash
    curl -X GET "http://localhost:5000/visualize/<file_id>?chart_type=histogram&columns=col1&columns=col2" \
      --output output_image.png
    ```

- **Response Example:**

    - The image will be saved as `output_image.png`.

## Testing

1. **Run Tests:**

    ```bash
    python -m unittest discover -s tests
    ```
