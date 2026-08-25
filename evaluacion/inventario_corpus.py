#!/usr/bin/env python3
"""Inventario y deduplicación del corpus por hash de contenido.

Uso:
    python3 inventario_corpus.py <directorio_con_pdfs> [--csv salida.csv]

Recorre los PDF, calcula el SHA-256 de cada uno y reporta cuántos documentos
únicos hay. Dos archivos con el mismo hash son byte a byte el mismo documento,
aunque tengan nombres distintos.

Motivo: el corpus de la evaluación original contenía entradas repetidas bajo
numeraciones distintas, lo que infla el recuento de artículos y sesga la
caracterización por dominio.
"""
import argparse, csv, hashlib, os, sys
from collections import defaultdict


def sha256(ruta, bloque=1 << 20):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for trozo in iter(lambda: f.read(bloque), b""):
            h.update(trozo)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directorio")
    ap.add_argument("--csv", help="escribe el inventario completo a este archivo")
    args = ap.parse_args()

    if not os.path.isdir(args.directorio):
        sys.exit(f"No es un directorio: {args.directorio}")

    por_hash = defaultdict(list)
    for raiz, _, archivos in os.walk(args.directorio):
        for nombre in sorted(archivos):
            if nombre.lower().endswith(".pdf"):
                ruta = os.path.join(raiz, nombre)
                por_hash[sha256(ruta)].append(os.path.relpath(ruta, args.directorio))

    total = sum(len(v) for v in por_hash.values())
    duplicados = {h: v for h, v in por_hash.items() if len(v) > 1}
    redundantes = sum(len(v) - 1 for v in duplicados.values())

    print(f"archivos PDF          : {total}")
    print(f"documentos únicos     : {len(por_hash)}")
    print(f"documentos repetidos  : {len(duplicados)}")
    print(f"archivos redundantes  : {redundantes}")

    if duplicados:
        print("\nrepeticiones (ordenadas por número de copias):")
        for h, v in sorted(duplicados.items(), key=lambda t: -len(t[1])):
            print(f"  ×{len(v)}  {v[0]}")
            for otro in v[1:]:
                print(f"        = {otro}")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["sha256", "n_copias", "archivo_canonico", "copias"])
            for h, v in sorted(por_hash.items(), key=lambda t: t[1][0]):
                w.writerow([h, len(v), v[0], " | ".join(v[1:])])
        print(f"\ninventario escrito en {args.csv}")

    return 1 if duplicados else 0


if __name__ == "__main__":
    sys.exit(main())
