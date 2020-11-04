import csv

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

with open('datosPrueba.csv', mode='r') as csvFile:
  csvReader = csv.DictReader(csvFile)
  with open('datosCovid.csv', mode='w') as csvOutFile:
    csvWriter = csv.DictWriter(csvOutFile, fieldnames=csvReader.fieldnames)
    csvWriter.writeheader()
    for row in csvReader:
      csvWriter.writerow({})
     # print(f'{row["FECHA_ACTUALIZACION"]},{row["ID_REGISTRO"]},{dictOrigen[row["ORIGEN"]]},{dictSector[row["SECTOR"]]},{dictEntidades[row["ENTIDAD_UM"]]},{dictSexo[row["SEXO"]]},{dictEntidades[row["ENTIDAD_NAC"]]},{dictEntidades[row["ENTIDAD_RES"]]},{dictMunicipios[row["MUNICIPIO_RES"]]},{dictTipoPaciente[row["TIPO_PACIENTE"]]},{row["FECHA_INGRESO"]},{row["FECHA_SINTOMAS"]},{row["FECHA_DEF"]},{dictSiNo[row["INTUBADO"]]},{dictSiNo[row["NEUMONIA"]]},{row["EDAD"]},{dictNacionalidad[row["NACIONALIDAD"]]},{dictSiNo[row["EMBARAZO"]]},{dictSiNo[row["HABLA_LENGUA_INDIG"]]},{dictSiNo[row["INDIGENA"]]},{dictSiNo[row["DIABETES"]]},{dictSiNo[row["EPOC"]]},{dictSiNo[row["ASMA"]]},{dictSiNo[row["INMUSUPR"]]},{dictSiNo[row["HIPERTENSION"]]},{dictSiNo[row["OTRA_COM"]]},{dictSiNo[row["CARDIOVASCULAR"]]},{dictSiNo[row["OBESIDAD"]]},{dictSiNo[row["RENAL_CRONICA"]]},{dictSiNo[row["TABAQUISMO"]]},{dictSiNo[row["OTRO_CASO"]]},{dictSiNo[row["TOMA_MUESTRA"]]},{dictResultadoLab[row["RESULTADO_LAB"]]},{dictClasificacionFinal[row["CLASIFICACION_FINAL"]]},{dictSiNo[row["MIGRANTE"]]},{paisNacionalidad(row["PAIS_NACIONALIDAD"])},{paisOrigen(row["PAIS_ORIGEN"])},{dictSiNo[row["UCI"]]}')
