from PIL import Image

# Open image
img = Image.open("sample.jpg")

# Resize image
resized = img.resize((300, 300))
resized.save("resized.jpg")

# Convert to grayscale
gray = img.convert("L")
gray.save("grayscale.jpg")

# Rotate image
rotated = img.rotate(90)
rotated.save("rotated.jpg")

print("Image processing completed!")