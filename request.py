import requests
import time
from concurrent.futures import ThreadPoolExecutor
import sys

# Define endpoint URLs
urls = {
    "serverless": "https://us-central1-cmpt756-413805.cloudfunctions.net/bert-test",
    "serverful": "http://35.224.81.129:8080/predict"
}

# Get the deployment type from command line argument
deployment_type = sys.argv[1] if len(sys.argv) > 1 else "serverless"

# Select the URL based on deployment type
url = urls.get(deployment_type, urls["serverless"])

# A list of 10 different sentences to send as data
sentences = [
    "Hello, I'm a [MASK] person.",
    "This is a [MASK] day.",
    "I love to play [MASK] games.",
    "She is a great [MASK].",
    "This [MASK] is very delicious.",
    "He is working as a [MASK].",
    "My favorite animal is a [MASK].",
    "I am learning [MASK] language.",
    "This movie is incredibly [MASK].",
    "She has a beautiful [MASK]."
]

# Function to send request
def send_request(sentence):
    response = requests.post(url, json={"sentence": sentence})
    return response

# Start timer
start_time = time.time()

# Send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request, sentence) for sentence in sentences]

# Wait for all futures to complete
for future in futures:
    future.result()

# Stop timer
end_time = time.time()

# Calculate total response time
total_response_time = end_time - start_time

# Print the URL and total response time
print(f"URL: {url}")
print(f"Total response time for 10 concurrent requests to {deployment_type}: {total_response_time:.2f} seconds")
