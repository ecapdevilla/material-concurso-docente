#!/usr/bin/env python3
"""Inventario NO destructivo. Uso: python auditar_repo.py /ruta/repo"""
import csv, hashlib, pathlib, sys, collections
repo=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
if not (repo/'.git').exists(): print('AVISO: no encontré .git; revisar ruta.')
script=pathlib.Path(__file__).resolve().parent
rows=[]
for p in sorted(repo.rglob('*')):
 if not p.is_file() or '.git' in p.relative_to(repo).parts: continue
 try:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
  rows.append([p.relative_to(repo).as_posix(),p.suffix.lower(),p.stat().st_size,h.hexdigest()])
 except OSError:pass
with (script/'inventario_repo.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['ruta','extension','bytes','sha256']);w.writerows(rows)
counts=collections.Counter(row[1] or '(sin extension)' for row in rows)
(script/'resumen_repo.txt').write_text(f'Ruta: {repo}\nArchivos: {len(rows)}\n'+''.join(f'{ext}: {n}\n' for ext,n in counts.most_common()),encoding='utf-8')
print(f'Inventario completo: {len(rows)} archivos -> {script / "inventario_repo.csv"}')
