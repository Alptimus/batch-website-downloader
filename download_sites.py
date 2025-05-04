import sys
import subprocess
from pathlib import Path

# Configuration: wget options
WGET_OPTS = [
    "--recursive",
    "--no-clobber",
    "--page-requisites",
    "--html-extension",
    "--convert-links",
    "--restrict-file-names=windows",
    "--no-parent"
]

def download_url(url: str, output_dir: Path = None):
    """
    Runs wget with the predefined options on the given URL.
    If output_dir is provided, passes -P <output_dir> to wget.
    """
    cmd = ["wget"] + WGET_OPTS + ["--domains", url.split("/")[2]]
    if output_dir:
        cmd += ["-P", str(output_dir)]
    cmd.append(url)
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error downloading {url}: {e}", file=sys.stderr)

def load_urls_from_file(path: Path):
    """Reads URLs from a file, one per line, stripping whitespace and skipping blank lines."""
    with path.open() as f:
        for line in f:
            url = line.strip()
            if url and not url.startswith("#"):
                yield url

def main():
    import argparse
    p = argparse.ArgumentParser(
        description="Batch-download multiple sites with wget."
    )
    p.add_argument(
        "urls", nargs="*",
        help="List of URLs to download. If none specified, use --file."
    )
    p.add_argument(
        "-f", "--file", type=Path, default=None,
        help="Path to a text file containing one URL per line."
    )
    p.add_argument(
        "-o", "--output-dir", type=Path, default=None,
        help="Directory in which to store all downloads (passed to wget -P)."
    )
    args = p.parse_args()

    # Collect URLs
    urls = list(args.urls)
    if args.file:
        if not args.file.exists():
            print(f"[!] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        urls.extend(load_urls_from_file(args.file))

    if not urls:
        print("[!] No URLs provided. Specify them as arguments or via --file.", file=sys.stderr)
        sys.exit(1)

    # Process each URL
    for url in urls:
        download_url(url, args.output_dir)

if __name__ == "__main__":
    main()