# Corpus de evaluación — estado verificado

## Resumen

La evaluación reportada en el artículo procesó **89 unidades de corpus**, cifra que consta en las
salidas de `notebooks/3_agentes_y_evaluacion.ipynb` (`Total papers: 89`, en lotes de 20).

Una auditoría posterior por hash de contenido detectó que **una parte de esas unidades son el
mismo documento bajo identificadores distintos**. El recuento de 89 corresponde por tanto a
unidades de procesamiento, no a documentos únicos.

| | |
|---|---|
| Unidades de corpus declaradas | 89 |
| Identificadores recuperables de las salidas del notebook | 71 |
| De ellos, verificables contra archivo local | 51 |
| Documentos únicos entre los verificables | **32** |
| Entradas redundantes confirmadas | **19** |
| Identificadores sin archivo local disponible | 20 |
| Identificadores no visibles en las salidas | 18 |

**Cota inferior de duplicación: 19 entradas (21 % del corpus).** El número real puede ser mayor:
38 de las 89 unidades no pudieron verificarse por no disponer de los archivos correspondientes.

## Ejemplos de duplicación confirmada

Documentos byte a byte idénticos evaluados bajo identificadores distintos:

| Documento | Identificadores |
|---|---|
| GPT-4 Technical Report | `paper_038`, `paper_058`, `paper_095` |
| LaMDA: Language Models for Dialog Applications | `paper_040`, `paper_060`, `paper_097` |
| Longformer: The Long-Document Transformer | `paper_042`, `paper_062`, `paper_099` |
| LoRA: Low-Rank Adaptation of Large Language Models | `paper_045`, `paper_065`, `paper_073` |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP | `paper_046`, `paper_066`, `paper_074` |
| REALM: Retrieval-Augmented Language Model Pre-Training | `paper_047`, `paper_067`, `paper_075` |

`corpus_manifiesto.csv` lista los 71 identificadores recuperados, su archivo local cuando existe,
el SHA-256 del contenido, el número de copias detectadas y el identificador canónico del grupo.

## Efecto sobre los resultados

**Afecta a la caracterización del corpus.** La distribución por dominio y las estadísticas
estructurales —número de secciones y de referencias por artículo— cuentan varias veces los
documentos repetidos. Dado que la mayoría de los duplicados son artículos sobre modelos de
lenguaje, la concentración temática real es mayor que la reportada.

**No afecta a la comparación entre modelos.** Los cinco modelos de lenguaje procesaron
exactamente el mismo conjunto de unidades, con las mismas consultas y en las mismas condiciones.
La diferencia máxima de latencia de 0.22 s y la distribución del tiempo de ejecución entre
agentes son comparaciones intra-sujeto y se mantienen válidas.

## Reproducción

```bash
python3 evaluacion/inventario_corpus.py <directorio_de_pdfs> --csv inventario.csv
```

Dos archivos con el mismo SHA-256 son el mismo documento, con independencia de su nombre.
