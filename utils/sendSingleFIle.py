from starlette.responses import FileResponse
import os
from models import fileFormats

"""
Send a single file as a response.
"""


def send_single_file(file_path: str, to_format: str) -> FileResponse:
    fdir, fname = os.path.split(file_path)
    if to_format == fileFormats.FileFormats.TEXT:
        return FileResponse(os.path.join(os.path.dirname(__file__), '../results/' + fname),
                            media_type='application/octet-stream', filename=fname[36:])
    if [fileFormats.FileFormats.JPEG, fileFormats.FileFormats.PNG, fileFormats.FileFormats.JPG].__contains__(
            to_format) != -1:
        return FileResponse(os.path.join(os.path.dirname(__file__), '../results/' + fname),
                            media_type='image/', filename=fname[36:])
    if to_format == fileFormats.FileFormats.PDF:
        return FileResponse(os.path.join(os.path.dirname(__file__), '../results/' + fname),
                            media_type='application/pdf', filename=fname[36:])
