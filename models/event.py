from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    
    # Relationship to Attendee
    attendees = relationship("Attendee", back_populates="event")
    
    def __repr__(self):
        return f"<Event(name={self.name}, date={self.date})>"

    @classmethod
    def create(cls, session, name, date):
        new_event = cls(name=name, date=date)
        session.add(new_event)
        session.commit()
        return new_event

    @classmethod
    def delete(cls, session, event_id):
        event = session.query(cls).filter_by(id=event_id).first()
        if event:
            session.delete(event)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, event_id):
        return session.query(cls).filter_by(id=event_id).first()
