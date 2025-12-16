import os
from dotenv import load_dotenv
from imagekitio import ImageKit

load_dotenv()

# SDK auto-detects from .env - no parameters needed!
imagekit = ImageKit()