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


with open('datosPrueba.csv', mode='r') as csvFile:
  csvReader = csv.DictReader(csvFile)
  for row in csvReader:
    print(row["FECHA_ACTUALIZACION"] + " " + dictOrigen(row["ORIGEN"]))
