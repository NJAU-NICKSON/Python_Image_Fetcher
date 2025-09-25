import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one if not available."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # Fallback if no filename found in URL
        filename = "downloaded_image.jpg"
    return filename

def get_file_hash(filepath):
    """Generate SHA256 hash of a file to check for duplicates."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def fetch_image(url, save_dir="Fetched_Images"):
    """Download and save an image from a URL with Ubuntu principles in mind."""
    try:
        os.makedirs(save_dir, exist_ok=True)

        # Request with headers (respectful client)
        headers = {
            "User-Agent": "UbuntuFetcher/1.0 (Respectful Client)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping: {url} (Not an image, Content-Type={content_type})")
            return

        # Prepare filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(save_dir, filename)

        # Avoid duplicate by checking hash if file exists
        if os.path.exists(filepath):
            existing_hash = get_file_hash(filepath)
            new_hash = hashlib.sha256(response.content).hexdigest()
            if existing_hash == new_hash:
                print(f"✓ Skipped duplicate: {filename}")
                return
            else:
                # Append unique suffix
                base, ext = os.path.splitext(filename)
                filename = f"{base}_copy{ext}"
                filepath = os.path.join(save_dir, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter one or more image URLs (separate by spaces): ").split()

    if not urls:
        print("✗ No URLs provided. Exiting.")
        return

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
