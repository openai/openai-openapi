# OpenAPI spec for the OpenAI API

This repository contains an [OpenAPI](https://www.openapis.org/) specification for the [OpenAI API](https://platform.openai.com/docs/api-reference).

## API Exploration Engine

This repository now includes an API exploration engine that allows you to call and simulate APIs based on the `openapi.yaml` file. Additionally, it includes a middleware layer to collect information from API requests and responses, providing metrics to the user.

### How to Use the API Exploration Engine

1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the API exploration engine:
   ```sh
   python api_explorer.py
   ```

### Middleware Layer

The middleware layer collects information from API requests and responses, providing metrics to the user. It is automatically integrated with the API exploration engine.

### Example Usage

Here is an example of how to use the API exploration engine and middleware layer:

```python
from api_explorer import APIExplorer
from middleware import Middleware

# Initialize the API Explorer
api_explorer = APIExplorer('openapi.yaml')

# Initialize the Middleware
middleware = Middleware()

# Call an API endpoint
response = api_explorer.call_api('/v1/engines', 'GET')

# Simulate an API endpoint
simulation_response = api_explorer.simulate_api('/v1/engines', 'GET')

# Collect metrics
metrics = middleware.collect_metrics()
print(metrics)
```

### Using the API Exploration Engine with Multiple AI

The API exploration engine can be used with multiple AI, such as Gemini and Anthropic. Here is an example:

```python
# Example for Gemini AI
response_gemini = api_explorer.call_api('/v1/gemini/engines', 'GET')
simulation_response_gemini = api_explorer.simulate_api('/v1/gemini/engines', 'GET')

# Example for Anthropic AI
response_anthropic = api_explorer.call_api('/v1/anthropic/engines', 'GET')
simulation_response_anthropic = api_explorer.simulate_api('/v1/anthropic/engines', 'GET')
```

### Including a New API

To include a new API in the exploration engine, follow these steps:

1. Update the `openapi.yaml` file with the new API specifications.
2. Add the necessary functions in `api_explorer.py` to handle the new API endpoints.
3. Use the new API endpoints in the same way as shown in the examples above.

### Using Docker to Run the Project

You can use Docker to run the project in a containerized environment. Follow these steps:

1. Build the Docker image:
   ```sh
   docker build -t openai-openapi .
   ```
2. Run the Docker container:
   ```sh
   docker run -p 5000:5000 openai-openapi
   ```

### Setting Up the Conda Environment

You can set up a Conda environment for the project using the `environment.yml` file. Follow these steps:

1. Create the Conda environment:
   ```sh
   conda env create -f environment.yml
   ```
2. Activate the Conda environment:
   ```sh
   conda activate openai-openapi
   ```

### Using Poetry to Manage Dependencies

You can use Poetry to manage the project's dependencies. Follow these steps:

1. Install Poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Install the dependencies:
   ```sh
   poetry install
   ```

### Setting Up a Virtual Environment

You can set up a virtual environment for the project using `venv`. Follow these steps:

1. Create the virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Installing the Pip Package

You can install the pip package for this project by running the following command:
```sh
pip install .
```

### Using the Pip Package

After installing the pip package, you can use the API exploration engine and middleware layer as follows:

```python
from openai_openapi.api_explorer import APIExplorer
from openai_openapi.middleware import Middleware

# Initialize the API Explorer
api_explorer = APIExplorer('openapi.yaml')

# Initialize the Middleware
middleware = Middleware()

# Call an API endpoint
response = api_explorer.call_api('/v1/engines', 'GET')

# Simulate an API endpoint
simulation_response = api_explorer.simulate_api('/v1/engines', 'GET')

# Collect metrics
metrics = middleware.collect_metrics()
print(metrics)
```
