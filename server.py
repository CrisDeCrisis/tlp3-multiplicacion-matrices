from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Matrices(BaseModel):
    matriz1: List[List[float]]
    matriz2: List[List[float]]

@app.post("/multiplicar-matrices")
async def multiplicar_matrices(matrices: Matrices):
    matriz1 = matrices.matriz1
    matriz2 = matrices.matriz2

    # Validar que las matrices puedan multiplicarse
    if len(matriz1[0]) != len(matriz2):
        raise HTTPException(status_code=400, detail="El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")

    # Multiplicar las matrices
    resultado = [
        [
            sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
            for j in range(len(matriz2[0]))
        ]
        for i in range(len(matriz1))
    ]

    return {"resultado": resultado}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)