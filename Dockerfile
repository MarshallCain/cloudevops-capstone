FROM python:3.10.12-slim-bookworm

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . app.py requirements.txt testflask.py /app/
COPY static /app/static/
COPY templates /app/templates/


## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

## Step 4:
# Expose port 9090
Expose 9090

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]