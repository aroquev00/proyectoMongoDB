import csv
import codecs

# Cargar diccionario de Tipo Paciente
with open('dictOrigen.csv', mode='r') as origenCsv:
  reader = csv.reader(origenCsv)
  dictOrigen = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de Sector
with open('dictSector.csv', mode='r') as sectorCsv:
  reader = csv.reader(sectorCsv)
  dictSector = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de Sexo
with open('dictSexo.csv', mode='r') as sexoCsv:
  reader = csv.reader(sexoCsv)
  dictSexo = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de Tipo Paciente
with open('dictTipoPaciente.csv', mode='r') as tipoPacienteCsv:
  reader = csv.reader(tipoPacienteCsv)
  dictTipoPaciente = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de SI_NO
with open('dictSiNo.csv', mode='r') as siNoCsv:
  reader = csv.reader(siNoCsv)
  dictSiNo = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de nacionalidad
with open('dictNacionalidad.csv', mode='r') as nacionalidadCsv:
  reader = csv.reader(nacionalidadCsv)
  dictNacionalidad = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de resultado lab
with open('dictResultadoLab.csv', mode='r') as resultadoLabCsv:
  reader = csv.reader(resultadoLabCsv)
  dictResultadoLab = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de clasificación final
with open('dictClasificacionFinal.csv', mode='r') as clasificacionFinalCsv:
  reader = csv.reader(clasificacionFinalCsv)
  dictClasificacionFinal = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de entidades
with open('dictEntidades.csv', mode='r') as entidadesCsv:
  reader = csv.reader(entidadesCsv)
  dictEntidades = {rows[0]:rows[1] for rows in reader}

# Cargar diccionario de municipios
with open('dictMunicipios.csv', mode='r') as municipiosCsv:
  reader = csv.reader(municipiosCsv)
  dictMunicipios = {rows[0]:rows[1] for rows in reader}

def paisNacionalidad(key):
  if (key != "99"):
    return key
  else:
    return "SE IGNORA"

def paisOrigen(key):
  if (key != "97"):
    return key
  else:
    return "NO APLICA"

#with open('datosPrueba.csv', mode='r', encoding='utf-8') as csvFile:
with open('201102COVID19MEXICO.csv', mode='r', encoding='utf-8-sig') as csvFile:
  csvReader = csv.DictReader(csvFile)
  print(csvReader.fieldnames)
  with open('datosCovid.csv', mode='w') as csvOutFile:
    csvWriter = csv.DictWriter(csvOutFile, fieldnames=csvReader.fieldnames)
    csvWriter.writeheader()
    for row in csvReader:
      csvWriter.writerow({'FECHA_ACTUALIZACION': row["FECHA_ACTUALIZACION"], 'ID_REGISTRO': row["ID_REGISTRO"], 'ORIGEN': dictOrigen[row["ORIGEN"]], 'SECTOR': dictSector[row["SECTOR"]], 'ENTIDAD_UM': dictEntidades[row["ENTIDAD_UM"]], 'SEXO': dictSexo[row["SEXO"]], 'ENTIDAD_NAC': dictEntidades[row["ENTIDAD_NAC"]], 'ENTIDAD_RES': dictEntidades[row["ENTIDAD_RES"]], 'MUNICIPIO_RES': dictMunicipios[row["MUNICIPIO_RES"]], 'TIPO_PACIENTE': dictTipoPaciente[row["TIPO_PACIENTE"]], 'FECHA_INGRESO': row["FECHA_INGRESO"], 'FECHA_SINTOMAS': row["FECHA_SINTOMAS"], 'FECHA_DEF': row["FECHA_DEF"], 'INTUBADO': dictSiNo[row["INTUBADO"]], 'NEUMONIA': dictSiNo[row["NEUMONIA"]], 'EDAD': row["EDAD"], 'NACIONALIDAD': dictNacionalidad[row["NACIONALIDAD"]], 'EMBARAZO': dictSiNo[row["EMBARAZO"]], 'HABLA_LENGUA_INDIG': dictSiNo[row["HABLA_LENGUA_INDIG"]], 'INDIGENA': dictSiNo[row["INDIGENA"]], 'DIABETES': dictSiNo[row["DIABETES"]], 'EPOC': dictSiNo[row["EPOC"]], 'ASMA': dictSiNo[row["ASMA"]], 'INMUSUPR': dictSiNo[row["INMUSUPR"]], 'HIPERTENSION': dictSiNo[row["HIPERTENSION"]], 'OTRA_COM': dictSiNo[row["OTRA_COM"]], 'CARDIOVASCULAR': dictSiNo[row["CARDIOVASCULAR"]], 'OBESIDAD': dictSiNo[row["OBESIDAD"]], 'RENAL_CRONICA': dictSiNo[row["RENAL_CRONICA"]], 'TABAQUISMO': dictSiNo[row["TABAQUISMO"]], 'OTRO_CASO': dictSiNo[row["OTRO_CASO"]], 'TOMA_MUESTRA': dictSiNo[row["TOMA_MUESTRA"]], 'RESULTADO_LAB': dictResultadoLab[row["RESULTADO_LAB"]], 'CLASIFICACION_FINAL': dictClasificacionFinal[row["CLASIFICACION_FINAL"]], 'MIGRANTE': dictSiNo[row["MIGRANTE"]], 'PAIS_NACIONALIDAD': paisNacionalidad(row["PAIS_NACIONALIDAD"]), 'PAIS_ORIGEN': paisOrigen(row["PAIS_ORIGEN"]), 'UCI': dictSiNo[row["UCI"]]})
      
print("Done.")
