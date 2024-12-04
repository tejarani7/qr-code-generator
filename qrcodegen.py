import qrcode


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str, pdf_url: str):
        try:
            # Add the URL of the PDF
            self.qr.add_data(pdf_url)
            self.qr.make(fit=True)  # Make sure the QR code fits the data

            # Create and save the QR code as an image
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f"QR code successfully created and saved as {file_name}")
        except Exception as e:
            print(f"Error: {e}")


def main():
    # URL of your resume PDF (replace this with your actual link)
    pdf_url = "https://drive.google.com/file/d/1NhAbVwBVH2r2cjTy9xhAPIwWbNBXlD31/view?usp=sharing"

    myqr = MyQR(size=10, padding=4)  # Adjust size and padding as needed
    myqr.create_qr(file_name="resume_qrcode.png", fg="black", bg="white", pdf_url=pdf_url)


if __name__ == "__main__":
    main()


