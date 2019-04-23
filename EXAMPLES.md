# Example Queries

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
