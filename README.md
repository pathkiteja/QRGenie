QR Code Generator

----->>> This is a Python-based QR Code Generator application that allows users to generate QR codes from text, URLs, or any other data. The generated QR code is saved as an image file for further use.

Features
  -> Input Flexibility: Accepts text, URLs, or any other data as input.
      Customizable Output: Saves the QR code as a PNG file with a customizable filename.
      High Error Correction: Uses qrcode.constants.ERROR_CORRECT_H for robust error correction.
      User-Friendly Output: Prompts users with clear input instructions and provides helpful feedback.



Code Explanation
   ->  Main Functionality
       generate_qr_from_input(output_file="custom_qr.png"):
       Prompts the user for input.
       Validates the input to ensure it's not empty.
       Uses the qrcode library to generate a QR code with the specified error correction level, box size, and border.
       Saves the QR code as an image file.

Before running the application, ensure you have Python installed on your system. You also need to install the required library:

   pip install qrcode[pil]

### Video Demonstration

[Click here to watch the video demonstration](20250124-1628-50.0566174.mp4)
