// Query 7
db.covidMexico.aggregate( [{ $match: {CLASIFICACION_FINAL: { $in: ["CASO DE COVID-19 CONFIRMADO POR ASOCIACIÓN CLÍNICA EPIDEMIOLÓGICA", "CASO DE COVID-19 CONFIRMADO POR COMITÉ DE  DICTAMINACIÓN", "CASO DE SARS-COV-2  CONFIRMADO POR LABORATORIO", "CASO SOSPECHOSO"] } } },{ $group : { _id:{Edad: "$EDAD", Sexo:"$SEXO"}, total: {$sum: 1}}},{$sort:{"_id.Edad":1,"_id.Sexo":1 }}])

// Query 8
db.covidMexico.aggregate( [{ $match: {CLASIFICACION_FINAL: { $in: ["CASO DE COVID-19 CONFIRMADO POR ASOCIACIÓN CLÍNICA EPIDEMIOLÓGICA", "CASO DE COVID-19 CONFIRMADO POR COMITÉ DE  DICTAMINACIÓN", "CASO DE SARS-COV-2  CONFIRMADO POR LABORATORIO", "CASO SOSPECHOSO"] } } },{ $group : { _id:{Entidad: "$ENTIDAD_RES"}, total: {$sum: 1}}},{$sort:{total:-1 }}])

// Query 9
db.covidMexico.aggregate( [ {$match:{ FECHA_DEF:{$ne: ISODate("1970-01-01T00:00:00.000+00:00")}}},{ $group : {_id:{FechaDefuncion: "$FECHA_DEF"}, total: {$sum: 1}}},{$sort:{FechaDefuncion:1 }}])
