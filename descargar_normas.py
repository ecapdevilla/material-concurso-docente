#!/usr/bin/env python3
"""Descarga 7 normas oficiales y valida encabezado PDF. Ejecutar desde la raíz del repositorio."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
import sys

BASE = Path(__file__).resolve().parent / 'Estudio Concurso 2026' / '02-normas'
BASE.mkdir(parents=True, exist_ok=True)
DOCUMENTOS = {
 'constitucion-politica.pdf': ['https://dapre.presidencia.gov.co/normativa/normativa/Constitucion-Politica-Colombia-1991.pdf'],
 'ley-1346-2009.pdf': ['https://www.itrc.gov.co/Itrc/wp-content/uploads/2024/07/Ley_1346_de_2009.pdf', 'https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php/norma_pdf.php?i=37150'],
 'decreto-3782-2007.pdf': ['https://www.mineducacion.gov.co/1759/articles-135430_archivo_pdf.pdf'],
 'ley-2418-2024.pdf': ['https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/pdf/ley_2418_2024.pdf'],
 'ley-1437-2011.pdf': ['https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php/norma_pdf.php?i=41249'],
 'decreto-1743-1994.pdf': ['https://www.mineducacion.gov.co/1621/articles-103598_archivo_pdf.pdf'],
 'decreto-1384-2026.pdf': ['https://www.cancilleria.gov.co/normograma/compilacion/docs/pdf/decreto_1384_2026.pdf'],
}

def descargar(nombre, urls):
 destino=BASE/nombre
 if destino.exists() and destino.read_bytes()[:5] == b'%PDF-':
  print('YA EXISTE', nombre);return True
 for url in urls:
  try:
   req=Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; NormasConcurso/1.0)','Accept':'application/pdf,*/*'})
   with urlopen(req,timeout=40) as r: contenido=r.read()
   if not contenido.startswith(b'%PDF-'):raise ValueError('El servidor no devolvió un PDF')
   destino.write_bytes(contenido)
   print('OK',nombre,len(contenido),'bytes');return True
  except (OSError,ValueError,URLError) as exc: print('FALLÓ',nombre,url,str(exc))
 return False

if __name__=='__main__':
 resultados=[descargar(nombre,urls) for nombre,urls in DOCUMENTOS.items()]
 print(f'\n{sum(resultados)}/{len(resultados)} PDF descargados y validados')
 sys.exit(0 if all(resultados) else 1)
