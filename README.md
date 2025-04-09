# LangChain-Based Celebrity Search Application (Local Model)

This Streamlit application allows you to search for information about celebrities using a local Large Language Model (LLM) powered by LangChain and CTransformers.

## Overview

The application takes a celebrity name as input and then uses a sequence of LangChain prompts and the local LLM to retrieve and display the following information:

1.  **General Information:** A brief description of the celebrity.
2.  **Date of Birth:** The celebrity's birth date.
3.  **Major Events Around Birth Date:** Five significant world events that occurred around the time of the celebrity's birth.

The application utilizes `ConversationBufferMemory` to maintain context between the different stages of the information retrieval process.

## Technologies Used

* **Streamlit:** For creating the interactive web interface.
* **LangChain:** A framework for developing applications powered by language models.
* **CTransformers:** A library for running transformer models (like LLaMA) locally on your CPU or GPU.

## Prerequisites

Before running this application, you need to:

1.  **Install Python:** Ensure you have Python 3.7 or higher installed on your system.
2.  **Install Required Libraries:** Install the necessary Python packages using pip:
    ```bash
    pip install streamlit langchain ctransformers
    ```
3.  **Download a Local LLaMA Model:** You need to download a compatible GGUF format LLaMA model (or a similar model supported by CTransformers). The current code is configured for a `mistral-7b-v0.1.Q5_K_M.gguf` model. You can find various models on platforms like Hugging Face.
4.  **Update Model Path:** **Crucially, you need to modify the `model` path in the `main.py` file to point to the actual location of your downloaded model.**

    ```python
    local_llm = CTransformers(
        model="Your_Path/mistral-7b-v0.1.Q5_K_M.gguf",  # 👈 UPDATE THIS PATH
        model_type="llama",
        config={
            "temperature": 0.8,
            "max_new_tokens": 200
        }
    )
    ```

## Setup and Running the Application

This project has already been initialized as a Git repository and the initial commit has been made. The remote origin has also been added. To run the application:

1.  **Clone the Repository (if you haven't already):**
    ```bash
    git clone [https://github.com/SwarajSD/LangChain-Based-Celebrity-Search-Application.git](https://github.com/SwarajSD/LangChain-Based-Celebrity-Search-Application.git)
    cd LangChain-Based-Celebrity-Search-Application
    ```
2.  **Navigate to the Project Directory:** Make sure your terminal is in the project directory.
3.  **Run the Streamlit Application:** Execute the following command in your terminal:
    ```bash
    streamlit run main.py
    ```

    This will automatically open the application in your web browser.

## Usage

1.  Enter the name of a celebrity in the text input field.
2.  Press Enter or click outside the input field.
3.  The application will process your request using the local LLM and display the results, including general information, date of birth, and major events around that time.
4.  You can expand the sections labeled "Person Info," "DOB Info," and "Major Events Around DOB" to see the step-by-step information retrieved by the LangChain pipeline.

## Important Notes

* The quality of the results depends on the capabilities and the data the local LLM was trained on.
* Running large language models locally can be computationally intensive. The performance of the application might vary depending on your system's hardware (CPU, RAM).
* Ensure that the path to your local LLM model in `main.py` is correct.
* This application demonstrates a basic implementation of a celebrity search using a local LLM and LangChain. It can be further enhanced with more sophisticated prompting, error handling, and user interface improvements.

## Git Commands Used (for your reference)

The following Git commands were used to initialize and set up the repository:

* `echo "# LangChain-Based-Celebrity-Search-Application" >> README.md`: Created the initial README file.
* `git init`: Initialized a new Git repository.
* `git add README.md`: Staged the `README.md` file.
* `git commit -m "first commit"`: Created the first commit.
* `git branch -M main`: Renamed the default branch to `main`.
* `git remote add origin https://github.com/SwarajSD/LangChain-Based-Celebrity-Search-Application.git`: Added the remote repository on GitHub.
* `git push -u origin main`: Pushed the local `main` branch to the remote `origin` repository and set up tracking.

## License

This project is for educational purposes. Free to use and adapt.

---

## Author

**Swaraj SD**  
🔗 [GitHub Profile](https://github.com/SwarajSD)