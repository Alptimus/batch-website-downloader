# 🕸️ Batch Website Downloader

A Python script to recursively download full websites using `wget`, ideal for offline access, archiving, or mirroring.

## 🚀 Features

* Supports multiple URLs via command-line or input file
* Preserves directory structure and page assets
* Converts links for offline browsing
* Optional output directory support
* Built-in error handling and verbose output

## 📦 Prerequisites

* Python 3.6+
* `wget` installed and available in your system's PATH

## 🔧 Installation

1. Clone the repository:([GitHub][1])

   ```bash
   git clone https://github.com/yourusername/batch-wget-downloader.git
   cd batch-wget-downloader
   ```



2. Ensure `wget` is installed:

   ```bash
   wget --version
   ```



If not installed, refer to [GNU Wget](https://www.gnu.org/software/wget/) for installation instructions.

## ⚙️ Usage

### Download a Single URL

```bash
python3 batch_wget.py https://example.com/page1
```



### Download Multiple URLs

```bash
python3 batch_wget.py https://example.com/page1 https://site.org/another
```



### Use a File with URLs

```bash
python3 batch_wget.py -f urls.txt
```



Where `urls.txt` contains one URL per line.([GitHub][2])

### Specify an Output Directory

```bash
python3 batch_wget.py -f urls.txt -o downloads/
```



### Full Command-Line Options

```bash
python3 batch_wget.py -h
```



```
usage: batch_wget.py [-h] [-f FILE] [-o OUTPUT_DIR] [urls ...]

Batch-download multiple sites with wget.

positional arguments:
  urls                  List of URLs to download. If none specified, use --file.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to a text file containing one URL per line.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory in which to store all downloads (passed to wget -P).
```



## 🧪 Example

```bash
python3 batch_wget.py -f urls.txt -o saved_sites/
```



This command will download all websites listed in `urls.txt` and save them in the `saved_sites/` directory.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

* Built using Python's `subprocess` module
* Relies on the powerful `wget` tool for downloading

---