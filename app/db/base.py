# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base   
from app.models.item import Item   
from app.models.user import User   
from app.models.country import Country
from app.models.user_preference import UserPreference
from app.models.user_interest import UserInterest
from app.models.user_image import UserImage
from app.models.interest import Interest



from app.models.chat import Chat
from app.models.message import Message
from app.models.notification import Notification

from app.models.user_report import UserReport
from app.models.user_location import UserLocation
from app.models.activity_log import ActivityLog 
from app.models.user_block import UserBlock
