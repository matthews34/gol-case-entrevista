FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1 

# Create and change to the app directory.
# WORKDIR /app

# Copy local code to the container image.
COPY . ./

# Install project dependencies
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry install

# Run the web service on container startup.
CMD ["poetry", "run", "gunicorn", "case_gol:create_app()"]