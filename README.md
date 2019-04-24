# Geonames GraphQL

A graphQL server for the open source [geonames database](http://download.geonames.org/export/dump/)

Note that this assumes you have already imported the database to MySQL. Most column configurations are determined dynamically, but you can verify your setup in [TABLE_STRUCTURE.sql](docs/TABLE_STRUCTURE.sql) or create it from scratch using that SQL file.

```
mysql> show tables;
+------------------------------+
| Tables_in_geonames           |
+------------------------------+
| admin1_codes                 |
| admin2_codes                 |
| admin5_codes                 |
| alternatenames               |
| boundaries                   |
| continent_codes              |
| country_info                 |
| feature_codes                |
| geoname                      |
| hierarchy                    |
| iso_language_codes           |
| postal_codes                 |
| timezones                    |
| usertags                     |
+------------------------------+
14 rows in set (0.01 sec)
```

### Filter Params
```
-geoname_id
-name
-asciiname
-latitude
-longitude
-feature_class
-feature_code
-country_code
-admin1_code
-admin2_code
-admin3_code
-admin4_code
-admin5_code
-min_population
-max_population
```

### Schema
The Geonames dataset provides a large amount of information. The schema follows the provided tables
```
{
  geoname {
    geonameId
    name
    asciiname
    Alternatenames {
      edges {
        node {
          alternatename
          alternatenameId
          isHistoric
          isColloquial
          isShortname
          isPreferredName
        }
      }
    }
    latitude
    longitude
    featureClass
    featureCode
    countryCode
    CountryInfo {
      isoAlpha2
      isoAlpha3
      isoNumeric
      fipsCode
      name
      capital
      areaInSqKm
      population
      continent
      tld
      currency
      currencyName
      phone
      postalCodeFormat
      postalCodeRegex
      languages
      neighbours
      equivalentFipsCode
    }
    cc2
    admin1Code
    Admin1Code{
      code
      asciiname
    }
    admin2Code
    Admin2Code {
      code
      name
      asciiname
    }
    admin3Code
    admin4Code
    admin5Code {
      admin5Code
    }
    population
    elevation
    dem
    timezone
    modificationDate
    children {
      edges {
        node {
          #Full geoname object and all its properties available here
          geonameId
        }
      }
    }
    parents {
      edges {
        node {
          #Full geoname object and all its properties available here
          geonameId
        }
      }
    }
  }
}

```

### Running

Ensure MySQL is running and then start the server:
```
❯ python3 app.py
```

Navigate your browser to localhost:5000 to use the interactive request builder, or use the API directly:
```
curl 'http://localhost:5000/graphql?' --data '{"query":"{
    geoname(geonameId: 6115047) {
      asciiname
    }
  }",
  "variables":null,
  "operationName":null
}'
```

### Sample Queries

See [EXAMPLES.md](docs/EXAMPLES.md)

### Environemnt

* Python 3.7.2
* MacOS 10.13
* MySQL 5.6.37

