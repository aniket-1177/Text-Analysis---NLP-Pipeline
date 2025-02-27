# Text Analysis - NLP Pipeline

This Flask web application performs text analysis, including:
* **Data Ingestion:** Takes .txt file as an input file to conduct analysis
* **Text Preprocessing:** Tokenization, stopword removal, and lemmatization.
* **Named Entity Recognition (NER):** Extraction of persons, organizations, and locations.
* **Sentiment Analysis:** Determining the sentiment of the text (positive, negative, or neutral).
* **Word Cloud Generation:** Visualizing the most frequent words.
* **TF-IDF Keyword Extraction:** Identifying the top 10 keywords.

## Installation

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/aniket-1177 Text-Analysis---NLP-Pipeline.git

    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    * **On macOS and Linux:**

        ```bash
        source .venv/bin/activate
        ```

    * **On Windows:**

        ```bash
        .venv\Scripts\activate
        ```

4.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Open your web browser:**

    * Navigate to `http://127.0.0.1:5000/`.

3.  **Upload a text file:**

    * Use the file upload form to select and upload your text file.

4.  **View the results:**

    * The results, including named entities, sentiment analysis, a word cloud, and top keywords, will be displayed on the results page.