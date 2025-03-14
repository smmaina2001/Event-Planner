from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    
    event = relationship("Event", back_populates="attendees")

    def __repr__(self):
        return f"<Attendee(name={self.name}, event_id={self.event_id})>"

    @classmethod
    def create(cls, session, name, event_id):
        new_attendee = cls(name=name, event_id=event_id)
        session.add(new_attendee)
        session.commit()
        return new_attendee

    @classmethod
    def delete(cls, session, attendee_id):
        attendee = session.query(cls).filter_by(id=attendee_id).first()
        if attendee:
            session.delete(attendee)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, attendee_id):
        return session.query(cls).filter_by(id=attendee_id).first()
