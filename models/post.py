from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    image = Column(String)
    timestamp = Column(DateTime, default=datetime.now(datetime.utc))
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    likes = relationship('Like', back_populates='post')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'image': self.image,
            'timestamp': self.timestamp.isoformat()
        }
