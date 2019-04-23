# Geonames GraphQL

A graphQL server for the open source [geonames database](http://download.geonames.org/export/dump/)

Note that this assumes you have already imported the database to MySQL. Most column configurations are determined dynamically, however very in models.py that those specified match your own settings.


## Usage

#### Hierarchy
Query:
```
{
  geoname(geonameId:6251999) {
		geonameId
    asciiname
    parents {
      edges {
        node {
          geonameId
          asciiname
        }
      }
    }
    children(first:2) {
      edges {
        node {
          geonameId
          asciiname
          children(first:1) {
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
```
Response:
```
{
  "data": {
    "geoname": [
      {
        "geonameId": "6251999",
        "asciiname": "Canada",
        "parents": {
          "edges": [
            {
              "node": {
                "geonameId": "6255149",
                "asciiname": "North America"
              }
            },
            {
              "node": {
                "geonameId": "7729890",
                "asciiname": "Northern America"
              }
            }
          ]
        },
        "children": {
          "edges": [
            {
              "node": {
                "geonameId": "6354959",
                "asciiname": "Newfoundland and Labrador",
                "children": {
                  "edges": []
                }
              }
            },
            {
              "node": {
                "geonameId": "6115047",
                "asciiname": "Quebec",
                "children": {
                  "edges": [
                    {
                      "node": {
                        "geonameId": "6077246",
                        "asciiname": "Montreal"
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


#### Sample Query:
```
{
  geoname(limit: 1, asciiname: "Vancouver", featureClass: "P", countryCode: "CA") {
    geonameId
    name
    population
    featureCode
    featureClass
    admin1Code
    admin2Code
    Admin1Codes {
      edges {
        node {
          geonameId
        }
      }
    }
    Admin2Codes {
      edges {
        node {
          geonameId
        }
      }
    }
    Alternatenames(first: 3) {
      edges {
        node {
          alternatename
        }
      }
    }
    Admin5Codes {
      edges {
        node {
          geonameId
          admin5Code
        }
      }
    }
    ContinentCodes {
      edges {
        node {
          code
        }
      }
    }
    CountryInfo {
      edges {
        node {
          currency
        }
      }
    }
  }
}
```
#### Sample Response:
```
{
  "data": {
    "geoname": [
      {
        "geonameId": "6173331",
        "name": "Vancouver",
        "population": 600000,
        "featureCode": "PPL",
        "featureClass": "P",
        "admin1Code": "02",
        "admin2Code": "",
        "Admin1Codes": {
          "edges": []
        },
        "Admin2Codes": {
          "edges": []
        },
        "Alternatenames": {
          "edges": [
            {
              "node": {
                "alternatename": "Vancouver"
              }
            },
            {
              "node": {
                "alternatename": "Vancouver"
              }
            },
            {
              "node": {
                "alternatename": "Vancouver"
              }
            }
          ]
        },
        "Admin5Codes": {
          "edges": []
        },
        "ContinentCodes": {
          "edges": []
        },
        "CountryInfo": {
          "edges": []
        }
      }
    ]
  }
}
```

### Environemnt

Python 3.7.2 on MacOS 10.13

