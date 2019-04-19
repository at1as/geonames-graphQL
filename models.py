from database import Base, engine
from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import CHAR, Text, VARCHAR

class GeonameModel(Base):
  __tablename__ = 'geoname'
  geoname_id = Column(Integer, primary_key=True)
  #child_id   = Column(Integer, ForeignKey("hierarchy.child_id"))
  #parent_id  = Column(Integer, ForeignKey("hierarchy.parent_id"))

  Admin1Codes    = relationship("Admin1CodeModel")
  Admin2Codes    = relationship("Admin2CodeModel")
  Admin5Codes    = relationship("Admin5CodeModel")
  Alternatenames = relationship("AlternatenameModel")
  ContinentCodes = relationship("ContinentCodeModel")
  CountryInfo    = relationship("CountryInfoModel")
  #Child          = relationship("HierarchyModel", foreign_keys=[child_id])
  #Parent         = relationship("HierarchyModel", foreign_keys=[parent_id])

  #Parent         = relationship("HierarchyModel", Column(Integer, ForeignKey("hierarchy.parent_id"))
  #HierarchyParent = relationship("HierarchyModel",
  #    primaryjoin=HierarchyModel().child_id,
  #    secondaryjoin="hierarchy.parent_id"
  #)

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
  code = Column(CHAR)
  name = Column(Text)
  asciiname = Column(Text)
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))

class Admin5CodeModel(Base):
  __tablename__ = 'admin5_codes'
  __table_args__ = (
    PrimaryKeyConstraint("geoname_id", "admin5_code"),
  )
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))
  admin5_code = Column(Integer)

class AlternatenameModel(Base):
  __tablename__ = 'alternatenames'
  alternatename_id = Column(Integer, primary_key=True)

class ContinentCodeModel(Base):
  __tablename__ = 'continent_codes'
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"), primary_key=True)

class CountryInfoModel(Base):
  __tablename__ = 'country_info'
  __table_args__ = (
    PrimaryKeyConstraint("iso_alpha2", "iso_alpha3"),
  )
  iso_alpha2 = Column(CHAR(2), nullable=False)
  iso_alpha3 = Column(CHAR(3), nullable=False)
  geoname_id = Column(Integer, ForeignKey("geoname.geoname_id"))

class FeatureCodeModel(Base):
  __tablename__ = 'feature_codes'
  code = Column(VARCHAR, primary_key=True)

class HierarchyModel(Base):
  __tablename__ = 'hierarchy'
  __table_args__ = (
    PrimaryKeyConstraint("parent_id", "child_id"), # key is also on 'type', a reserved word in python
  )
  parent_id = Column(Integer, ForeignKey("geoname.geoname_id"), nullable=False)
  child_id = Column(Integer, ForeignKey("geoname.geoname_id"), nullable=False)

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

