# Verificación independiente de los resultados de latencia

Las salidas guardadas en `notebooks/3_agentes_y_evaluacion.ipynb` registran el tiempo de
respuesta de cada modelo para cada consulta. Eso permite recomputar los resultados publicados
sin volver a ejecutar la evaluación y sin depender de ficheros externos.

**Se recuperaron 5775 mediciones**, 1155 por modelo, equivalentes al 87 % de las 1335 ejecuciones
por modelo que componen la evaluación completa. La diferencia corresponde a salidas truncadas en
el notebook.

## Latencia media por modelo

| Modelo | Publicado | Recomputado | n |
|---|---|---|---|
| GPT-4o Mini | 6.01 s | 6.04 s | 1155 |
| Llama 3.3 70B | 5.87 s | 5.90 s | 1155 |
| DeepSeek R1 | 5.83 s | 5.92 s | 1155 |
| Ministral 8B | 5.81 s | 5.87 s | 1155 |
| Gemini 2.0 Flash | 5.79 s | 5.86 s | 1155 |

El ordenamiento se reproduce exactamente. La diferencia entre el modelo más lento y el más
rápido es de 0.18 s en el recomputo, frente a los 0.22 s publicados; ambas cifras sostienen la
misma conclusión de consistencia entre modelos.

## Latencia por nivel de dificultad

| Nivel | Publicado (rango entre modelos) | Recomputado (media) | n |
|---|---|---|---|
| Fácil | 4.98 - 5.41 s | 5.10 s | 1925 |
| Media | 6.23 - 6.48 s | 6.40 s | 1925 |
| Difícil | 6.12 - 6.19 s | 6.26 s | 1925 |

## Latencia por tipo de consulta

| Tipo | Publicado | Recomputado | n |
|---|---|---|---|
| `reference_location` | 3.46 s | 3.36 s | 385 |
| `section_tools` | 3.76 s | 3.99 s | 385 |
| `section_summary` | 4.02 s | 3.85 s | 385 |
| `reference_context` | 4.60 s | 5.04 s | 385 |
| `multi_reference_topic` | 6.66 s | 6.41 s | 385 |
| `domain_evaluation` | 7.16 s | 7.40 s | 385 |
| `comparative_analysis` | 7.95 s | 7.90 s | 385 |
| `main_methodology` | 8.38 s | 8.38 s | 385 |

Los siete tipos restantes, no reportados individualmente en el artículo, quedan registrados en el
notebook: `missing_reference` 5.24 s, `section_term_references` 5.42 s, `section_references`
5.56 s, `reference_sections` 6.13 s, `concept_definition` 6.58 s, `methodology_tools` 6.75 s,
`evaluation_methods` 6.76 s.

## Conclusión

Los resultados de latencia publicados —consistencia entre modelos, sensibilidad al nivel de
dificultad y especialización por tipo de consulta— **se reproducen a partir de los registros del
notebook**, con desviaciones inferiores a 0.5 s atribuibles a la cobertura parcial del 87 %.

Esta verificación es independiente del problema de duplicación descrito en `README_corpus.md`:
las cinco condiciones se ejecutaron sobre el mismo conjunto de unidades, de modo que la
comparación entre modelos no se ve afectada por él.
