# paperRag — experimentos

Notebooks que producen los resultados del artículo **«Sistema multi-agente basado en RAG y LLMs
para el análisis contextual de citas en documentos científicos»**, enviado a la revista
TecnoLógicas.

Este repositorio contiene el código **tal como se ejecutó** para la evaluación reportada. Para el
prototipo de aplicación interactiva, posterior y reimplementado, ver
[`Rodato/paperRag`](https://github.com/Rodato/paperRag).

> Los dos repositorios **no** son la misma implementación. Este usa **PyMuPDF** para la
> extracción de PDF, que es lo que describe la Sección 2.2 del artículo. La aplicación migró
> después a `docling`. Para reproducir los resultados publicados, usar estos notebooks.

## Contenido

| Notebook | Qué hace |
|---|---|
| `1_construccion_vectorstores.ipynb` | Extracción con PyMuPDF, identificación de secciones y referencias por prompting, chunking dual e indexación en ChromaDB y FAISS |
| `2_vectorstores_extendido.ipynb` | Variante con metadatos enriquecidos y medición de tiempos de indexación |
| `3_agentes_y_evaluacion.ipynb` | Grafo de cinco agentes en LangGraph, generación de las 15 consultas por artículo, y arnés de evaluación por lotes sobre los 5 modelos |
| `4_analisis_y_figuras.ipynb` | Análisis de latencia y generación de las Figuras 3 a 7 del artículo |

`evaluacion/plantillas_consultas.md` documenta el instrumento completo: las 15 plantillas con su
dificultad y tipo, la escala de la ejecución y las variables registradas.

## Cómo se ejecutaron

Los notebooks se corrieron en **Google Colab**, con los artículos en Google Drive y las claves de
API en el gestor de secretos de Colab (`google.colab.userdata`). Los secretos esperados son:

```
OPENAI_API_KEY        embeddings (text-embedding-ada-002) y GPT-4o Mini
GEMINI_API_KEY_1..4   Gemini 2.0 Flash (cuatro claves rotativas por límite de cuota)
MISTRAL_API_KEY       Ministral 8B
OPENROUTER_API_KEY    DeepSeek R1 Distill Qwen 32B y Llama 3.3 70B Instruct
```

Para correrlos fuera de Colab hay que reemplazar `userdata.get(...)` por lectura de variables de
entorno y ajustar las rutas `/content/drive/...` al sistema de archivos local.

Las salidas de las celdas se conservan a propósito: permiten inspeccionar los resultados
reportados sin volver a ejecutar la evaluación completa, que consume cuota de cinco proveedores
de API.

## Escala de la evaluación

89 artículos × 15 consultas × 5 modelos = **6675 ejecuciones** (1335 por modelo), en lotes de 20
artículos con puntos de control.

Modelos evaluados: GPT-4o Mini, Gemini 2.0 Flash, Ministral 8B, DeepSeek R1 Distill Qwen 32B y
Llama 3.3 70B Instruct.

## Alcance de los resultados

La evaluación midió **rendimiento operacional**: latencia por agente y por sistema, longitud de
respuesta, base de datos seleccionada y filtros extraídos.

**No** midió la corrección de las respuestas ni la de las decisiones internas de los agentes. El
campo `confidence` que aparece en los registros es `min(nº de fragmentos recuperados / 5, 1.0)`
—un recuento normalizado, no una medida de calidad— y `success` indica únicamente que la llamada
no lanzó una excepción. Cualquier afirmación sobre exactitud requiere un conjunto de referencia
anotado por evaluadores humanos, que no forma parte de esta ejecución y se aborda en trabajo
posterior.

## Cita

Ver `CITATION.cff`. La referencia al artículo se añadirá cuando se publique.

## Licencia

MIT — ver `LICENSE`.
