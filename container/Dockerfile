# syntax=docker/dockerfile:1

FROM python:3.9.2

WORKDIR /app




# Install PyTorch, TorchVision, and TorchAudio
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


# Install Flask and Transformers
RUN pip install flask transformers

COPY . .
# Expose port 8080
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "app.py"]