from database import Base, engine
from sqlalchemy import Column, Integer, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import MEDIUMBLOB
from sqlalchemy.orm import backref, relationship, relation
from sqlalchemy.types import CHAR, Text, VARCHAR


HierarchyRelationship = Table('hierarchy', Base.metadata,
  Column("parent_id", Integer, ForeignKey('geoname.geoname_id')),
  Column("child_id", Integer, ForeignKey('geoname.geoname_id'))
)

class GeonameModel(Base):
  __tablename__ = 'geoname'
  geoname_id = Column(Integer, primary_key=True)
  Admin1Code = relationship("Admin1CodeModel", uselist=False)
  Admin2Code = relationship("Admin2CodeModel", uselist=False)
  admin5_code = relationship("Admin5CodeModel", uselist=False, back_populates="geoname")
  Boundaries = relationship("BoundariesModel", uselist=False)
  CountryInfo = relation("CountryInfoModel", foreign_keys='CountryInfoModel.iso_alpha2', backref='country', uselist=False)

  children = relationship("GeonameModel",
      secondary=HierarchyRelationship,
      primaryjoin=HierarchyRelationship.c.parent_id==geoname_id,
      secondaryjoin=HierarchyRelationship.c.child_id==geoname_id)
  parents = relation("GeonameModel",
      secondary=HierarchyRelationship,
      primaryjoin=HierarchyRelationship.c.child_id==geoname_id,
      secondaryjoin=HierarchyRelationship.c.parent_id==geoname_id)

  Alternatenames = relationship("AlternatenameModel")
  ContinentCodes = relationship("ContinentCodeModel")

class Admin1CodeModel(Base):
  __tablename__ = 'admin1_codes'
  __table_args__ = (
    PrimaryKeyConstraint("code", "geoname_id"),
  )
  code = Column(CHAR)
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))

class Admin2CodeModel(Base):
  __tablename__ = 'admin2_codes'
  __table_args__ = (
    PrimaryKeyConstraint("code", "name", "asciiname", "geoname_id"),
  )
  code = Column(VARCHAR(30))
  name = Column(Text)
  asciiname = Column(Text)
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))

class Admin5CodeModel(Base):
  __tablename__ = 'admin5_codes'
  __table_args__ = (
    PrimaryKeyConstraint("geoname_id", "admin5_code"),
  )
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))
  admin5_code = Column(VARCHAR(40))
  geoname = relationship("GeonameModel", back_populates="admin5_code")

class AlternatenameModel(Base):
  __tablename__ = 'alternatenames'
  alternatename_id = Column(Integer, primary_key=True)

class BoundariesModel(Base):
  __tablename__ = 'boundaries'
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"), primary_key=True)
  # geo_json is actually a MEDIUMBLOB, however that response is in bytes and not json_seraliziable
  # This is temporary, until an upgrade to MySQL 5.7 allows for JSON format
  # Although the data size exceeds Text, SQLAlchemy will nevertheless fetch all data, without truncation
  geo_json = Column(Text)

class ContinentCodeModel(Base):
  __tablename__ = 'continent_codes'
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"), primary_key=True)

class CountryInfoModel(Base):
  __tablename__ = 'country_info'
  __table_args__ = (
    PrimaryKeyConstraint("iso_alpha2", "iso_alpha3"),
  )
  iso_alpha2 = Column(CHAR(2), ForeignKey("geoname.country_code"), nullable=False)
  iso_alpha3 = Column(CHAR(3), nullable=False)
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))

class FeatureCodeModel(Base):
  __tablename__ = 'feature_codes'
  code = Column(VARCHAR(7), primary_key=True)

class IsoLanguageCodeModel(Base):
  __tablename__ = 'iso_language_codes'
  __table_args__ = (
    PrimaryKeyConstraint("iso_639_1", "iso_639_2", "iso_639_3"),
  )
  iso_639_1 = Column(VARCHAR(50))
  iso_639_2 = Column(VARCHAR(50))
  iso_639_3 = Column(CHAR(4))

class PostalCodeModel(Base):
  __tablename__ = 'postal_codes'
  __table_args__ = (
    PrimaryKeyConstraint("country_code", "postal_code", "admin_code1", "admin_code2", "admin_code3"),
  )
  country_code = Column(CHAR(2))
  postal_code = Column(VARCHAR(20))
  admin_code1 = Column(VARCHAR(20))
  admin_code2 = Column(VARCHAR(20))
  admin_code3 = Column(VARCHAR(20))

class TimezoneModel(Base):
  __tablename__ = 'timezones'
  timezone_id = Column(Integer, primary_key=True, nullable=False)

class UserTagModel(Base):
  __tablename__ = 'usertags'
  __table_args__ = (
    PrimaryKeyConstraint("geoname_id", "tag"),
  )
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"), nullable=False)
  tag = Column(VARCHAR(100))

Base.prepare(engine)

