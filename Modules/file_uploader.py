import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

def save_pdf(file):
    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return True
    else:
        return False
