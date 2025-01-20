import qrcode

def generate_qr_from_input(output_file="custom_qr.png"):
    """
    Generate a QR code based on user input and save it as an image file.

    Args:
    output_file (str): The filename for the generated QR code image.
    """
    try:
        # Prompt the user to input the text or URL
        user_input = input("Enter the text, URL, or data to generate a QR code: ")

        # Validate input
        if not user_input.strip():
            print("Input cannot be empty. Please enter valid text or data.")
            return

        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)  # Add the user-provided data to the QR code
        qr.make(fit=True)  # Adjust the size of the QR code

        # Create an image of the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code as an image file
        qr_image.save(output_file)
        print(f"QR code successfully generated and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the QR Code Generator!")
    generate_qr_from_input()
