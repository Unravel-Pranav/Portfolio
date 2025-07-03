from sqlalchemy import Column, Integer, String
from app.config.database import Base

from sqlalchemy import Column, Integer, String, Text
import json

class About(Base):
    __tablename__ = "about"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    tech_stack = Column(String)  # store JSON string here
    image_url = Column(String)

    def get_tech_stack(self):
        return json.loads(self.tech_stack)

    def set_tech_stack(self, tech_list):
        self.tech_stack = json.dumps(tech_list)
        

