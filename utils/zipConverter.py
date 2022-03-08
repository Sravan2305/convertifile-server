import os
import zipfile
import io
from fastapi.responses import Response
from fastapi import HTTPException


def zip_files(filenames, result_file_name: str):
    zip_filename = result_file_name.split(".")[0] + ".zip"

    s = io.BytesIO()
    zf = zipfile.ZipFile(s, "w")

    count = 1
    try:
        for fpath in filenames:
            # Calculate path for file in zip
            fdir, fname = os.path.split(fpath)
            # Add file, at correct path
            zf.write(os.path.join(os.path.dirname(__file__), '../results/' + fname), fname[36:])
            count += 1

        # Must close zip for all contents to be written
        zf.close()
    except:
        return HTTPException(status_code=500, detail="Error writing zip file")
    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = Response(s.getvalue(), media_type="application/x-zip-compressed", headers={
        "Access-Control-Expose-Headers": "Content-Disposition",
        'Content-Disposition': f'filename={zip_filename}'
    })

    return resp
