import express from 'express';
import morgan from 'morgan';
import path from 'node:path';

const app = express();
const PORT = 3000;

app.use(express.static(path.join(path.resolve(), 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(morgan('dev'));

app.post('/multiplicar-matrices', (req, res) => {
    const { matriz1, matriz2 } = req.body;

    // Validar que las matrices puedan multiplicarse
    if (matriz1[0].length !== matriz2.length) {
        return res.status(400).json({ error: 'El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz' });
    }

    // Multiplicar las matrices
    const resultado = [];
    for (let i = 0; i < matriz1.length; i++) {
        const fila = [];
        for (let j = 0; j < matriz2[0].length; j++) {
            let suma = 0;
            for (let k = 0; k < matriz1[0].length; k++) {
                suma += matriz1[i][k] * matriz2[k][j];
            }
            fila.push(suma);
        }
        resultado.push(fila);
    }

    res.json({ resultado });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});