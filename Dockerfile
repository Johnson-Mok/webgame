FROM python:3.12-bookworm

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copy only the poetry files to install dependencies first
COPY pyproject.toml poetry.lock /app/

RUN poetry install --only main --no-root && rm -rf $POETRY_CACHE_DIR

# Copy the rest of the application code into the container
COPY src/ images/ /app/

# Expose the port that the Streamlit app will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "app.py"]
