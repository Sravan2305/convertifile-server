from fastapi import UploadFile


def save_file(file: UploadFile, path: str, file_counter: str = ""):
    file_location = f"{path}{file_counter}{file.filename}"
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
            return True
    except:
        return False
