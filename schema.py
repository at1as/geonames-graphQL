import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *

class Geoname(SQLAlchemyObjectType):
    class Meta:
        model = GeonameModel
        interfaces = (graphene.relay.Node, )

class Admin1Code(SQLAlchemyObjectType):
    class Meta:
        model = Admin1CodeModel
        interfaces = (graphene.relay.Node, )

class Admin2Code(SQLAlchemyObjectType):
    class Meta:
        model = Admin2CodeModel
        interfaces = (graphene.relay.Node, )

class Admin5Code(SQLAlchemyObjectType):
    class Meta:
        model = Admin5CodeModel
        interfaces = (graphene.relay.Node, )

class Alternatename(SQLAlchemyObjectType):
    class Meta:
        model = AlternatenameModel
        interfaces = (graphene.relay.Node, )

class ContinentCode(SQLAlchemyObjectType):
    class Meta:
        model = ContinentCodeModel 
        interfaces = (graphene.relay.Node, )

class CountryInfo(SQLAlchemyObjectType):
    class Meta:
        model = CountryInfoModel 
        interfaces = (graphene.relay.Node, )

class UserTag(SQLAlchemyObjectType):
    class Meta:
        model = UserTagModel 
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    
    node = graphene.relay.Node.Field()
    geoname = graphene.List(
      Geoname,
      geoname_id     = graphene.Int(default_value=None),
      name           = graphene.String(default_value=None),
      asciiname      = graphene.String(default_value=None),
      #latitude       = graphene.Float(default_value=None),
      #longitude      = graphene.Float(default_value=None),
      feature_class  = graphene.String(default_value=None),
      feature_code   = graphene.String(default_value=None),
      country_code   = graphene.String(default_value=None),
      admin1_code    = graphene.String(default_value=None),
      admin2_code    = graphene.String(default_value=None),
      admin3_code    = graphene.String(default_value=None),
      admin4_code    = graphene.String(default_value=None),
      admin5_code    = graphene.String(default_value=None),

      min_population = graphene.Float(default_value=None),
      max_population = graphene.Float(default_value=None),

      limit          = graphene.Int(default_value=5)
    )
    
    def resolve_geoname(self, info, **args):
        query = Geoname.get_query(info)
        geoname_id = args.get('geoname_id')
        limit = args.get('limit')

        if args.get('geoname_id'):
          query = query.filter(Geoname._meta.model.geoname_id == args.get('geoname_id'))
        if args.get('name'):
          query = query.filter(Geoname._meta.model.asciiname.like(args.get('name') + "%"))
        if args.get('asciiname'):
          query = query.filter(Geoname._meta.model.asciiname.like(args.get('asciiname') + "%"))
        if args.get('feature_class'):
          query = query.filter(Geoname._meta.model.feature_class == args.get('feature_class'))
        if args.get('feature_code'):
          query = query.filter(Geoname._meta.model.feature_code == args.get('feature_code'))
        if args.get('country_code'):
          query = query.filter(Geoname._meta.model.country_code == args.get('country_code'))
        if args.get('admin1_code'):
          query = query.filter(Geoname._meta.model.admin1_code == args.get('admin1_code'))
        if args.get('admin2_code'):
          query = query.filter(Geoname._meta.model.admin2_code == args.get('admin2_code'))
        if args.get('admin3_code'):
          query = query.filter(Geoname._meta.model.admin3_code == args.get('admin3_code'))
        if args.get('admin4_code'):
          query = query.filter(Geoname._meta.model.admin4_code == args.get('admin4_code'))
        if args.get('admin5_code'):
          pass # TODO
        if args.get('min_population'):
          query = query.filter(Geoname._meta.model.population > args.get('min_population'))
        if args.get('max_population'):
          query = query.filter(Geoname._meta.model.population < args.get('max_population'))

        # Generally the most populous matching location is the we're searching for
        query = query.order_by(Geoname._meta.model.population)
        
        return query.limit(limit).all()

schema = graphene.Schema(query=Query, types=[Geoname])

