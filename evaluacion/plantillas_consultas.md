# Instrumento de evaluación — 15 plantillas de consulta

Las consultas no son literales: son **plantillas parametrizadas** que se instancian para cada
artículo sustituyendo los marcadores por términos extraídos del propio documento
(`[REF_NUM]`, `[SECTION_NAME]`, `[MAIN_CONCEPT]`, `[DOMAIN_FIELD]`, `[DOMAIN_TASK]`,
`[DOMAIN_CONTEXT]`, `[SPECIFIC_TERM]`, `[TOPIC]`).

La estratificación por dificultad sigue el principio del benchmark GPQA; no se retomaron ni su
dominio, ni sus preguntas, ni su formato de opción múltiple.

Definición canónica: `notebooks/3_agentes_y_evaluacion.ipynb`, función
`generate_complete_gpqa_questions()`.

## Fáciles (E1-E5) — funcionalidades básicas

| ID | Plantilla | Tipo |
|----|-----------|------|
| E1 | ¿En qué secciones se menciona la referencia `[REF_NUM]`? | `reference_sections` |
| E2 | ¿Qué referencias tiene la sección de `[SECTION_NAME]`? | `section_references` |
| E3 | ¿Dónde aparece citado `[REF_NUM]`? | `reference_location` |
| E4 | Resume la sección de `[SECTION_NAME]` | `section_summary` |
| E5 | ¿Qué es `[MAIN_CONCEPT]`? | `concept_definition` |

## Intermedias (M1-M5) — integración multi-agente

| ID | Plantilla | Tipo |
|----|-----------|------|
| M1 | ¿Cómo se usa la referencia `[REF_NUM]` en la sección de `[SECTION_NAME]`? | `reference_context` |
| M2 | ¿En qué secciones aparecen las referencias `[REF_NUM1]` y `[REF_NUM2]` relacionadas con `[TOPIC]`? | `multi_reference_topic` |
| M3 | ¿Cuáles son las principales herramientas de `[DOMAIN_FIELD]` mencionadas en este paper? | `methodology_tools` |
| M4 | ¿Qué referencias de la sección `[SECTION_NAME]` mencionan específicamente `[SPECIFIC_TERM]`? | `section_term_references` |
| M5 | ¿Cuál es la metodología principal utilizada para `[DOMAIN_TASK]`? | `main_methodology` |

## Difíciles (H1-H5) — capacidades avanzadas

| ID | Plantilla | Tipo |
|----|-----------|------|
| H1 | ¿Cómo evalúan el rendimiento de los sistemas propuestos en esta investigación? | `evaluation_methods` |
| H2 | ¿Qué dice la referencia `[NONEXISTENT_REF]` sobre `[TOPIC]` en este paper? | `missing_reference` |
| H3 | ¿Qué metodologías de evaluación específicas para `[DOMAIN_CONTEXT]` se mencionan? | `domain_evaluation` |
| H4 | ¿Qué herramientas se mencionan en `[SECTION_NAME]`? | `section_tools` |
| H5 | ¿Cómo se comparan las diferentes aproximaciones según las métricas mencionadas en el paper? | `comparative_analysis` |

`H2` es deliberadamente insatisfacible: pregunta por una referencia que no existe en el
documento, para verificar que el sistema declare la ausencia de información en lugar de
completarla.

## Escala de la ejecución

| | |
|---|---|
| Artículos | 89 |
| Consultas por artículo | 15 |
| Modelos por consulta | 5 |
| Ejecuciones por modelo | 1335 |
| **Ejecuciones totales** | **6675** |

Cada consulta se ejecutó una sola vez por combinación de artículo y modelo. La evaluación se
organizó en lotes de 20 artículos con puntos de control que permitían reanudarla entre sesiones.

## Variables registradas

`latency`, `response_length`, `confidence`, `query_type`, `vectorstore_choice`,
`search_filters`, `num_results`, `difficulty`, `question_type`, `domain_detected`.

> **Alcance.** La instrumentación registró métricas temporales y estructurales. No capturó
> juicios de corrección sobre las respuestas ni sobre las decisiones internas de los agentes:
> `confidence` es `min(nº de fragmentos recuperados / 5, 1.0)`, es decir un recuento normalizado
> y no una medida de calidad. La evaluación de corrección requiere un conjunto de referencia
> anotado por evaluadores humanos, que no forma parte de esta ejecución.
