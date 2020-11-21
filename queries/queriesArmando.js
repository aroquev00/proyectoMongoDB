// Query 1
db.covidMexico.aggregate([
  { $match: {INTUBADO: "SI" } },
  { $group: { _id: {Hipertension: "$HIPERTENSION", Diabetes: "$DIABETES"}, TOTALES: {$sum: 1}, FALLECIDOS: {$sum: {$cond: [{$ne: [ISODate("1970-01-01T00:00:00.000+00:00"), "$FECHA_DEF"]}, 1, 0]} } } },
  { $project: {_id: 1, numero: { $divide: [ "$FALLECIDOS", "$TOTALES" ] } } }
])



db.covidMexico.aggregate([
  { $match: {INTUBADO: "SI" } },
  { $project: {HIPERTENSION: 1, DIABETES: 1 , FALLECIDO: {$cond: [{$ne: [ISODate("1970-01-01T00:00:00.000+00:00"), "$FECHA_DEF"]}, 1, 0]} } },
  { $group: { _id: {Hipertension: "$HIPERTENSION", Diabetes: "$DIABETES"}, total: {$sum: 1} } },
  { $project: {_id: 1, numero: { $divide: ["$FALLECIDO", "$total"] } } }
])

db.covidMexico.aggregate([
  { $match: {INTUBADO: "SI" } },
  { $project: {HIPERTENSION: 1, DIABETES: 1 , FALLECIDO: {$cond: [{$ne: [ISODate("1970-01-01T00:00:00.000+00:00"), "$FECHA_DEF"]}, 1, 0]} } },
  { $group: { _id: {Hipertension: "$HIPERTENSION", Diabetes: "$DIABETES", Fallecido: "$FALLECIDO"}, total: {$sum: 1} } }
])

totales 