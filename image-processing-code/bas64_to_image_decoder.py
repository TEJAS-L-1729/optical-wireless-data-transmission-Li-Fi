"""
Base64 -> Image Decoder
========================
Reconstructs an image from the Base64 string received over the Li-Fi (VLC)
link (either read live from the Arduino over serial, or from a saved text
file). Usage:

    python bas64_to_image_decoder.py --serial-port COM5 -o received.png
    python bas64_to_image_decoder.py --text-file encoded.txt -o received.png
"""

import argparse
import base64


def decode_and_save(base64_str: str, output_path: str):
    image_bytes = base64.b64decode(base64_str)
    with open(output_path, "wb") as f:
        f.write(image_bytes)
    print(f"Image reconstructed and saved to {output_path}")


def read_from_serial(port: str, baud: int) -> str:
    import serial  # imported here so --text-file mode doesn't require pyserial

    with serial.Serial(port, baud, timeout=10) as ser:
        line = ser.readline().decode("utf-8").strip()
    return line


def main():
    parser = argparse.ArgumentParser(description="Decode a Base64 string back into an image.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--serial-port", help="Serial port to read the Base64 string from (e.g. COM5, /dev/ttyUSB0)")
    source.add_argument("--text-file", help="Path to a text file containing the Base64 string")
    parser.add_argument("--baud", type=int, default=250000, help="Baud rate for serial mode (default: 250000)")
    parser.add_argument("-o", "--output", default="received.png", help="Output image path (default: received.png)")
    args = parser.parse_args()

    if args.serial_port:
        base64_str = read_from_serial(args.serial_port, args.baud)
    else:
        with open(args.text_file) as f:
            base64_str = f.read().strip()

    decode_and_save(base64_str, args.output)


if __name__ == "__main__":
    main()
