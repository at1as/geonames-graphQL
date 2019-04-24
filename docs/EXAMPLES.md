# Example Queries

Many more complex queries can be created by understanding the Geoname data model (such as finding neighbors, etc). The following are some useful resources to help understand the database structure:

* http://download.geonames.org/export/dump/
* http://www.geonames.org/statistics/
* http://www.geonames.org/export/ws-overview.html

### Find by Geoname ID

#### Query
```
{
  geoname(geonameId: 1125426) {
    geonameId
    name
    asciiname
    Alternatenames(last:3) {
      edges {
        node {
          alternatename
          isoLanguage
        }
      }
    }
    latitude
    longitude
    admin1Code
    Admin1Code {
      geonameId
      code
    }
    admin2Code
    Admin2Code {
      name
      asciiname
      code
    }
    admin3Code
    admin4Code
    admin5Code {
      admin5Code
      geonameId
    }
    featureCode
    featureClass
    population
    countryCode
    CountryInfo {
      currency
      fipsCode
      isoAlpha3
      areaInSqKm
    }
  }
}
```

#### Response
```
{
  "data": {
    "geoname": [
      {
        "geonameId": "1125426",
        "name": "Shighnan District",
        "asciiname": "Shighnan District",
        "Alternatenames": {
          "edges": [
            {
              "node": {
                "alternatename": "Shughnan",
                "isoLanguage": ""
              }
            },
            {
              "node": {
                "alternatename": "Khughnan",
                "isoLanguage": ""
              }
            },
            {
              "node": {
                "alternatename": "Шугнан",
                "isoLanguage": "ru"
              }
            }
          ]
        },
        "latitude": 37.61667,
        "longitude": 71.45,
        "admin1Code": "01",
        "Admin1Code": null,
        "admin2Code": "1125426",
        "Admin2Code": {
          "name": "Shighnan District",
          "asciiname": "Shighnan District",
          "code": "AF.01.1125426"
        },
        "admin3Code": "",
        "admin4Code": "",
        "admin5Code": null,
        "featureCode": "ADM2",
        "featureClass": "A",
        "population": 0,
        "countryCode": "AF",
        "CountryInfo": {
          "currency": "AFN",
          "fipsCode": "AF",
          "isoAlpha3": "AFG",
          "areaInSqKm": 647500
        }
      }
    ]
  }
}
```

### Search Hierarchy

#### Query
```
{
  geoname(geonameId: 6115047) {
    name
    asciiname
    parents(first: 3) {
      edges {
        node {
          geonameId
          asciiname
        }
      }
    }
    children(first: 4) {
      edges {
        node {
          geonameId
          asciiname
        }
      }
    }
  }
}
```

#### Response
```
{
  "data": {
    "geoname": [
      {
        "name": "Québec",
        "asciiname": "Quebec",
        "parents": {
          "edges": [
            {
              "node": {
                "geonameId": "6251999",
                "asciiname": "Canada"
              }
            }
          ]
        },
        "children": {
          "edges": [
            {
              "node": {
                "geonameId": "6077246",
                "asciiname": "Montreal"
              }
            },
            {
              "node": {
                "geonameId": "5928473",
                "asciiname": "Cote-Nord"
              }
            },
            {
              "node": {
                "geonameId": "6691319",
                "asciiname": "Capitale-Nationale"
              }
            },
            {
              "node": {
                "geonameId": "5881941",
                "asciiname": "Abitibi-Temiscamingue"
              }
            }
          ]
        }
      }
    ]
  }
}
```

### Deeply Nested Hierarchy

#### Query
```
{
  geoname(geonameId: 6115047) {
    name
    asciiname
    children(first: 1) {
      edges {
        node {
          geonameId
          asciiname
          children(first: 1) {
            edges {
              node {
                geonameId
                asciiname
                children(first: 1) {
                  edges {
                    node {
                      geonameId
                      asciiname
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

#### Response
```
{
  "data": {
    "geoname": [
      {
        "name": "Québec",
        "asciiname": "Quebec",
        "children": {
          "edges": [
            {
              "node": {
                "geonameId": "6077246",
                "asciiname": "Montreal",
                "children": {
                  "edges": [
                    {
                      "node": {
                        "geonameId": "8672772",
                        "asciiname": "Senneville",
                        "children": {
                          "edges": []
                        }
                      }
                    }
                  ]
                }
              }
            }
          ]
        }
      }
    ]
  }
}
```

### Find Boundaries

Note that geonames dataset only provides boundaries for country entities. The [premium subscription](http://www.geonames.org/products/premium-data.html) extends this to most administrative divisions. With some effort, this data can also be sourced from other open source datasets and added to the table (such as OpenStreetMaps)

Also note that the `geoJson` response will change when the column is changed from MEDIUMBLOB to JSON upon upgrade to MySQL 5.7.8

#### Query
```
{
  geoname(geonameId: 49518) {
    geonameId
    name
    countryCode
    Boundaries {
      geoJson
    }
  }
}
```

#### Response
```
{
  "data": {
    "geoname": [
      {
        "geonameId": "49518",
        "name": "Republic of Rwanda",
        "countryCode": "RW",
        "Boundaries": {
          "geoJson": "b'{\"type\":\"Polygon\",\"coordinates\":[[[29.96,-2.327],[29.919,-2.703],[29.724,-2.819],[29.438,-2.798],[29.371,-2.84],[29.326,-2.654],[29.15,-2.592],[29.062,-2.602],[29.04,-2.745],[28.897,-2.66],[28.862,-2.531],[28.884,-2.393],[29.119,-2.249],[29.175,-2.119],[29.136,-1.86],[29.362,-1.509],[29.45,-1.506],[29.566,-1.387],[29.66,-1.393],[29.735,-1.34],[29.796,-1.373],[29.824,-1.309],[29.883,-1.356],[29.915,-1.482],[30.052,-1.431],[30.345,-1.131],[30.352,-1.062],[30.47,-1.053],[30.47,-1.156],[30.569,-1.337],[30.738,-1.445],[30.839,-1.651],[30.808,-1.938],[30.9,-2.078],[30.844,-2.206],[30.857,-2.315],[30.782,-2.391],[30.716,-2.357],[30.569,-2.42],[30.409,-2.311],[30.136,-2.438],[29.96,-2.327]]]}'"
        }
      }
    ]
  }
}
```

