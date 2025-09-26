import requests
import os
from urllib.parse import urlparse

# Define a maximum file size in bytes (e.g., 10 MB) to prevent excessively large downloads.
# This is a precaution when downloading from unknown sources.
MAX_FILE_SIZE = 10 * 1024 * 1024

def main():
    """
    A tool for mindfully collecting images from the web.
    It prompts the user for URLs, fetches the images, and saves them
    while implementing checks for safety and efficiency.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # A list to store the filenames of successfully downloaded files in this session
    downloaded_files = []

    # Loop to allow the user to input multiple URLs
    while True:
        url = input("Please enter an image URL (or type 'done' to finish): ")
        
        # Break the loop if the user is finished
        if url.lower() == 'done':
            break
        
        # Skip empty input
        if not url:
            continue

        try:
            # Create a dedicated directory for fetched images
            os.makedirs("Fetched_Images", exist_ok=True)

            # --- Implement precautions for unknown sources ---
            # Using stream=True allows us to check headers before downloading the full content,
            # which is an important precaution for large or malicious files.
            with requests.get(url, stream=True, timeout=10) as response:
                response.raise_for_status()  # Raise an exception for bad status codes

                # Check Content-Type header to ensure it's an image.
                content_type = response.headers.get('Content-Type', '')
                if not content_type.startswith('image/'):
                    print(f"✗ Failed to fetch {url}: The URL does not point to an image. (Content-Type: {content_type})")
                    continue

                # Check Content-Length to prevent downloading excessively large files.
                content_length = int(response.headers.get('Content-Length', 0))
                if content_length > MAX_FILE_SIZE:
                    print(f"✗ Failed to fetch {url}: File size ({content_length} bytes) exceeds the maximum limit ({MAX_FILE_SIZE} bytes).")
                    continue
                
                # --- Implement a feature that prevents downloading duplicate images ---
                # Extract the filename from the URL, or use a default if it's not present.
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
                
                # Create the full file path.
                filepath = os.path.join("Fetched_Images", filename)
                
                # Check for existing file to prevent duplicates.
                if os.path.exists(filepath):
                    print(f"✓ Skipping {url}: A file named '{filename}' already exists. Our community values shared resources and avoids unnecessary duplicates.")
                    continue
                
                # Check if the file has already been downloaded in this session.
                if filename in downloaded_files:
                    print(f"✓ Skipping {url}: '{filename}' was already downloaded in this session. Let's work together and avoid redundancy.")
                    continue

                # Save the image content mindfully, in chunks.
                with open(filepath, 'wb') as f:
                    # Using iter_content is a good practice for large files
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Record the successful download
                downloaded_files.append(filename)
                
                print(f"✓ Successfully fetched: {filename}")
                print(f"✓ Image saved to {filepath}")
                print("\nConnection strengthened. Community enriched.")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An unexpected error occurred for {url}: {e}")

    print("\nAll downloads processed.")
    print("Faith in the web restored. The spirit of Ubuntu lives on.")
    if downloaded_files:
        print("\nSummary of successful downloads:")
        for name in downloaded_files:
            print(f"  - {name}")

if __name__ == "__main__":
    main()
