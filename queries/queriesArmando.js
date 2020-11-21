// Query 1
db.covidMexico.aggregate([
  { $match: {INTUBADO: "SI" } },
  { $group: { _id: {Hipertension: "$HIPERTENSION", Diabetes: "$DIABETES"}, TOTALES: {$sum: 1}, FALLECIDOS: {$sum: {$cond: [{$ne: [ISODate("1970-01-01T00:00:00.000+00:00"), "$FECHA_DEF"]}, 1, 0]} } } },
  { $project: {_id: 1, porcentajeFallecidos: { $divide: [ "$FALLECIDOS", "$TOTALES" ] } } }
])

// Query 5
db.covidMexico.aggregate([
  { $match: {FECHA_DEF: {$ne: ISODate("1970-01-01T00:00:00.000+00:00")} } },
  { $project: { DIAS_DIF: {$trunc: [{ $divide: [{ $subtract: ["$FECHA_DEF", "$FECHA_INGRESO"] }, 1000 * 60 * 60 * 24] }, 1 ] }, TOTAL: {$sum: 1}, FECHA_DEF: 1, FECHA_INGRESO: 1 } },
  { $group: { _id: {diasAFallecimiento: "$DIAS_DIF"}, CUENTA: {$sum: 1} } },
  {$sort:{"CUENTA":-1}}
])

// Query 6
db.covidMexico.aggregate([
  { $match: {CLASIFICACION_FINAL: { $in: ["CASO DE COVID-19 CONFIRMADO POR ASOCIACIÓN CLÍNICA EPIDEMIOLÓGICA", "CASO DE COVID-19 CONFIRMADO POR COMITÉ DE  DICTAMINACIÓN", "CASO DE SARS-COV-2  CONFIRMADO POR LABORATORIO", "CASO SOSPECHOSO"] } } },
  { $group: { _id: "$SECTOR", TOTALES: {$sum: 1}, FALLECIDOS: {$sum: {$cond: [{$ne: [ISODate("1970-01-01T00:00:00.000+00:00"), "$FECHA_DEF"]}, 1, 0]} } } },
  { $project: {_id: 1, porcentajeFallecidos: { $divide: [ "$FALLECIDOS", "$TOTALES" ] }, casosPositivosTotales: "$TOTALES" } },
  {$sort:{"porcentajeFallecidos":-1}}
])
