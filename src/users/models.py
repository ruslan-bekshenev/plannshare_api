import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class User(Base):
  __tablename__ = "users"
  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  username = Column(String, unique=True, nullable=False)
  email = Column(String, unique=True, nullable=False)
  hashed_password = Column(String)