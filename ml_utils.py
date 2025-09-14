from transformers import pipeline
from PIL import Image


captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")


def generate_alt_text(image_path: str) -> str:
    """Generate caption for an image."""
    img = Image.open(image_path)
    result = captioner(img)
    return result[0]['generated_text']


def detect_objects(image_path: str, top_k: int = 5) -> list[str]:
    """Return top-k object labels for an image."""
    img = Image.open(image_path)
    results = classifier(img, top_k=top_k)
    return [r['label'] for r in results]
