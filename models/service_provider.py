from sqlalchemy import Column, Integer, String
from database import Base

class ServiceProvider(Base):
    __tablename__ = 'service_providers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    service_type = Column(String, nullable=False)

    def __repr__(self):
        return f"<ServiceProvider(name={self.name}, service_type={self.service_type})>"

    @classmethod
    def create(cls, session, name, service_type):
        new_provider = cls(name=name, service_type=service_type)
        session.add(new_provider)
        session.commit()
        return new_provider

    @classmethod
    def delete(cls, session, provider_id):
        provider = session.query(cls).filter_by(id=provider_id).first()
        if provider:
            session.delete(provider)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, provider_id):
        return session.query(cls).filter_by(id=provider_id).first()
