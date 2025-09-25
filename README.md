# Ubuntu Requests
"I am because we are." – Ubuntu Philosophy

Ubuntu Requests is a Python tool inspired by the wisdom of Ubuntu.  
It connects to the global community of the internet, respectfully fetches images, and organizes them for sharing and later appreciation.

---

## Features
- Fetch images from one or more URLs
- Automatically organizes them into a `Fetched_Images` folder
- Gracefully handles errors (timeouts, bad URLs, invalid content)
- Avoids duplicate downloads using SHA256 hashing
- Checks HTTP headers to ensure only images are saved
- Uses respectful request headers (`User-Agent`)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/NJAU-NICKSON/Python_Image_Fetcher.git
   cd Ubuntu_Requests
````

2. Install required dependencies:

   ```bash
   pip install requests
   ```

---

## Usage

Run the script in your terminal:

```bash
python ubuntu_fetcher.py
```

You will see:

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separate by spaces):  https://unsplash-assets.imgix.net/marketing/studio/deck/6.jpg?w=336&dpr=1&q=80&h=441&auto=format&fit=crop
```

Example output:

```
✓ Successfully fetched: 6.jpg
✓ Image saved to Fetched_Images/6.jpg

Connection strengthened. Community enriched.
```

---

## Ubuntu Principles in Action

* Community → Connects to the wider web, sharing resources
* Respect → Handles errors gracefully without crashing
* Sharing → Stores images neatly for future appreciation
* Practicality → A real tool for collecting and organizing images

---

## Challenge Extensions

* Handle multiple URLs at once
* Avoid downloading duplicate images
* Verify `Content-Type` headers before saving
* Respectful request headers (`User-Agent`)

---

## License

This project is open-source and free to share in the spirit of Ubuntu.

---

"A person is a person through other persons." – Ubuntu Philosophy
Your program connects you to the work of others across the web.