from pydantic import BaseModel
from typing import List, Dict, Optional

class Comment(BaseModel):
    author: str

class User(BaseModel):
    username: str
    password: Optional[str] = None
    likes: Dict[str, int]
    comments: List[Comment]


class AdminUser(User):
    admin_password: str

user = User(username='fdf', likes={'fdf': 23}, comments=[Comment(author="FDFDFD")])

admin_user = AdminUser(username='admin', likes={'admin': 42}, comments=[Comment(author="AdminComment")], admin_password='admin_password')

user2=User(**user)
print(user2)

# User.username='fdf'
# User.password='fdf'
# User.likes={'fdf':23}
# User.comments=Comment.author="FDFDFD"
# user2:User
# user2=user2(**User)
print(user)