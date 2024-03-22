import os
from werkzeug.utils import secure_filename
from Modules.authorization import connect_to_mongodb

UPLOAD_FOLDER = 'uploads'

def save_pdf(file, username):
    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        # Update MongoDB to store the document information
        db = connect_to_mongodb()
        db.users.update_one({'username': username}, {'$push': {'documents': {'filename': filename, 'path': file_path}}})
        
        return True
    else:
        return False
