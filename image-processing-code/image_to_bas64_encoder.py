"""
Image -> Base64 Encoder
=======================
Converts an image file into a Base64 text string for transmission over the
Li-Fi (VLC) link. Usage:

    python image_to_bas64_encoder.py path/to/image.png
    python image_to_bas64_encoder.py path/to/image.png -o encoded.txt
"""

import argparse
import base64


def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description="Encode an image to a Base64 string.")
    parser.add_argument("image", help="Path to the input image file")
    parser.add_argument(
        "-o", "--output",
        help="Optional path to write the Base64 string to a .txt file. "
             "If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    base64_string = image_to_base64(args.image)

    if args.output:
        with open(args.output, "w") as f:
            f.write(base64_string)
        print(f"Base64 string written to {args.output}")
    else:
        print(base64_string)


if __name__ == "__main__":
    main()
