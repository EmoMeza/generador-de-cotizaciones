from fastapi import FastAPI, UploadFile, Response
import pandas as pd

app = FastAPI()


@app.post("/excel-to-pdf")
async def excel_to_pdf(file: UploadFile):
    # Lee el Excel directamente desde el archivo subido
    df = pd.read_excel(file.file)

    # Convierte a columnas + filas
    columns = list(df.columns)
    rows = df.values.tolist()

    # Genera el PDF
    pdf_bytes = generate_pdf(columns, rows)

    return Response(pdf_bytes, media_type="application/pdf")
