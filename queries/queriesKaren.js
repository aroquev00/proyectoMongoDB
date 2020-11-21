// Query 2.1
db.covidMexico.aggregate( [ {$match:{INTUBADO: "SI"}},{ $group : { _id: "$TABAQUISMO", total: {$sum: 1}}}])

// Query 2.2
db.covidMexico.aggregate( [ {$match:{INTUBADO: "SI"}},{ $group : { _id:{Padece_Tabaquismo: "$TABAQUISMO"}, total: {$sum: 1}}},{$project:{Porcentaje_total :{ $multiply: [ { $divide: [ "$total",db.covidMexico.find({"INTUBADO":"SI"}).count()] }, 100] }}}])

// Query 3
(db.covidMexico.find({ "$and": [ {INTUBADO: "SI"},{ FECHA_DEF:{$ne: ISODate("1970-01-01T00:00:00.000+00:00")}}]}).count()/db.covidMexico.find({INTUBADO: "SI"}).count())*100

// Query 4
db.covidMexico.aggregate( [ {$match:{INTUBADO: "SI"}},{ $group : { _id:{Edad: "$EDAD"}, total: {$sum: 1}}},{$sort:{"_id.Edad":1}}])
